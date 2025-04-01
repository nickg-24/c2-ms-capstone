# run this from c2-ms-capstone> 
import pandas as pd

def merge_csv(to_be_merged, output_file):
    """
    Merges multiple CSV files into a single file.

    Parameters:
    - to_be_merged (list): List of file paths to be merged.
    - output_file (str): Path to save the merged CSV.

    Returns:
    - None
    """
    # Load and concatenate all CSVs
    df_list = [pd.read_csv(csv_file) for csv_file in to_be_merged]
    merged_df = pd.concat(df_list, ignore_index=True)

    # Save the merged CSV
    merged_df.to_csv(output_file, index=False)
    print(f"[+] Merged {len(to_be_merged)} CSV files into {output_file}")


# to_be_merged = ["./data/c2_only/metasploit_0_filtered.csv", "./data/mixed/metasploit_mixed_0.csv", "./data/c2_only/metasploit_beaconing_0.csv", "./data/c2_only/metasploit_beaconing_1.csv", "./data/c2_only/metasploit_beaconing_2.csv"]
# to_be_merged = ["./data/combined_datasets/foo.csv", "./data/mixed/metasploit_mixed_0.csv"]
to_be_merged = [
    "./data/c2_only/covenant_beaconing_0.csv", 
    "./data/c2_only/covenant_beaconing_1.csv", 
    "./data/c2_only/covenant_beaconing_2.csv", 
    "./data/c2_only/metasploit_beaconing_0.csv",
    "./data/c2_only/metasploit_beaconing_1.csv",
    "./data/c2_only/metasploit_beaconing_2.csv",
    "./data/c2_only/metasploit_0_filtered.csv",
    "./data/mixed/metasploit_mixed_0.csv"
]
# output_file = "./data/combined_datasets/foo.csv"
output_file = "./data/combined_datasets/full_dataset.csv"

merge_csv(to_be_merged, output_file)
