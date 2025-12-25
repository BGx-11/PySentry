# 🛡️ PySentry: Heuristic Threat Monitor

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)

**PySentry** is a lightweight, heuristic-based Intrusion Detection System (IDS) written in Python.  
Unlike traditional antiviruses that rely on static signatures, PySentry analyzes **process behavior in real time** to identify potential threats such as keyloggers, reverse shells, and spyware.

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

- **🕵️ Heuristic Analysis**  
  Detects threats based on suspicious behavior rather than known signatures.

- **🛡️ Smart Whitelisting**  
  Automatically ignores trusted system paths and common applications to reduce false positives.

- **📡 Network Monitoring**  
  Watches for active `inet` (internet) socket connections from background processes.

- **🛑 Integrated Kill Switch**  
  Instantly terminate suspicious processes directly from the dashboard.

- **💻 Terminal Dashboard**  
  Clean, color-coded, real-time monitoring interface.

---

## 🧠 How It Works

PySentry follows a rule-based detection pipeline:

1. **Scan** – Iterates through all running system processes (PIDs).
2. **Filter** – Excludes safe system paths (`SAFE_PATHS`) and ignored PIDs.
3. **Analyze** – Checks for script engines (Python, PowerShell, CMD) and active network connections.
4. **Flag**
   - **🔴 HIGH RISK**: Script engine + active internet connection  
   - **🟡 MEDIUM RISK**: Script engine running silently in background

---

## 📦 Installation

### Prerequisites
- Python 3.6+
- `pip`

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/BGx-11/PySentry.git
   cd PySentry
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Usage

### 1. Run the Monitor (Defense)

> ⚠️ Administrator / root privileges are recommended for full visibility.

**Windows**

```powershell
python pysentry.py
```

*(Run terminal as Administrator)*

**Linux / macOS**

```bash
sudo python3 pysentry.py
```

---

### 2. Run the Simulator (Test)

A safe simulator is included to validate detection.

1. Open a **new terminal window**
2. Run:

   ```bash
   python simulation_tool.py
   ```
3. PySentry should instantly show a **🔴 HIGH RISK** alert.
4. Use the PySentry prompt to kill the simulator PID.

---

## 📂 Project Structure

```text
PySentry/
│
├── pysentry.py          # Main detection engine + dashboard
├── simulation_tool.py   # Safe malware behavior simulator
├── requirements.txt     # Dependencies (psutil)
└── README.md            # Documentation
```

---

## ⚙️ Configuration

Edit `pysentry.py` to fine-tune detection.

### Whitelist Trusted Paths

```python
SAFE_PATHS = [
    r"C:\Windows\System32",
    r"C:\Program Files\NVIDIA Corporation",
    "TrustedApp.exe"
]
```

### Monitor Additional Script Engines

Add interpreters like `ruby`, `perl`, or `java` to the `SCRIPT_ENGINES` list.

---

## ⚠️ Disclaimer

**FOR EDUCATIONAL AND DEFENSIVE PURPOSES ONLY**

* Do not run the simulator on systems you do not own
* The author is not responsible for misuse
* Always test security tools in a controlled environment (VM recommended)

---

## 📄 License

This project is licensed under the **MIT License**.

---

<p align="center">
<strong>Developed by BGx (Devansh Agarwal)</strong><br>
<em>Cybersecurity Enthusiast & Developer</em>
</p>
```

