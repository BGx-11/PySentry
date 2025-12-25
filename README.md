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
