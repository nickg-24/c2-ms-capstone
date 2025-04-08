# Dataset Composition

Targeting ~10k packets per C2 framework, each making up about 3.2% of total traffic. Overall, the dataset will be roughly 20% C2 and 80% normal traffic. Note, only IP packets were included in datasets. This means there may be slight differences in packet counts between pcaps and csvs. This is intentional.

## Mixed Traffic (`./mixed`): Normal and C2 Traffic
- `metasploit_mixed_0.csv` → Mixed metasploit traffic, sourced from `metasploit_mixed_0.pcapng`

## C2-Only Traffic (`./c2_only`): Exclusively C2 Traffic (50679 packets total)
### Metasploit (9123 packets total)
**CSV packet num matches pcapng's**
- `metasploit_0_filtered.csv` → 1603 packets Metasploit traffic, sourced from `metasploit_0_filtered.pcapng`
- `metasploit_beaconing_0.csv` → 1243 packets, ~10 minutes of beaconing with the occasional `pwd` to make sure the connection stays open. Sourced from `metasploit_beaconing_0.pcapng`
- `metasploit_beaconing_1.csv` → 780 packets, ~10 minutes of just beaconing, no other commands. Sourced from `metasploit_beaconing_1.pcapng`
- `metasploit_beaconing_2.csv` → 1420 packets, ~30 minutes of beaconing, with a `pwd` about every 5 minutes to keep the connection open. Sourced from `metasploit_beaconing_2.pcapng`
- `metasploit_tasks_0.csv`  → 4077 packets. ~22 minutes of various tasks. Collected network and system information, enumerated processes, uploaded and downloaded files, deleted a file, created and navigated directories, and executed calc.exe and notepad.exe. Sourced from `metasploit_tasks_0.pcapng`.
### Covenant (12276 packets total)
**CSV packet num matches pcapng's**
- `covenant_random_0.csv` → 1842 packets, ~20 minutes of beaconing and various commands. Getting process list, user information, shell commands, getting file system info. Source from `covenant_random_0.pcapng`
- `covenant_beaconing_0.csv` → 856 packets, ~20 minutes of beaconing, with 1 cmd execution at the beginning. Sourced from `covenant_beaconing_0.pcapng`
- `covenant_beaconing_1.csv` → 867 packets, ~13 minutes of just beaconing, with a `GetCurrentDirectory` about every 5 minutes to ensure the connection stayed open. Sourced from `covenant_beaconing_1.pcapng`
- `covenant_beaconing_2.csv` → 3547 packets, ~60 minutes of just beaconing, with a `WhoAmI` about every 5 minutes to ensure the connection stayed open. Sourced from `covenant_beaconing_2.pcapng`
- `covenant_tasks_0.csv` → 5164 packets, ~35 minutes. Ran WhoAmI, GetNetLoggedOnUser (got domain info), GetCurrentDirectory, ListDirectory, GetNetSession, CreateDirectory, ProcessList, Download file, Shell (executes shell commands), Powershell (run powershell commands), Mimikatz, ChangeDirecotry a number of times. General C2 usage. Sourced from `covenant_tasks_0.pcapng`

### Empire (10570 packets total)
**CSV packet num matches pcapng's**
- `empire_beaconing_0.csv` → 7357 packets, ~51 minutes of beaconing, with an occasional `pwd` to ensure the connection stays open. Sourced from `empire_beaconing_0.pcapng`.
- `empire_tasks_0.csv` → 3213 packets, ~20 minutes. Ran ipconfig, whoami, ls, mkdir, uploaded a file, downloaded a file, file system traversal, cat a file, created files, ps. Sourced from `empire_tasks_0.pcapng`.

### Sliver (10151 packets total)
**CSV packet num matches pcapng's**
- `sliver_beaconing_0.csv` → 4946 packets, ~10 minutes of beaconing, with an occasional `pwd` to ensure the connection stays open. Generated payload as a "session" (`SPRITUAL_ORGAN.exe`). Sourced from `sliver_beaconing_0.pcapng`.
- `sliver_beaconing_1.csv` → 2568 packets, ~2 hours of beaconing, Agent checks in around every 60 seconds. Generated payload as a "beacon" (`SKINNY_OUTCOME.exe`). Sourced from `sliver_beaconing_1.pcapng`.
- `sliver_tasks_0.csv` →  2004 packets, ~3 minutes. In session mode (`SPRITUAL_ORGAN.exe`) ran whoami, ls, mkdir, cd, pwd, cat, upload, download. Sourced from `sliver_tasks_0.pcapng`.
- `sliver_tasks_1.csv`  → 633 packets, ~12 minutes. In beacon mode (`SKINNY_OUTCOME.exe`) ran ls, mkdir, whoami, pwd, netstat, ps, memfiles, do, cd, upload, download. Sourced from `sliver_tasks_1.pcapng`.


### TODO Pupy
foo

### TODO Merlin (8559 packets total)
**CSV packet num matches pcapng's**
- `merlin_beaconing_0.csv` → 5192 packets, ~70 minutes of beaconing, with an occasional `pwd` to ensure connection stays open. Sourced from `merlin_beaconing_0.pcapng`.
- `merlin_tasks_0.csv` → 3367 packets, ~51 minutes. Ran pwd, ls, ps, upload, download, cd, rm, shell, ipconfig, netstat, printenv. Sourced from `merlin_tasks_0.pcapng`.

## Normal-Only Traffic (`./normal_only`): Exclusively Normal Traffic (249057 packets total)
- `normal_1.csv` → 249057 packets, ~20 minutes of normal traffic (google searches, youtube videos, dns lookups, visiting websites). 249057 packets, sourced from `normal_1.pcapng`


## Combined Datasets
<!-- - `combined_0.csv` → FOO Packets. Merged: `covenant_beaconing_0.csv`, `covenant_beaconing_1.csv`, `covenant_beaconing_2.csv`, `covenant_random_0.csv`, `metasploit_0_filtered.csv`, `metasploit_beaconing_0.csv`, `metasploit_beaconing_1.csv`, `metasploit_beaconing_2.csv`, `metasploit_mixed_.csv` -->

- `combined_1.csv` → 270456 Packets. Merged: `covenant_beaconing_0.csv`, `covenant_beaconing_1.csv`, `covenant_beaconing_2.csv`, `covenant_random_0.csv`, `covenant_tasks_0.csv`, `metasploit_0_filtered.csv`, `metasploit_beaconing_0.csv`, `metasploit_beaconing_1.csv`, `metasploit_beaconing_2.csv`, `metasploit_tasks_0.csv`, `normal_1.csv`

- `combined_2.csv` → 281026 Packets. Merged: `covenant_beaconing_0.csv`, `covenant_beaconing_1.csv`, `covenant_beaconing_2.csv`, `covenant_random_0.csv`, `covenant_tasks_0.csv`, `metasploit_0_filtered.csv`, `metasploit_beaconing_0.csv`, `metasploit_beaconing_1.csv`, `metasploit_beaconing_2.csv`, `metasploit_tasks_0.csv`, `normal_1.csv`, `empire_beaconing_0.csv`, `empire_tasks_0.csv`


- `combined_3.csv` → 291177 Packets. Merged: `covenant_beaconing_0.csv`, `covenant_beaconing_1.csv`, `covenant_beaconing_2.csv`, `covenant_random_0.csv`, `covenant_tasks_0.csv`, `metasploit_0_filtered.csv`, `metasploit_beaconing_0.csv`, `metasploit_beaconing_1.csv`, `metasploit_beaconing_2.csv`, `metasploit_tasks_0.csv`, `normal_1.csv`, `empire_beaconing_0.csv`, `empire_tasks_0.csv`, `sliver_beaconing_0.csv`, `sliver_beaconing_1.csv`, `sliver_tasks_0.csv`, `sliver_tasks_1.csv`

- `combined_4.csv` → 299736 Packets. Merged: `covenant_beaconing_0.csv`, `covenant_beaconing_1.csv`, `covenant_beaconing_2.csv`, `covenant_random_0.csv`, `covenant_tasks_0.csv`, `metasploit_0_filtered.csv`, `metasploit_beaconing_0.csv`, `metasploit_beaconing_1.csv`, `metasploit_beaconing_2.csv`, `metasploit_tasks_0.csv`, `normal_1.csv`, `empire_beaconing_0.csv`, `empire_tasks_0.csv`, `sliver_beaconing_0.csv`, `sliver_beaconing_1.csv`, `sliver_tasks_0.csv`, `sliver_tasks_1.csv`, `merlin_beaconing_0.csv`, `merline_tasks_0.csv`


- `foo.csv` -> the placeholder for development. 