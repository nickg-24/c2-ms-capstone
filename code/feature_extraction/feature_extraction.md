# Feature Extraction Script for Packet-Level C2 Detection
This script extracts packet-level features from a PCAP file using `tshark` and outputs a CSV file for use in training or evaluating a machine learning model for detecting command-and-control (C2) traffic.

## Overview
This script focuses on packet-level features to detect C2 traffic, avoiding reliance on decrypted payloads or flow-based aggregation. Instead, it captures timing, structure, and TCP behaviors that may vary between C2 frameworks and normal traffic.

Key Design Decisions:
- Only IP-layer packets are processed (filters out ARP, L2 broadcast, etc.).
- C2 traffic is dynamically labeled using a hardcoded C2 server IP.
- Internal vs. external IPs are abstracted into binary features to support generalization beyond specific IP addresses.
- Structural and temporal behaviors (e.g., inter-packet timing, TCP flags) are emphasized as encrypted payloads cannot be used.

---

## Features Extracted
1. Frame Length (`frame.len`)
- **What it measures:** Size of the packet in bytes.
- **Why it's included:** Different C2 frameworks may produce characteristic packet sizes (e.g., small, uniform packets or padded traffic).

2. IP Protocol (`ip.proto`)
- **What it measures:** Transport layer protocol (e.g., TCP = 6, UDP = 17).
- **Why it's included:** All frameworks use TCP (HTTPS), but this allows detection of protocol anomalies if they occur.

3. Source/Destination IP Class (`src_ip`, `dst_ip`)
- **What it measures:** Whether the IP address is internal (0) or external (1).
- **Why it's included:** Abstracts IP identity into a generalizable behavioral feature that doesn't rely on specific IPs.

4. C2 Label (`c2_label`)
- **What it measures:** Binary label indicating whether the packet is part of C2 traffic (1) or not (0), based on hardcoded C2 IP.
- **Why it's included:** Enables supervised learning by distinguishing C2 vs. normal traffic in the dataset.

5. Time Since Last Packet (`time_since_last`)
- **What it measures:** Delay between the current packet and the previous one.
- **Why it's included:** C2 frameworks often use timed beaconing or exhibit bursty timing patterns.

6. Delta Time Ratio (`delta_t_ratio`)
- **What it measures:** Ratio of current `time_since_last` to the previous one.
- **Why it's included:** Highlights sudden timing shifts, useful for detecting irregular beaconing or bursty traffic.

7. Rolling Mean of Time Delta (`rolling_mean_delta_t_X`)
- **What it measures:** Rolling average of inter-packet delays over X packets (X = 3, 5, 10).
- **Why it's included:** Smooths short-term fluctuations to highlight consistent timing behavior (e.g., periodic beacons).

8. Rolling Std Dev of Time Delta (`rolling_std_delta_t_X`)
- **What it measures:** Rolling standard deviation of `time_since_last` over X packets.
- **Why it's included:** Measures variability of timing. Random jitter or bursty behavior is more detectable via variance.

9. TCP Flag Indicators (`is_SYN`, `is_ACK`, `is_RST`, `is_FIN`, `is_PSH`, `is_URG`)
- **What they measure:** Presence of specific TCP flags extracted from `tcp.flags`.
- **Why they're included:** Different C2 frameworks may:
  - frequently initiate sessions (`SYN`)
  - send excessive acknowledgments (`ACK`)
  - use resets for evasion (`RST`)
  - gracefully end sessions (`FIN`)
  - push immediate data (`PSH`)
  - rarely use urgent data (`URG`, included for completeness)

---

## Usage
Run the script from the command line:
```bash
python extract_features_mixed.py <input_pcap> <output_csv>
```
- `<input_pcap>`: Path to the input PCAP file.
- `<output_csv>`: Path to save the extracted features as a CSV.
---

## Output
The output CSV will contain the following columns:

- frame.len
- ip.proto
- src_ip
- dst_ip
- c2_label
- time_since_last
- delta_t_ratio
- rolling_mean_delta_t_3 / 5 / 10
- rolling_std_delta_t_3 / 5 / 10
- is_SYN, is_ACK, is_RST, is_FIN, is_PSH, is_URG

---

## Notes
- The C2 host IP is hardcoded via `C2_HOST` in the script. Update as needed.
- This script uses `tshark` to extract fields directly from the PCAP. Make sure tshark is installed via `pip install -r requirements.txt`.
- Missing or malformed values are handled with default replacements (e.g., treating missing IPs as "UNKNOWN").


