# Dataset Composition

Targeting ~10k packets per C2 framework, each making up about 3.2% of total traffic. Overall, the dataset will be roughly 20% C2 and 80% normal traffic. Note, only IP packets were included in datasets. This means there may be slight differences in packet counts between pcaps and csvs. This is intentional.

## C2-Only Traffic (`./c2_only/`): Exclusively C2 Traffic (60921 packets total)
### Metasploit - `metasploit_only.csv` (9123 packets total)
- `metasploit_0_filtered.csv` → 1603 packets Metasploit traffic, sourced from `metasploit_0_filtered.pcapng`
- `metasploit_beaconing_0.csv` → 1243 packets, ~10 minutes of beaconing with the occasional `pwd` to make sure the connection stays open. Sourced from `metasploit_beaconing_0.pcapng`
- `metasploit_beaconing_1.csv` → 780 packets, ~10 minutes of just beaconing, no other commands. Sourced from `metasploit_beaconing_1.pcapng`
- `metasploit_beaconing_2.csv` → 1420 packets, ~30 minutes of beaconing, with a `pwd` about every 5 minutes to keep the connection open. Sourced from `metasploit_beaconing_2.pcapng`
- `metasploit_tasks_0.csv`  → 4077 packets. ~22 minutes of various tasks. Collected network and system information, enumerated processes, uploaded and downloaded files, deleted a file, created and navigated directories, and executed calc.exe and notepad.exe. Sourced from `metasploit_tasks_0.pcapng`.

### Covenant - `covenant_only.csv` (12276 packets total)
- `covenant_random_0.csv` → 1842 packets, ~20 minutes of beaconing and various commands. Getting process list, user information, shell commands, getting file system info. Source from `covenant_random_0.pcapng`
- `covenant_beaconing_0.csv` → 856 packets, ~20 minutes of beaconing, with 1 cmd execution at the beginning. Sourced from `covenant_beaconing_0.pcapng`
- `covenant_beaconing_1.csv` → 867 packets, ~13 minutes of just beaconing, with a `GetCurrentDirectory` about every 5 minutes to ensure the connection stayed open. Sourced from `covenant_beaconing_1.pcapng`
- `covenant_beaconing_2.csv` → 3547 packets, ~60 minutes of just beaconing, with a `WhoAmI` about every 5 minutes to ensure the connection stayed open. Sourced from `covenant_beaconing_2.pcapng`
- `covenant_tasks_0.csv` → 5164 packets, ~35 minutes. Ran WhoAmI, GetNetLoggedOnUser (got domain info), GetCurrentDirectory, ListDirectory, GetNetSession, CreateDirectory, ProcessList, Download file, Shell (executes shell commands), Powershell (run powershell commands), Mimikatz, ChangeDirecotry a number of times. General C2 usage. Sourced from `covenant_tasks_0.pcapng`

### Empire - `empire_only.csv` (10570 packets total)
- `empire_beaconing_0.csv` → 7357 packets, ~51 minutes of beaconing, with an occasional `pwd` to ensure the connection stays open. Sourced from `empire_beaconing_0.pcapng`.
- `empire_tasks_0.csv` → 3213 packets, ~20 minutes. Ran ipconfig, whoami, ls, mkdir, uploaded a file, downloaded a file, file system traversal, cat a file, created files, ps, shell commands. Sourced from `empire_tasks_0.pcapng`.

### Sliver - `sliver_only.csv` (10151 packets total)
- `sliver_beaconing_0.csv` → 4946 packets, ~10 minutes of beaconing, with an occasional `pwd` to ensure the connection stays open. Generated payload as a "session" (`SPRITUAL_ORGAN.exe`). Sourced from `sliver_beaconing_0.pcapng`.
- `sliver_beaconing_1.csv` → 2568 packets, ~2 hours of beaconing, Agent checks in around every 60 seconds. Generated payload as a "beacon" (`SKINNY_OUTCOME.exe`). Sourced from `sliver_beaconing_1.pcapng`.
- `sliver_tasks_0.csv` →  2004 packets, ~3 minutes. In session mode (`SPRITUAL_ORGAN.exe`) ran whoami, ls, mkdir, cd, pwd, cat, upload, download. Sourced from `sliver_tasks_0.pcapng`.
- `sliver_tasks_1.csv`  → 633 packets, ~12 minutes. In beacon mode (`SKINNY_OUTCOME.exe`) ran ls, mkdir, whoami, pwd, netstat, ps, memfiles, cd, upload, download. Sourced from `sliver_tasks_1.pcapng`.


### Merlin - `merlin_only.csv` (8559 packets total)
- `merlin_beaconing_0.csv` → 5192 packets, ~70 minutes of beaconing, with an occasional `pwd` to ensure connection stays open. Sourced from `merlin_beaconing_0.pcapng`.
- `merlin_tasks_0.csv` → 3367 packets, ~51 minutes. Ran pwd, ls, ps, upload, download, cd, rm, shell, ipconfig, netstat, printenv. Sourced from `merlin_tasks_0.pcapng`.


### Posh - `posh_only.csv` (10242 Packets total)
- `posh_beaconing_0.csv` → 3073 packets, ~20 minutes of beaconing, with an occasional `whoami` to ensure connection stays open. Sourced from `posh_beaconing_0.pcapng`.
- `posh_tasks_0.csv` → 3326 packets, ~13 minutes. Ran ls, pwd, mkdir, cd, whoami, ps, ipconfig, download, various shell commands, etc. Sourced from `posh_tasks_0.csv`.
- `posh_tasks_1.csv` → 3843 packets, ~10 minutes. Ran ipconfig, ls, ps, type, netstat, ran executables, etc. Sourced from `posh_tasks_1.csv`.


## Normal-Only Traffic (`./normal_only/`): Exclusively Normal Traffic (249057 packets total)
- `normal_1.csv` → 249057 packets, ~20 minutes of normal traffic (google searches, youtube videos, dns lookups, visiting websites). 249057 packets, sourced from `normal_1.pcapng`


## Mixed Traffic (`./mixed/`): Normal and C2 Traffic
- `metasploit_mixed_0.csv` → Mixed metasploit traffic, sourced from `metasploit_mixed_0.pcapng`

- `metasploit_mixed_1.csv` → 15216 packets, ~5 minutes. ~10% c2 packets. Web browsing/Windows 10 idling on target machine and c2 traffic. Ran ls, pwd, ipconfig, netstat, ps, whoami, run exe, etc. Sourced from `metasploit_mixed_1.pcapng`.

- `covenant_mixed_0.csv` → 12084 packets, ~9 minutes. ~10% c2 packets. Web browsing/Windows 10 idling on target machine and c2 traffic. Ran ls, ps, pwd, whoami, run exe, cd, upload file, download file, etc. Sourced from `covenant_mixed_0.pcapng`.

- `empire_mixed_0.csv` → 13973 packets, ~10 minutes. ~9% c2 packets. Web browsing/Windows 10 idling on target machine and c2 traffic. Ran ls, pwd, whoami, ps, run exe, netstat, ipconfig, upload file, download file. Sourced from `empire_mixed_0.pcapng`.

- `merlin_mixed_0.csv` → 52750 packets, ~13 minutes. ~2% c2 packets. Web browsing/Windows 10 idling on target machine and c2 traffic. Ran info, ps, netstat, pwd, ls, run exe, etc. Sourced from `merlin_mixed_0.pcapng`.

- `merlin_mixed_1.csv` → 6843 packets, ~5 minutes. ~6% c2 packets. Web browsing/Windows 10 idling on target machine and c2 traffic. Ran info, ps, netstat, pwd, ls, run exe, etc. Sourced from `merlin_mixed_1.pcapng`.

- `posh_mixed_0.csv` → 10724 packets, ~3 minutes. ~11% c2 packets. Web browsing/Windows 10 idling on target machine and c2 traffic. Ran ls, whoami, pwd, ps, shell commands, mkdir, download files, etc. Sourced from `posh_mixed_0.pcapng`.


- `sliver_mixed_0.csv` → 15979 packets, ~4 minutes. ~11% c2 packets. Web browsing/Windows 10 idling on target machine and c2 traffic. Ran ls, whoami, pwd, execute shell, netstat, ipconfig, ps, etc. in session mode. Sourced from `sliver_mixed_0.pcapng`.

- `sliver_mixed_1.csv` → 4034 packets, ~8 minutes. ~8% c2 packets. Web browsing/Windows 10 idling on target machine and c2 traffic. Ran ls, whoami, pwd, execute shell, netstat, ipconfig, ps, etc. in beacon mode. Sourced from `sliver_mixed_1.pcapng`

## Combined Datasets
- `combined_1.csv` → 270456 Packets. Merged: `covenant_beaconing_0.csv`, `covenant_beaconing_1.csv`, `covenant_beaconing_2.csv`, `covenant_random_0.csv`, `covenant_tasks_0.csv`, `metasploit_0_filtered.csv`, `metasploit_beaconing_0.csv`, `metasploit_beaconing_1.csv`, `metasploit_beaconing_2.csv`, `metasploit_tasks_0.csv`, `normal_1.csv`

- `combined_2.csv` → 281026 Packets. Merged: `covenant_beaconing_0.csv`, `covenant_beaconing_1.csv`, `covenant_beaconing_2.csv`, `covenant_random_0.csv`, `covenant_tasks_0.csv`, `metasploit_0_filtered.csv`, `metasploit_beaconing_0.csv`, `metasploit_beaconing_1.csv`, `metasploit_beaconing_2.csv`, `metasploit_tasks_0.csv`, `normal_1.csv`, `empire_beaconing_0.csv`, `empire_tasks_0.csv`


- `combined_3.csv` → 291177 Packets. Merged: `covenant_beaconing_0.csv`, `covenant_beaconing_1.csv`, `covenant_beaconing_2.csv`, `covenant_random_0.csv`, `covenant_tasks_0.csv`, `metasploit_0_filtered.csv`, `metasploit_beaconing_0.csv`, `metasploit_beaconing_1.csv`, `metasploit_beaconing_2.csv`, `metasploit_tasks_0.csv`, `normal_1.csv`, `empire_beaconing_0.csv`, `empire_tasks_0.csv`, `sliver_beaconing_0.csv`, `sliver_beaconing_1.csv`, `sliver_tasks_0.csv`, `sliver_tasks_1.csv`

- `combined_4.csv` → 299736 Packets. Merged: `covenant_beaconing_0.csv`, `covenant_beaconing_1.csv`, `covenant_beaconing_2.csv`, `covenant_random_0.csv`, `covenant_tasks_0.csv`, `metasploit_0_filtered.csv`, `metasploit_beaconing_0.csv`, `metasploit_beaconing_1.csv`, `metasploit_beaconing_2.csv`, `metasploit_tasks_0.csv`, `normal_1.csv`, `empire_beaconing_0.csv`, `empire_tasks_0.csv`, `sliver_beaconing_0.csv`, `sliver_beaconing_1.csv`, `sliver_tasks_0.csv`, `sliver_tasks_1.csv`, `merlin_beaconing_0.csv`, `merlin_tasks_0.csv`

- `combined_5.csv` → 309978 Packets. Merged: `covenant_beaconing_0.csv`, `covenant_beaconing_1.csv`, `covenant_beaconing_2.csv`, `covenant_random_0.csv`, `covenant_tasks_0.csv`, `metasploit_0_filtered.csv`, `metasploit_beaconing_0.csv`, `metasploit_beaconing_1.csv`, `metasploit_beaconing_2.csv`, `metasploit_tasks_0.csv`, `normal_1.csv`, `empire_beaconing_0.csv`, `empire_tasks_0.csv`, `sliver_beaconing_0.csv`, `sliver_beaconing_1.csv`, `sliver_tasks_0.csv`, `sliver_tasks_1.csv`, `merlin_beaconing_0.csv`, `merlin_tasks_0.csv`, `posh_beaconing_0.csv`, `posh_tasks_0.csv`, `posh_tasks_1.csv`

- `combined_6.csv` → 361975 Packets. Merged: `covenant_beaconing_0.csv`, `covenant_beaconing_1.csv`, `covenant_beaconing_2.csv`, `covenant_random_0.csv`, `covenant_tasks_0.csv`, `metasploit_0_filtered.csv`, `metasploit_beaconing_0.csv`, `metasploit_beaconing_1.csv`, `metasploit_beaconing_2.csv`, `metasploit_tasks_0.csv`, `normal_1.csv`, `empire_beaconing_0.csv`, `empire_tasks_0.csv`, `sliver_beaconing_0.csv`, `sliver_beaconing_1.csv`, `sliver_tasks_0.csv`, `sliver_tasks_1.csv`, `merlin_beaconing_0.csv`, `merlin_tasks_0.csv`, `posh_beaconing_0.csv`, `posh_tasks_0.csv`, `posh_tasks_1.csv`, `metasploit_mixed_1.csv`, `covenant_mixed_0.csv`, `empire_mixed_0.csv`, `posh_mixed_0.csv`

