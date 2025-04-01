# Dataset Composition

## Mixed Traffic (`./mixed`): Normal and C2 Traffic
- `metasploit_mixed_0.csv` → Mixed metasploit traffic, sourced from `metasploit_mixed_0.pcapng`

## C2-Only Traffic (`./c2_only`): Exclusively C2 Traffic
- `metasploit_0_filtered.csv` → Metasploit traffic, sourced from `metasploit_0_filtered.pcapng`
- `metasploit_beaconing_0.csv` → ~10 minutes of beaconing with the occasional `pwd` to make sure the session stays open. Sourced from `metasploit_beaconing_0.pcapng`
- `metasploit_beaconing_1.csv` → ~10 minutes of just beaconing, no other commands. Sourced from `metasploit_beaconing_1.pcapng`
- `metasploit_beaconing_2.csv` → ~30 minutes of beaconing, with a `pwd` about every 5 minutes to keep the session open. Sourced from `metasploit_beaconing_2.pcapng`
- `covenant_random_0.csv` → ~20 minutes of beaconing and various commands. Getting process list, user information, shell commands, getting file system info. Source from `covenant_random_0.pcapng`
- `covenant_beaconing_0.csv` → ~20 minutes of beaconing, with 1 cmd execution at the beginning. Sourced from `covenant_beaconing_0.pcapng`
- `covenant_beaconing_1.csv` → ~13 minutes of just beaconing, with a `GetCurrentDirectory` about every 5 minutes to ensure the session stayed open. Sourced from `covenant_beaconing_1.pcapng`
- `covenant_beaconing_2.csv` → ~60 minutes of just beaconing, with a `WhoAmI` about every 5 minutes to ensure the session stayed open. Sourced from `covenant_beaconing_2.pcapng`

## Normal-Only Traffic (`./normal_only`): Exclusively Normal Traffic
- **TODO** `normal_0.csv` → ~10 minutes of normal traffic (google searches, youtube videos, dns lookups, visiting websites). Sourced from `normal_0.csv`

## Combined Datasets
- `mixed_combined.csv` → All mixed traffic CSVs merged
- `c2only_combined.csv` → All C2-only traffic CSVs merged
- `normalonly_combined.csv` → All normal-only traffic CSVs merged.
- `full_dataset.csv` → EVERYTHING merged (mixed + C2-only + normal)

- `foo.csv` -> the placeholder for development. 