### **C2 Framework Testing Workflow**

#### **1. Initial Setup (Before Each Test)**
- Start the appropriate C2 listener.
- Start PCAP capture on the windows target:

---

#### **2. Testing Process (For Each Framework)**
1. Run the payload on the Windows target.
2. Wait **1-2 minutes** to capture beaconing traffic.
3. Execute the following commands in sequence, waiting **5-15 seconds** between each:

| **Category**       | **Action**                          | **Purpose** |
|-------------------|---------------------------------|---------------------------------|
| **Recon #1** | `whoami` or equivalent | Identifies user context |
| **Recon #2** | `hostname` or equivalent | Identifies machine name |
| **Recon #3** | `pwd` or equivalent | Confirms current directory |
| **Recon #4** | `get network info` (ipconfig, ifconfig, etc.) | Captures network configuration |
| **File System #1** | `ls` or equivalent | Lists current directory contents |
| **File System #2** | `cd <existing directory>` or equivalent | Changes to a known directory |
| **Recon #5** | `pwd` or equivalent | Verifies directory change |
| **File System #3** | `upload test.txt` or equivalent | Transfers the test file |
| **File System #4** | `ls` or equivalent | Ensures file was uploaded |
| **Command Execution** | `cmd.exe /c echo PWNED` or equivalent | Runs a test command |
| **Authentication Dumping** | `mimikatz`, `dump-creds`, or equivalent | Extracts credentials (if possible) |

4. Stop PCAP capture.

---

#### **3. Jitter/Delay Adjustments**
- If the framework supports jitter/delay, modify settings and repeat the test.
- Save each test run as a new PCAP file:
  ```
  metasploit_test1.pcap  (default settings)
  metasploit_test2.pcap  (modified jitter)
  ```

---

#### **4. Authentication Dumping**
| **Framework** | **Authentication Dumping Command** |
|--------------|-----------------------------------|
| **Metasploit** | `hashdump` |
| **Covenant** | `MimikatzLogonPasswords` |
| **Empire** | `credential`, `use module mimikatz` |
| **Sliver** | `idk yet` |
| **Pupy** | `run mimikatz` |
| **Merlin** | `Invoke-Mimikatz` module |

- Need to double check these commands

---

#### **5. Repeating the Process for Each Framework**
- Perform the full test workflow for each C2 framework:
  - **Metasploit**
  - **Covenant**
  - **Empire**
  - **Sliver**
  - **Pupy**
  - **Merlin**
- Repeat tests with jitter/delay settings if applicable.

---