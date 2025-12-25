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
