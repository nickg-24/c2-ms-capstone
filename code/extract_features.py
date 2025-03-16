import subprocess
import pandas as pd
import sys
import numpy as np

def run_tshark(pcap_path):
    """
    Runs Tshark to extract packet-level data and returns a Pandas DataFrame.
    """
    tshark_cmd = [
        "tshark", "-r", pcap_path, "-T", "fields",
        "-e", "frame.number", "-e", "frame.time_relative",
        "-e", "ip.src", "-e", "ip.dst", "-e", "ip.proto",
        "-e", "frame.len", "-e", "tcp.flags",
        "-E", "header=y", "-E", "separator=,", "-E", "occurrence=f"
    ]

    try:
        # Run Tshark command and capture output
        result = subprocess.run(tshark_cmd, capture_output=True, text=True, check=True)

        # Convert output to list of lines
        lines = result.stdout.strip().split("\n")

        # Load into Pandas DataFrame
        df = pd.DataFrame([line.split(",") for line in lines[1:]], columns=lines[0].split(","))

        # Convert numeric fields to proper types
        df["frame.time_relative"] = df["frame.time_relative"].astype(float)
        df["frame.len"] = df["frame.len"].astype(int)
        df["ip.proto"] = df["ip.proto"].astype(int)
        df["tcp.flags"] = df["tcp.flags"].apply(lambda x: int(x, 16) if x else 0)  # Convert hex flags to int

        return df

    except subprocess.CalledProcessError as e:
        print(f"[-] Error running tshark: {e}")
        sys.exit(1)


def derive_features(df):
    """
    Computes additional derived features for ML analysis.
    """
    df = df.copy()  # Avoid modifying original DataFrame

    # Inter-Packet Timing (Time Difference Between Packets)
    df["inter_packet_time"] = df["frame.time_relative"].diff().fillna(0)

    # HOMENET vs INTERNET (0 = internal, 1 = external)
    df["is_external"] = df["ip.dst"].apply(lambda x: 1 if not x.startswith("192.168.1.") else 0)

    # Drop unnecessary columns
    df = df.drop(columns=["frame.number", "frame.time_relative", "ip.src", "ip.dst"])

    return df

def extract_features(pcap_path, output_csv):
    """
    Extracts and processes network traffic features from a PCAP file.
    """
    print(f"[+] Processing {pcap_path}...")

    # Run Tshark & Get DataFrame
    raw_df = run_tshark(pcap_path)

    # Derive Features
    feature_df = derive_features(raw_df)

    # Save to CSV
    feature_df.to_csv(output_csv, index=False)
    print(f"[+] Feature extraction complete. Output saved to: {output_csv}")

# Example usage:
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_features.py <input_pcap> <output_csv>")
        sys.exit(1)

    pcap_file = sys.argv[1]
    output_file = sys.argv[2]
    
    extract_features(pcap_file, output_file)
