# 🛡️ PySentry: Process Threat Monitor

PySentry is a lightweight, Python-based cybersecurity tool designed to detect and monitor suspicious background processes. It uses **heuristic analysis** to identify potential keyloggers, reverse shells, and unauthorized scripts running on your system.

**Current Version:** v1.0

## 🚀 Features

* **Heuristic Detection:** Flags processes based on behavior (e.g., Python scripts connecting to the internet).
* **Smart Filtering:** Whitelists known safe applications (VS Code, Spotify, NVIDIA, etc.) to reduce false positives.
* **Real-time Dashboard:** Color-coded terminal UI for instant threat assessment.
* **Kill Switch:** Terminate suspicious processes directly from the tool.
* **Cross-Platform:** Works on Windows (primary target), Linux, and macOS.

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/PySentry.git](https://github.com/YOUR_USERNAME/PySentry.git)
    cd PySentry
    ```

2.  **Install dependencies:**
    PySentry requires `psutil` to interact with system processes.
    ```bash
    pip install -r requirements.txt
    ```

## 🛠️ Usage

### 1. Run the Detector
Start the monitoring dashboard:
```bash
python pysentry.py
