import socket
import time
import os

def connect_to_server():
    """
    Simulates a network beacon (sending data to a server).
    In reality, it just connects to Google DNS (8.8.8.8).
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80)) 
        return True
    except:
        return False

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*40)
    print("💀 MALWARE SIMULATOR (SAFE MODE)")
    print("="*40)
    print(f"[+] Process ID (PID): {os.getpid()}")
    print("[*] Status: Running in background...")
    print("[*] Action: Attempting network connection...")
    
    if connect_to_server():
        print("[+] Connection Established!")
        print("    -> PySentry should flag this as 'HIGH RISK' (Script + Network)")
    else:
        print("[-] Connection Failed.")

    print("\n[!] I will stay active for 300 seconds.")
    print("[!] Run 'pysentry.py' to detect and kill me.")
    
    try:
        time.sleep(300)
    except KeyboardInterrupt:
        print("\n[x] Simulation stopped.")

if __name__ == "__main__":
    # Set a custom title for the window
    if os.name == 'nt':
        os.system("title Malware_Simulator")
    main()