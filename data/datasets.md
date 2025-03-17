# Dataset Composition

## Mixed Traffic (`./mixed`): Normal and C2 Traffic
- `metasploit_mixed_0.csv` → Mixed metasploit traffic, sourced from `metasploit_mixed_0.pcapng`

## C2-Only Traffic (`./c2_only`): Exclusively C2 Traffic
- `metasploit_0_filtered.csv` → Metasploit traffic, sourced from `metasploit_0_filtered.pcapng`

## Combined Datasets
- `mixed_combined.csv` → All mixed traffic CSVs merged
- `c2only_combined.csv` → All C2-only traffic CSVs merged
- `full_dataset.csv` → EVERYTHING merged (mixed + C2-only + normal)

- `foo.csv` -> the placeholder for development. 