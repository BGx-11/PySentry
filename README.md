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
