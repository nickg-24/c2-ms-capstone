import subprocess
import pandas as pd
import sys

def is_internal(ip):
    """ Returns 0 if internal, 1 if external """
    if ip.startswith("192.168.1."):
        return 0
    elif ip == "0.0.0.0" or ip == "255.255.255.255": # Local broadcast
        return 0
    else:
        return 1

def run_tshark(pcap_path):
    """
    Runs Tshark to extract only IP-based packet-level data and returns a Pandas DataFrame.
    """

    tshark_cmd = [
        "tshark", "-r", pcap_path, "-Y", "ip", "-T", "fields",
        "-e", "frame.number", "-e", "frame.time_relative",
        "-e", "ip.src", "-e", "ip.dst", "-e", "ip.proto",
        "-e", "frame.len", "-e", "tcp.flags",
        "-E", "header=y", "-E", "separator=,", "-E", "occurrence=f"
    ]

    try:
        result = subprocess.run(tshark_cmd, capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split("\n")
        df = pd.DataFrame([line.split(",") for line in lines[1:]], columns=lines[0].split(","))

        # Handle missing values. if all goes well, we wont see any missing values
        df["frame.number"] = df["frame.number"].astype(int)  # Ensure packet number is an integer
        df["ip.src"] = df["ip.src"].fillna("UNKNOWN")
        df["ip.dst"] = df["ip.dst"].fillna("UNKNOWN")
        df["ip.proto"] = df["ip.proto"].replace("", "-1").fillna("-1").astype(int)  # Set unknown protocols to -1
        df["tcp.flags"] = df["tcp.flags"].fillna("0").apply(lambda x: int(x, 16) if x else 0) # Convert hex to int

        # Convert to internal/external abstraction
        df["src_ip"] = df["ip.src"].apply(lambda x: is_internal(x))
        df["dst_ip"] = df["ip.dst"].apply(lambda x: is_internal(x))

        return df

    except subprocess.CalledProcessError as e:
        print(f"[-] Error running tshark: {e}")
        sys.exit(1)


def extract_features(pcap_path, output_csv, c2_label):
    print(f"[+] Processing {pcap_path}...")
    raw_df = run_tshark(pcap_path)

    # Add C2 label
    raw_df["c2_label"] = c2_label

    # Drop debug columns
    raw_df.drop(columns=["ip.src", "ip.dst"], inplace=True)
    raw_df.drop(columns=["frame.number"], inplace=True)

    raw_df.to_csv(output_csv, index=False)
    print(f"[+] Feature extraction complete. Output saved to: {output_csv}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python extract_features.py <input_pcap> <output_csv> <c2_label>")
        sys.exit(1)

    extract_features(sys.argv[1], sys.argv[2], int(sys.argv[3]))
