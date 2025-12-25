# 🛡️ PySentry: Heuristic Threat Monitor

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)

**PySentry** is a lightweight, heuristic-based Intrusion Detection System (IDS) written in Python. Unlike traditional antiviruses that look for specific file signatures, PySentry analyzes **process behavior** in real-time to identify potential threats like keyloggers, reverse shells, and spyware.

---

## 📖 Table of Contents
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Disclaimer](#-disclaimer)
- [License](#-license)

---

## 🚀 Features

* **🕵️ Heuristic Analysis:** Detects threats based on behavior (e.g., a Python script running in the background and connecting to the internet).
* **🛡️ Smart Whitelisting:** Automatically ignores safe system processes and developer tools (VS Code, NVIDIA, Spotify, etc.) to prevent false alarms.
* **📡 Network Monitoring:** Specifically watches for `inet` (Internet) socket connections initiated by background processes.
* **🛑 Integrated Kill Switch:** Allows the user to terminate suspicious processes immediately from the dashboard.
* **💻 Dashboard UI:** A clean, color-coded terminal interface for real-time monitoring.

---

## 🧠 How It Works

PySentry operates on a strictly defined set of rules to filter noise and highlight danger:

1.  **Scan:** It iterates through all active system processes (PIDs).
2.  **Filter:** It compares processes against a `SAFE_PATHS` whitelist (System32, Program Files, etc.) and `IGNORE_PIDS` (System Idle).
3.  **Analyze:** It checks for "Script Engine" signatures (Python, PowerShell, CMD) and active network connections.
4.  **Flag:**
    * **🔴 HIGH RISK:** A script engine is active AND has an established network connection.
    * **🟡 MEDIUM RISK:** A script engine is active in the background (potential local logger).

---

## 📦 Installation

### Prerequisites
* Python 3.6 or higher
* `pip` (Python Package Manager)

### Setup
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/PySentry.git](https://github.com/YOUR_USERNAME/PySentry.git)
    cd PySentry
    ```

2.  **Install dependencies:**
    PySentry relies on `psutil` for low-level system access.
    ```bash
    pip install -r requirements.txt
    ```

---

## 🛠️ Usage

### 1. Run the Monitor (Defense)
Start the detection engine. You must run this with Administrator privileges to scan all processes effectively.

**Windows:**
```powershell
python pysentry.py
(Right-click your terminal and select "Run as Administrator" for best results)

Linux/macOS:

Bash

sudo python3 pysentry.py
2. Run the Simulator (Test)
To verify that PySentry is working, use the included Safe Simulator. This script mimics the behavior of a malware beacon (connecting to a public DNS) to test the detector.

Open a new terminal window (separate from the detector).

Run the simulator:

Bash

python simulation_tool.py
Check your PySentry window. You should immediately see a 🔴 HIGH RISK alert for the simulation_tool.py process.

Use the PySentry input prompt to kill the simulator PID.

📂 Project Structure
Plaintext

PySentry/
│
├── pysentry.py          # MAIN TOOL: The detection engine and dashboard
├── simulation_tool.py   # TEST TOOL: Safely mimics malware behavior
├── requirements.txt     # Dependencies list (psutil)
└── README.md            # Documentation
⚙️ Configuration
You can customize the detection sensitivity by editing the pysentry.py file directly:

SAFE_PATHS: Add paths here to whitelist trusted applications that are triggering false positives.

Python

SAFE_PATHS = [
    r"C:\Windows\System32",
    r"C:\Program Files\NVIDIA Corporation",
    "TrustedApp.exe"
]
SCRIPT_ENGINES: Add other interpreters you want to monitor (e.g., ruby, perl, java) to the list in pysentry.py.

⚠️ Disclaimer
THIS SOFTWARE IS FOR EDUCATIONAL AND DEFENSIVE PURPOSES ONLY.

Do not use the simulator code on networks or systems you do not own.

The authors are not responsible for any damage caused by the misuse of this tool.

Always test security tools in a controlled environment (Virtual Machine) before using them on critical systems.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

<p align="center"> Developed by <strong>BGx</strong> (Devansh Agarwal)


<em>Cybersecurity Enthusiast & Developer</em> </p>
