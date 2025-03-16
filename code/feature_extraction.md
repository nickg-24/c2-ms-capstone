### **Planned Features for Packet-Based AI Detection of C2 Channels**

This section outlines the planned feature set for detecting **Command-and-Control (C2) traffic over HTTPS** using a **packet-based machine learning model**. Initially, a flow-based approach was considered, but it became apparent that C2 traffic, including both beaconing and task execution, was contained within a single long-lived TLS session. This prevented the model from capturing meaningful distinctions between different stages of C2 activity, limiting its ability to differentiate between beaconing, command execution, and normal web browsing. By shifting to a packet-based approach, the model can analyze individual packet behaviors within these persistent sessions, allowing for a more detailed characterization of timing, packet size distributions, and session behaviors. The features selected focus on **packet behavior rather than environment-specific identifiers** (e.g., raw IP addresses, TLS certificate details) to ensure generalization across different C2 frameworks without overfitting.

---

## **1. Inter-Packet Timing**
### **What It Is**
- Measures **time gaps between consecutive packets** within a single TLS session.
- Detects **beaconing patterns** and **burst activity from attack commands**.

### **Why It’s Useful**
- **C2 beaconing traffic is periodic**, with packets appearing at regular intervals (e.g., every 30 seconds).
- **Attack commands create short bursts of activity** following beaconing, resulting in sudden shifts in timing.
- **Normal HTTPS traffic has more variable inter-packet timing** due to user behavior and natural request-response patterns.

### **How to Avoid Overfitting**
- **Normalize time differences** instead of using absolute timestamps, which can be environment-specific.
- **Cluster timing patterns** to detect regular intervals rather than relying on exact values.

**Example Extraction Command (Tshark)**
```bash
tshark -r traffic.pcapng -T fields -e frame.time_relative
```
**Example Output (Time Gaps Between Packets)**
```
0.200
30.000  # Beacon
0.350
30.001  # Beacon
1.000    # Attack command
```

---

## **2. Packet Size Distribution**
### **What It Is**
- Measures **the variation in packet sizes** within a session.
- Helps distinguish **small beacon packets** from **larger attack command packets**.

### **Why It’s Useful**
- **Beaconing packets are small and consistent** (e.g., 50-300 bytes).
- **Attack commands generate bursts of larger packets** (e.g., 500-5000 bytes).
- **Normal HTTPS traffic has highly variable packet sizes**, as different web applications load content dynamically.

### **How to Avoid Overfitting**
- **Use distributions (percentiles, histograms) instead of raw values**, which can vary across different C2 frameworks.
- **Avoid setting static thresholds** for what constitutes "small" or "large" packets, as these values may shift across tools.

**Example Extraction Command (Tshark)**
```bash
tshark -r traffic.pcapng -T fields -e frame.len
```
**Example Output (Packet Sizes in Bytes)**
```
80
120
80
80
1500  # Attack command
```

---

## **3. TCP Session Termination Behavior**
### **What It Is**
- Analyzes how **TCP sessions are closed** (graceful `FIN` vs. abrupt `RST`).
- Detects C2 frameworks that use **forced session resets** to evade detection.

### **Why It’s Useful**
- **Most normal HTTPS sessions end with `FIN` handshakes**, signaling proper session termination.
- **C2 sessions often terminate with `RST` instead of `FIN`** to avoid logging artifacts that may trigger security monitoring systems.

### **How to Avoid Overfitting**
- **Use the ratio of RST terminations to total sessions**, rather than absolute RST counts.
- **Normalize across different environments**, as some legitimate traffic may also experience RST terminations due to network conditions.

**Example Extraction Command (Tshark)**
```bash
tshark -r traffic.pcapng -T fields -e tcp.flags | sort | uniq -c
```
**Example Output**
```
300 SYN-ACK  # Normal
50 RST       # Suspicious (C2 evasion)
```

---

## **4. TLS Session Behavior**
### **What It Is**
- Measures how **TLS sessions are established and reused** within HTTPS-based C2 communications.
- Detects **long-lived encrypted tunnels**, which are uncommon in normal HTTPS traffic.

### **Why It’s Useful**
- **Legitimate web browsing frequently negotiates new TLS sessions** when users open new tabs, load new pages, or switch between services.
- **C2 traffic often reuses the same TLS session for multiple commands**, minimizing handshake activity to blend in.
- **Avoids relying on self-signed certificate detection**, as attackers can obtain valid certificates.

### **How to Avoid Overfitting**
- **Measure TLS handshake frequency and session reuse**, rather than tracking specific certificate properties.
- **Ignore self-signed vs. valid certificate details**, focusing on behavioral characteristics instead.

**Example Extraction Command (Tshark)**
```bash
tshark -r traffic.pcapng -T fields -e tls.handshake.type
```
**Example Output**
```
ClientHello
ServerHello
ChangeCipherSpec
(ClientHello appears again → New session)
```

---

## **5. Source/Destination Classification (Internal vs. External Traffic)**
### **What It Is**
- Classifies whether a packet’s source/destination is within **the home network** or **external**.
- Identifies **C2 reverse shells (external → internal connections).**

### **Why It’s Useful**
- **Most internal network traffic is benign (HOMENET ↔ HOMENET).**
- **C2 traffic often involves an external IP (HOMENET ↔ INTERNET).**
- **Reverse shells create inbound connections from an external IP (INTERNET → HOMENET).**

### **How to Avoid Overfitting**
- **Replace raw IP addresses with a binary classification (`0` for internal, `1` for external).**
- **Focus on behavioral patterns (e.g., internal machine initiating outbound communication vs. external server initiating contact).**

**Example Extraction Command (Tshark + AWK)**
```bash
tshark -r traffic.pcapng -T fields -e ip.src -e ip.dst | awk '
{
  src_home = ($1 ~ /^192\.168\./) ? "0" : "1";
  dst_home = ($2 ~ /^192\.168\./) ? "0" : "1";
  print src_home, dst_home;
}'
```
**Example Output**
```
0 0  # Internal LAN communication
0 1  # Outbound traffic to external IP
1 0  # Incoming external traffic (reverse shell)
```

---

## **6. TCP Flag Ratios**
### **What It Is**
- Tracks **ratios of key TCP flags** (`SYN`, `ACK`, `FIN`, `RST`).
- Identifies **anomalous TCP behavior** in C2 sessions.

### **Why It’s Useful**
- **Normal TCP sessions** follow predictable sequences (`SYN → SYN-ACK → FIN`).
- **C2 sessions may exhibit repeated SYNs, missing FINs, or excessive RSTs.**

### **How to Avoid Overfitting**
- **Use ratios of `RST` to `FIN`, `SYN` to `ACK`, etc., instead of absolute counts.**
- **Normalize based on overall session behavior.**

**Example Extraction Command (Tshark)**
```bash
tshark -r traffic.pcapng -T fields -e tcp.flags | sort | uniq -c
```
**Example Output**
```
SYN-ACK: 300  # Normal
RST: 20       # Suspicious (C2 evasion)
```

---

### **Final Feature Selection**
| **Feature** | **Why It’s Useful?** | **How to Avoid Overfitting?** |
|------------|----------------------|-------------------------------|
| **Inter-Packet Timing** | Detects beaconing vs. attack bursts | Normalize time gaps |
| **Packet Size Distribution** | Separates beaconing from attack execution | Use distributions, not static values |
| **HOMENET vs. INTERNET** | Distinguishes internal vs. external traffic | Use `0/1`, not raw IPs |
| **TCP Flags Ratios** | Detects abnormal connection behavior | Track ratios, not absolute counts |
| **Packet Length Variability** | Differentiates beaconing vs. attack traffic | Use statistical distributions |

This feature set is designed to capture key **behavioral characteristics of C2 frameworks** while avoiding overfitting to environment-specific data.