# Dataset Composition

Targeting ~10k packets per C2 framework, each making up about 3.2% of total traffic. Overall, the dataset will be roughly 20% C2 and 80% normal traffic.

## Mixed Traffic (`./mixed`): Normal and C2 Traffic
- `metasploit_mixed_0.csv` → Mixed metasploit traffic, sourced from `metasploit_mixed_0.pcapng`

## C2-Only Traffic (`./c2_only`): Exclusively C2 Traffic (10035 packets total)
### Metasploit (9129 packets total)
- `metasploit_0_filtered.csv` → 1605 packets Metasploit traffic, sourced from `metasploit_0_filtered.pcapng`
- `metasploit_beaconing_0.csv` → 1245 packets, ~10 minutes of beaconing with the occasional `pwd` to make sure the session stays open. Sourced from `metasploit_beaconing_0.pcapng`
- `metasploit_beaconing_1.csv` → 782 packets, ~10 minutes of just beaconing, no other commands. Sourced from `metasploit_beaconing_1.pcapng`
- `metasploit_beaconing_2.csv` → 1421 packets, ~30 minutes of beaconing, with a `pwd` about every 5 minutes to keep the session open. Sourced from `metasploit_beaconing_2.pcapng`
- `metasploit_tasks_0.csv`  → 4077 packets. ~22 minutes of various tasks. Collected network and system information, enumerated processes, uploaded and downloaded files, deleted a file, created and navigated directories, and executed calc.exe and notepad.exe. Sourced from `metasploit_tasks_0.pcapng`.
### Covenant (10147 packets total)
- `covenant_random_0.csv` → 1844 packets, ~20 minutes of beaconing and various commands. Getting process list, user information, shell commands, getting file system info. Source from `covenant_random_0.pcapng`
- `covenant_beaconing_0.csv` → 857 packets, ~20 minutes of beaconing, with 1 cmd execution at the beginning. Sourced from `covenant_beaconing_0.pcapng`
- `covenant_beaconing_1.csv` → 860 packets, ~13 minutes of just beaconing, with a `GetCurrentDirectory` about every 5 minutes to ensure the session stayed open. Sourced from `covenant_beaconing_1.pcapng`
- `covenant_beaconing_2.csv` → 1422 packets, ~60 minutes of just beaconing, with a `WhoAmI` about every 5 minutes to ensure the session stayed open. Sourced from `covenant_beaconing_2.pcapng`
- `covenant_tasks_0.csv` → 5164 packets, ~35 minutes. Ran WhoAmI, GetNetLoggedOnUser (got domain info), GetCurrentDirectory, ListDirectory, GetNetSession, CreateDirectory, ProcessList, Download file, Shell (executes shell commands), Powershell (run powershell commands), Mimikatz, ChangeDirecotry a number of times. General C2 usage. Sourced from `covenant_tasks_0.pcapng`

### TODO Empire
foo

### TODO Sliver
foo

### TODO Pupy
foo

### TODO Merlin
foo

## Normal-Only Traffic (`./normal_only`): Exclusively Normal Traffic (249059 packets total)
- `normal_1.csv` → 249059 packets, ~20 minutes of normal traffic (google searches, youtube videos, dns lookups, visiting websites). 249057 packets, sourced from `normal_1.pcapng`

## Combined Datasets
<!-- - `mixed_combined.csv` → All mixed traffic CSVs merged
- `c2only_combined.csv` → All C2-only traffic CSVs merged
- `normalonly_combined.csv` → All normal-only traffic CSVs merged. -->
<!-- - `full_dataset.csv` → EVERYTHING merged (mixed + C2-only + normal) -->
- `combined_0.csv` → 148697 Packets. Merged: `covenant_beaconing_0.csv`, `covenant_beaconing_1.csv`, `covenant_beaconing_2.csv`, `covenant_random_0.csv`, `metasploit_0_filtered.csv`, `metasploit_beaconing_0.csv`, `metasploit_beaconing_1.csv`, `metasploit_beaconing_2.csv`, `metasploit_mixed_.csv`

- `combined_1.csv` → 259375 Packets. Merged: `covenant_beaconing_0.csv`, `covenant_beaconing_1.csv`, `covenant_beaconing_2.csv`, `covenant_random_0.csv`, `metasploit_0_filtered.csv`, `metasploit_beaconing_0.csv`, `metasploit_beaconing_1.csv`, `metasploit_beaconing_2.csv`, `normal_1.csv`

- `combined_2.csv` → 268616 Packets. Merged: `covenant_beaconing_0.csv`, `covenant_beaconing_1.csv`, `covenant_beaconing_2.csv`, `covenant_random_0.csv`, `metasploit_0_filtered.csv`, `metasploit_beaconing_0.csv`, `metasploit_beaconing_1.csv`, `metasploit_beaconing_2.csv`, `normal_1.csv`, `covenant_tasks_0.csv`, `metasploit_tasks_0.csv`

- `foo.csv` -> the placeholder for development. 