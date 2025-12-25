import psutil
import os
import time
import sys
from datetime import datetime

# ==========================================
# 🎨 COLOR CODES & BANNER
# ==========================================
class Colors:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

BANNER = f"""{Colors.CYAN}
    ____        _____            __                  
   / __ \__  __/ ___/___  ____  / /________  __      
  / /_/ / / / /\__ \/ _ \/ __ \/ __/ ___/ / / /      
 / ____/ /_/ /___/ /  __/ / / / /_/ /  / /_/ /       
/_/    \__, //____/\___/_/ /_/\__/_/   \__, /        
      /____/                          /____/         
{Colors.RESET}{Colors.BOLD}   v1.0 - Heuristic Process Monitor & Killer{Colors.RESET}
"""

# ==========================================
# 🛡️ CONFIGURATION
# ==========================================
# PIDs to ignore (0=System Idle, 4=System)
IGNORE_PIDS = [0, 4] 

# Whitelist: Paths containing these strings are considered "Safe"
# This prevents false positives from your own dev tools or system files.
SAFE_PATHS = [
    r"C:\Windows\System32",
    r"C:\Program Files\NVIDIA Corporation",
    r"C:\Program Files\WindowsApps",
    r"C:\Program Files (x86)",
    "Antigravity",       # Code Editor (Cursor)
    "VSCode", "Microsoft VS Code",
    "electron", "ms-python",
    "AppData\Local\Microsoft\Teams",
    "Discord", "Spotify", "Steam",
    "Chrome", "Firefox", "Edge"
]

# Keywords that indicate a process might be a script engine
SCRIPT_ENGINES = ["python", "cmd.exe", "powershell.exe", "bash", "wscript.exe", "cscript.exe"]

def clear_screen():
    """Clears the terminal screen for a dashboard effect."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_process_info(proc):
    """
    Safely retrieves process name, command line, and executable path.
    Returns (None, None, None) if access is denied.
    """
    try:
        name = proc.name()
        cmdline = proc.cmdline()
        # Reconstruct the full command string
        full_cmd = " ".join(cmdline) if cmdline else name
        exe_path = proc.exe()
        return name, full_cmd, exe_path
    except (psutil.AccessDenied, psutil.ZombieProcess, psutil.NoSuchProcess):
        return None, None, None

def format_path(path, length=50):
    """Truncates long paths to fit the dashboard UI."""
    if not path: return "?"
    if len(path) <= length:
        return path
    return ".." + path[-(length-2):]

def is_safe(full_cmd, exe_path):
    """
    Checks if the process is in the whitelist.
    Returns True if safe, False if suspicious.
    """
    if exe_path:
        for safe in SAFE_PATHS:
            if safe.lower() in exe_path.lower(): return True
    if full_cmd:
        for safe in SAFE_PATHS:
            if safe.lower() in full_cmd.lower(): return True
    return False

def check_network(proc):
    """Returns True if the process has active internet connections."""
    try:
        # kind='inet' ensures we only look for IPv4/IPv6 connections
        connections = proc.net_connections(kind='inet')
        return len(connections) > 0
    except (psutil.AccessDenied, psutil.ZombieProcess):
        return False

def scan_system():
    """Main scanning logic."""
    clear_screen()
    print(BANNER)
    print(f"{Colors.BLUE}[*] Scanning active processes... | Time: {datetime.now().strftime('%H:%M:%S')}{Colors.RESET}")
    print(f"{Colors.BLUE}{'='*95}{Colors.RESET}")
    print(f"{Colors.BOLD}{'PID':<8} {'THREAT LEVEL':<15} {'ACTIVITY TYPE':<20} {'PROCESS / COMMAND'}{Colors.RESET}")
    print(f"{'-'*95}")

    detected_threats = []
    high_risks = []
    medium_risks = []

    # Iterate over all running processes
    for proc in psutil.process_iter(['pid']):
        try:
            pid = proc.pid
            if pid in IGNORE_PIDS: continue

            name, full_cmd, exe_path = get_process_info(proc)
            if name is None: continue 

            # Filter out whitelisted apps
            if is_safe(full_cmd, exe_path): continue

            # Analyze behavior
            is_connected = check_network(proc)
            is_script = any(eng in name.lower() for eng in SCRIPT_ENGINES)
            
            threat_data = None
            
            # --- HEURISTIC RULES ---
            
            # RULE 1: Script Engine + Internet Connection = HIGH RISK
            # (Common behavior for reverse shells, keyloggers, etc.)
            if is_script and is_connected:
                threat_data = {
                    "pid": pid, "level": "HIGH 🚨", "color": Colors.RED,
                    "reason": "Script + Network", "cmd": full_cmd
                }
                high_risks.append(threat_data)
                
            # RULE 2: Python hidden in a weird location connecting to internet
            elif is_connected and "python" in full_cmd.lower():
                threat_data = {
                    "pid": pid, "level": "HIGH 🚨", "color": Colors.RED,
                    "reason": "Python + Network", "cmd": full_cmd
                }
                high_risks.append(threat_data)

            # RULE 3: Script Engine running silently (Potential local gathering)
            elif is_script:
                threat_data = {
                    "pid": pid, "level": "MEDIUM ⚠️", "color": Colors.YELLOW,
                    "reason": "Script Running", "cmd": full_cmd
                }
                medium_risks.append(threat_data)

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Print results (High Priority First)
    for item in high_risks:
        detected_threats.append(item['pid'])
        clean_cmd = format_path(item['cmd'])
        print(f"{item['color']}{item['pid']:<8} {item['level']:<15} {item['reason']:<20} {clean_cmd}{Colors.RESET}")

    for item in medium_risks:
        detected_threats.append(item['pid'])
        clean_cmd = format_path(item['cmd'])
        print(f"{item['color']}{item['pid']:<8} {item['level']:<15} {item['reason']:<20} {clean_cmd}{Colors.RESET}")

    return detected_threats

def kill_process(pid):
    """Attempts to terminate a process."""
    try:
        p = psutil.Process(pid)
        name = p.name()
        print(f"\n{Colors.YELLOW}[!] Attempting to terminate {name} (PID: {pid})...{Colors.RESET}")
        p.terminate()
        p.wait(timeout=3)
        print(f"{Colors.GREEN}[+] SUCCESS: Process terminated.{Colors.RESET}")
    except psutil.NoSuchProcess:
        print(f"{Colors.RED}[-] Error: Process no longer exists.{Colors.RESET}")
    except psutil.AccessDenied:
        print(f"{Colors.RED}[-] Error: Access Denied. Run as Administrator.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Error: {e}{Colors.RESET}")

def main():
    try:
        while True:
            threats = scan_system()
            
            if not threats:
                print(f"\n{Colors.GREEN}[+] SYSTEM SECURE: No suspicious background scripts detected.{Colors.RESET}")
            else:
                print(f"\n{Colors.RED}[!] ACTION REQUIRED: {len(threats)} suspicious process(es) found.{Colors.RESET}")
                
            print(f"\n{Colors.BLUE}[INPUT]{Colors.RESET} Enter PID to KILL, [Enter] to Rescan, or 'q' to Quit:")
            choice = input("> ").strip().lower()

            if choice == 'q':
                print("Exiting PySentry...")
                break
            elif choice == "":
                continue
            elif choice.isdigit():
                pid = int(choice)
                if pid in threats:
                    kill_process(pid)
                    time.sleep(2)
                else:
                    print(f"{Colors.YELLOW}[!] PID {pid} was not flagged. Force kill anyway? (y/n){Colors.RESET}")
                    if input("> ").lower() == 'y':
                        kill_process(pid)
                        time.sleep(2)
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()