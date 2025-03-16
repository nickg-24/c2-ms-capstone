# Using:

6 C2 frameworks will initially be used to generate data for this project. More frameworks will be used time-permitting.

## Selected Protocol: HTTPS

## Overall Considerations:

- Will running the tests for each framework affect the results for behavior-based solutions?  
  - Do I need to revert to a consistent state before evaluating each framework?  
  - Do I need to introduce proxies from the attacker machine to deal with this? (hopefully not).  
    - No. Feature extraction will not rely on explicit ip labeling. IP address information will be abstracted into a HOMENET 0/1 value to signify if the traffic is originating from the same network or not. This was introduced to “even the playing field” in a way between the ML model and Suricata’s HOMENET property.  
- For various reasons, the test protocols have been reduced to just HTTPS.  
  - DNS tunneling detection is an interesting area to look at but given the complexity of separating malicious from normal traffic it was left out. This would be good to mention in the future works.

## [1\. Metasploit Framework:](https://github.com/rapid7/metasploit-framework)

- Beginner friendly  
- Lots of payloads  
- Comes with kali

**Requirements/TODOs:**

- [ ] Set up kali (comes pre-installed)  
- [ ] windows victim machine  
- [ ] **Identify** attacks to run  
      - Recon (sysinfo, ipconfig, getuid)  
      - File system access (ls, rm, upload, download, cd)  
      - Authentication data collection (hashdump)  
      - Command and Code Execution (shell)  
- [ ] **Use** exploit/multi/handler  
- [ ] **Test** reverse\_https (default and with jitter)  
- [ ] **Capture** baseline beaconing traffic for each protocol  
- [ ] **Capture** attack traffic for each protocol

## [2\. Covenant:](https://github.com/cobbr/Covenant)

- Web interface  
- Already dockerized  
- Thorough documentation  
- Http, optional ssl  
- C2Bridge listeners are available for expanded protocol support, however that increases development and setup complexity as custom scripts are needed to make that work.  
- Targets windows systems as it uses C\# and windows .NET runtime  
- Listener Profiles:  
  - Can customize the communication between Grunts and the server to evade detection.  
  - Can modify: HTTP Headers (mimic legitimate applications like Chrome, APIs) and URIs/Parameters (to make traffic appear as normal web browsing)  
  - Will need to develop listener profiles to mimic standard traffic

**Requirements/TODOs:**

- [ ] Setup dockerized server  
      - Great [link](https://www.hackingarticles.in/covenant-for-pentester-basics/) explaining everything from installation to exploitation  
- [ ] Windows victim machine (grunt)  
- [ ] Develop listener profiles to mimic standard traffic  
- [ ] Generate trusted cert for ssl traffic (if there is time)  
- [ ] **Identify Tasks to Test**  
      - Recon (WhoAmI, GetCurrentDirectory, Process-List, GetNetStat, GetSystemInfo)  
      - File system access (ChangeDirectory, ListFiles, Upload, Download)  
      - Authentication Data collection (MimikatzLogonPasswords)  
      - Command and Code Execution (ExecuteAssembly, Invoke-Powershell)  
- [ ] **Test** HTTPS traffic  
- [ ] **Test** different delays and jitter percentages  
- [ ] **Capture** baseline beaconing traffic for each protocol  
- [ ] **Capture** attack traffic for each protocol

## [3\. Empire:](https://github.com/BC-SECURITY/Empire)

- Support for GUI (starkiller) and CLI  
- HTTP/S, Malleable HTTP, OneDrive, Dropbox, PHP listeners  
- powershell , c\#, & python support  
- Dockerized  
- Should be able to instal via apt in kali as well  
- Malleable HTTP was considered however due to its added complexity, I plan to stick with the standard HTTP/HTTPS listeners for simplicity and baseline testing. There are a myriad of directions this project could go focusing just on the customization available with malleable http. It has real potential to divert focus from the primary goals of this project, especially if we go as in-depth for similar features of other frameworks.  
- Empire [network analysis](https://www.keysight.com/blogs/en/tech/nwvs/2021/06/16/empire-c2-networking-into-the-dark-side)

**Requirements/TODOs:**

- [ ] Setup dockerized server  
- [ ] **Determine** agent types  
      - Windows victim machine (guide [here](https://www.stationx.net/how-to-use-powershell-empire/))  
- [ ] **Identify** modules/tasks to test  
      - Recon (get system info, get network info, get process info)  
      - File system access (change dir, list files, upload file, download file)  
      - Authentication data collection (tasks to extract or collect authentication-related data. Ex: dumping password hashes, extracting ssh keys and env vars)  
      - Command and Code Execution (running scripts, console commands, etc.)  
- [ ] **Test** HTTPS traffic (Empire will auto-generate a self-signed cert for HTTPS, check documentation). **Transfer** the stager script to each of the victim machines and run them (victims will reach out to listener, capture this traffic). This will set up the agents.   
- [ ] **Test** different delay and jitter values  
- [ ] **Capture** baseline beaconing traffic for each protocol  
- [ ] **Capture** attack traffic for each protocol

## [4\. Sliver C2:](https://github.com/BishopFox/sliver?tab=readme-ov-file)

- Simple one liner to install on kali  
- HTTP(S), mTLS, and DNS c2s  
- Comes with a dockerfile  
- **Maybe** test mTLS listener if there is time. Not as common of a protocol and requires additional overhead for “normal” traffic.  
- Has GREAT [docs](https://sliver.sh/)

**Requirements/TODOs:**

- [ ] Set up dockerized c2 server  
- [ ] Set up windows victim machine.  
- [ ] **Identify** modules/tasks to test  
      - Recon (get system info, get network info, get process info)  
      - File system access (change dir, list files, upload file, download file)  
      - Authentication data collection (tasks to extract or collect authentication-related data. Ex: dumping password hashes, extracting ssh keys and env vars)  
      - Command and Code Execution (running scripts, console commands, etc.)  
- [ ] **Test** HTTPS listener using sliver generated cert  
- [ ] **Test** different delay and jitter values  
- [ ] **Capture** beaconing traffic (default behavior) for baseline testing; assign commands or execute tasks on implants later for additional traffic patterns.

## [5\. Pupy:](https://github.com/n1nj4sec/pupy)

- Pre-dockerized  
- Https, Obfs3, focuses on minimizing its detection footprint using:  
  - in-memory execution to avoid leaving files on disk.  
  - Polymorphic payload generation to evade signature-based detection.  
- Docs are alright  
- [Guide](https://www.hackingarticles.in/command-control-tool-pupy/) includes windows and linux exploitation

**Requirements/TODOs:**

- [ ] Set up docker container  
- [ ] Windows victim machine  
- [ ] **Identify** modules/tasks to test  
      - Recon (get system info, get network info, get process info)  
      - File system access (change dir, list files, upload file, download file)  
      - Authentication data collection (tasks to extract or collect authentication-related data. Ex: dumping password hashes, extracting ssh keys and env vars)  
      - Command and Code Execution (running scripts, console commands, etc.)  
- [ ] **Test** http \[http+rsa\] transport (basic HTTP stack with RSA)  
- [ ] **Capture** beaconing traffic (default behavior) for baseline testing; assign commands or execute tasks on implants later for additional traffic patterns.

## [6\. Merlin:](https://github.com/Ne0nd0g/merlin)

- Runs on Go but comes pre-dockerized  
- Designed to evade intrusion detection systems (IDS) and intrusion prevention systems (IPS) by mimicking normal, encrypted traffic.

**Requirements/TODOs:**

- [ ] Set up docker container  
- [ ] Copy windows binaries from docker container to host system. Then distribute to victim machines  
- [ ] **Identify** modules/tasks to test  
      - Recon (get system info, get network info, get process info)  
      - File system access (change dir, list files, upload file, download file)  
      - Authentication data collection (tasks to extract or collect authentication-related data. Ex: dumping password hashes, extracting ssh keys and env vars)  
      - Command and Code Execution (running scripts, console commands, etc.)  
- [ ] **Test** HTTP/2 with merlin generated cert  
- [ ] **Test** different delay and jitter values (double check this is a feature)  
- [ ] **Capture** beaconing traffic (default behavior) for baseline testing; assign commands or execute tasks on implants later for additional traffic patterns.