# Dataset Composition

## Mixed Traffic (`./mixed`): Normal and C2 Traffic
- `metasploit_mixed_0.csv` → Mixed metasploit traffic, sourced from `metasploit_mixed_0.pcapng`

## C2-Only Traffic (`./c2_only`): Exclusively C2 Traffic
- `metasploit_0_filtered.csv` → Metasploit traffic, sourced from `metasploit_0_filtered.pcapng`
- `metasploit_beaconing_0.csv` → 10 minutes of beaconing with the occasional `pwd` to make sure the session stays open. Sourced from `metasploit_beaconing_0.pcapng`
- `metasploit_beaconing_1.csv` → 10 minutes of just beaconing, no other commands. Sourced from `metasploit_beaconing_1.pcapng`
- `metasploit_beaconing_2.csv` → X minutes of beaconing, with a `pwd` about every 5 minutes to keep the session open. Sourced from `metasploit_beaconing_2.pcapng`

## Combined Datasets
- `mixed_combined.csv` → All mixed traffic CSVs merged
- `c2only_combined.csv` → All C2-only traffic CSVs merged
- `full_dataset.csv` → EVERYTHING merged (mixed + C2-only + normal)

- `foo.csv` -> the placeholder for development. 