# C2-MS-CAPSTONE

This repository supports a cybersecurity capstone project comparing two approaches for detecting command-and-control (C2) traffic: a behavior-based machine learning model and a traditional rule-based IDS. Specifically, it evaluates a Random Forest model trained on packet-level features against Suricata using the Emerging Threats Open ruleset. All traffic is collected in a controlled lab environment using multiple HTTPS-based C2 frameworks to simulate realistic attack scenarios.

---

## Project Goals

- Collect labeled C2 and normal traffic using open-source HTTPS-based C2 frameworks in a controlled environment.
- Extract packet-level features (timing, structure, and TCP behavior) that don’t rely on payload contents.
- Train and evaluate a Random Forest model to detect C2 traffic based on behavioral patterns.
- Compare the ML model’s performance against Suricata using the ET Open ruleset.
- Analyze model by testing on unseen C2 frameworks and realistic traffic mixes.

---

## Repository Structure

```
.
├── code/             # Jupyter notebooks for training, validation, inference, and reporting
├── data/             # Cleaned feature CSVs generated from PCAPs
├── documents/        # Project report, ET Open ruleset, topology diagrams
├── pcaps/            # Raw PCAP files (not committed; managed with Git LFS) 
├── requirements.txt  # Python dependencies for notebooks and scripts
└── README.md         # Project overview (this file)
```

---

## Getting Started

This project uses a Python virtual environment located in `.venv`. All scripts and Jupyter notebooks should be run from within this environment to ensure dependencies are properly managed.

### 1. Set up the virtual environment

If the environment doesn't already exist, you can create it manually:

```bash
python -m venv .venv
```

Then activate it:
- On Windows:
  ```bash
  .venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

Once activated, install the required packages:

```bash
pip install -r requirements.txt
```

### 2. Running code and notebooks

All scripts and notebooks assume the environment is active. For training, evaluation, and reporting information, refer to [`code/code.md`](code/code.md).

---

## Suricata Configuration

Suricata was run in **offline (PCAP) mode**, meaning it processed previously captured `.pcap` files rather than live network traffic. Traffic was captured on the Windows 10 target machine and then transferred to a separate analysis machine where Suricata was installed.

The **Emerging Threats Open** ruleset was used for detection. The ruleset version was retrieved on **April 17, 2025**. You can find the exact ruleset used at [`documents/emerging-all.rules`](./documents/emerging-all.rules).

PCAPs were analyzed using a command similar to:

```bash
suricata -r /path/to/pcap/file.pcap -S /path/to/rules/file.rules
```
