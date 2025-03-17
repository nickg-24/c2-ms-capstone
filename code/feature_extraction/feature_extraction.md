### **Feature Overview and Justification**

This section provides a breakdown of each feature used in the dataset, explaining what it measures, how it is calculated (if applicable), and why it was selected for this project.
The current iteration of selected features come from **`extract_features_mixed_0.py`**

---

### **1. Frame Length (`frame.len`)**
- **What it measures:** The total size of the packet in bytes.
- **Calculation:** Directly extracted from packet metadata using `tshark`.
- **Why it was selected:** 
  - Different protocols and frameworks may use characteristic packet sizes.
  - Some C2 frameworks might send smaller, more uniform packets to avoid detection.
  - Others might pad traffic to match legitimate sizes, which could still be an identifiable pattern.

---

### **2. IP Protocol (`ip.proto`)**
- **What it measures:** The protocol number used by the IP packet (e.g., TCP = 6, UDP = 17).
- **Calculation:** Extracted from packet headers via `tshark`.
- **Why it was selected:** 
  - All C2 frameworks in this study use HTTPS (which operates over TCP, `ip.proto=6`).
  - If anomalies occur (e.g., C2 using UDP instead), this could be useful.
  - May help identify unexpected C2 behavior in encrypted protocols.

---

### **3. Time Since Last Packet (`time_since_last`)**
- **What it measures:** The time (in seconds) since the previous packet in the dataset.
- **Calculation:** Computed using the difference between consecutive `frame.time_relative` values.
- **Why it was selected:** 
  - C2 traffic often exhibits different timing patterns than normal web traffic.
  - Normal traffic may be more continuous, whereas C2 may have bursts of activity or timed beacons.

---

### **4. Delta Time Ratio (`delta_t_ratio`)**
- **What it measures:** The ratio of the current packet’s interarrival time to the previous packet’s interarrival time.
- **Calculation:** 
  - `delta_t_ratio` = `time_since_last(n)` / `time_since_last(n-1)`
  - First packet is set to 1 to avoid division errors.
- **Why it was selected:** 
  - Helps capture sudden shifts in traffic patterns, which might indicate the presence of periodic C2 activity.
  - Useful for detecting structured timing behaviors in command execution.

---

### **5. Rolling Mean of Time Delta (`rolling_mean_delta_t_X`)**
- **What it measures:** The average of `time_since_last` over a rolling window of X packets.
- **Calculation:** 
  - `rolling_mean_delta_t_X` = `mean(time_since_last / X previous packets)`
  - Computed for window sizes of **3, 5, and 10** packets.
- **Why it was selected:** 
  - Smooths out individual packet variations to detect broader timing trends.
  - Helps recognize whether C2 traffic follows periodic beaconing behavior.

---

### **6. Rolling Standard Deviation of Time Delta (`rolling_std_delta_t_X`)**
- **What it measures:** The variability of `time_since_last` over a rolling window of X packets.
- **Calculation:** 
  - `rolling_std_delta_t_X` = `std(time_since_last / X previous packets)`
  - Computed for window sizes of **3, 5, and 10** packets.
- **Why it was selected:** 
  - Detects fluctuations in timing, which could indicate C2 frameworks with randomized beaconing.
  - High standard deviation could mean bursty C2 traffic, while low values might indicate constant beaconing.

---

### **7. TCP Flag Indicators (`is_SYN`, `is_ACK`, `is_RST`, `is_FIN`, `is_PSH`, `is_URG`)**
Each of these flags represents a specific TCP operation. They are extracted from the `tcp.flags` field and converted into binary features (0 = flag not set, 1 = flag set).

#### **7.1. `is_SYN` (SYN Flag)**
- **What it measures:** Whether a packet is attempting to initiate a TCP connection.
- **Why it was selected:** 
  - C2 frameworks may initiate new connections more frequently than normal web traffic.
  - Might be useful for detecting whether a framework repeatedly creates new sessions instead of reusing a persistent connection.

#### **7.2. `is_ACK` (ACK Flag)**
- **What it measures:** Whether a packet is acknowledging receipt of data.
- **Why it was selected:** 
  - C2 frameworks might send excessive acknowledgments to maintain control channels.
  - If ACKs are unusually frequent in a session, it could indicate persistent C2 activity.

#### **7.3. `is_RST` (RST Flag)**
- **What it measures:** Whether a packet is terminating a TCP session abruptly.
- **Why it was selected:** 
  - C2 frameworks using evasive techniques might intentionally send resets to avoid detection.
  - Anomalous resets during C2 activity might be distinguishable.

#### **7.4. `is_FIN` (FIN Flag)**
- **What it measures:** Whether a packet is requesting a graceful termination of a TCP session.
- **Why it was selected:** 
  - Some C2 frameworks might establish short-lived sessions and cleanly terminate them after command execution.
  - Could help differentiate structured C2 shutdown behavior from typical web browsing.

#### **7.5. `is_PSH` (PSH Flag)**
- **What it measures:** Whether a packet requests immediate data delivery to the application layer.
- **Why it was selected:** 
  - C2 frameworks may use this flag when sending commands in real time.
  - Observing C2 vs. normal traffic behavior for PSH patterns could be useful.

#### **7.6. `is_URG` (URG Flag)**
- **What it measures:** Whether a packet contains urgent data that should be prioritized.
- **Why it was selected:** 
  - Included to check whether any C2 framework makes use of it.
  - If it turns out to be completely unused, it can be dropped later.

---

### **Final Feature Set**
| Feature | What it Measures | Why it’s Included |
|---------|-----------------|------------------|
| `frame.len` | Packet size in bytes | Identifies possible C2 size patterns |
| `ip.proto` | Protocol number (TCP/UDP) | Helps confirm C2 protocols (e.g., HTTPS) |
| `time_since_last` | Time between packets | Detects C2 timing patterns |
| `delta_t_ratio` | Ratio of consecutive inter-packet delays | Identifies structured timing behavior |
| `rolling_mean_delta_t_3`, `rolling_mean_delta_t_5`, `rolling_mean_delta_t_10` | Smoothed time deltas | Captures beaconing periodicity |
| `rolling_std_delta_t_3`, `rolling_std_delta_t_5`, `rolling_std_delta_t_10` | Variability in time deltas | Detects bursty vs. stable C2 traffic |
| `is_SYN` | TCP connection initiation | Detects frequent session creation |
| `is_ACK` | Acknowledgment flag | Identifies excessive ACKs in C2 |
| `is_RST` | Abrupt connection termination | Helps detect evasive techniques |
| `is_FIN` | Graceful session closure | May reveal structured session handling |
| `is_PSH` | Immediate data push | Could indicate real-time C2 commands |
| `is_URG` | Urgent flag | Included for completeness, may be dropped later |

---

### **Summary**
- These features were selected based on expected behaviors of C2 frameworks.
- Some features focus on **timing anomalies** (e.g., `time_since_last`, `rolling_mean_delta_t_X`).
- Others capture **packet-level traits** (e.g., `frame.len`, `ip.proto`).
- TCP flag features were kept since different C2 frameworks may interact with them in unexpected ways.
