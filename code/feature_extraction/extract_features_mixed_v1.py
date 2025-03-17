import subprocess
import pandas as pd
import numpy as np
import sys

C2_HOST = "192.168.2.15"  # Hardcoded C2 host IP

def is_internal(ip):
    """ Returns 0 if internal, 1 if external """
    if isinstance(ip, str) and ip.startswith("192.168.1."):
        return 0
    elif ip == "0.0.0.0" or ip == "255.255.255.255":  # Local broadcast
        return 0
    else:
        return 1

def is_c2_traffic(src_ip, dst_ip):
    """ Determines if a packet is C2 traffic based on hardcoded C2 server IP. """
    return 1 if src_ip.strip() == C2_HOST or dst_ip.strip() == C2_HOST else 0

def extract_tcp_flags(flag_value):
    """ Extracts individual TCP flags from a numeric flag value. Returns a dictionary of binary flags. """
    return {
        "is_SYN": (flag_value & 0x02) >> 1,
        "is_ACK": (flag_value & 0x10) >> 4,
        "is_RST": (flag_value & 0x04) >> 2,
        "is_FIN": (flag_value & 0x01),
        "is_PSH": (flag_value & 0x08) >> 3,
        "is_URG": (flag_value & 0x20) >> 5,
    }

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

        # Handle missing values
        df["frame.number"] = df["frame.number"].astype(int)
        df["ip.src"] = df["ip.src"].fillna("UNKNOWN").astype(str).str.strip()
        df["ip.dst"] = df["ip.dst"].fillna("UNKNOWN").astype(str).str.strip()
        df["ip.proto"] = df["ip.proto"].replace("", "-1").fillna("-1").astype(int)
        df["tcp.flags"] = df["tcp.flags"].fillna("0").apply(lambda x: int(x, 16) if x else 0)
        df["frame.len"] = df["frame.len"].astype(int)
        df["frame.time_relative"] = df["frame.time_relative"].astype(float)

        # Convert IPs to internal/external
        df["src_ip"] = df["ip.src"].apply(is_internal)
        df["dst_ip"] = df["ip.dst"].apply(is_internal)

        # Label C2 traffic dynamically
        df["c2_label"] = df.apply(lambda row: is_c2_traffic(row["ip.src"], row["ip.dst"]), axis=1)

        # Extract TCP flag features
        flag_features = df["tcp.flags"].apply(extract_tcp_flags).apply(pd.Series)
        df = pd.concat([df, flag_features], axis=1)

        return df

    except subprocess.CalledProcessError as e:
        print(f"[-] Error running tshark: {e}")
        sys.exit(1)

def extract_features(pcap_path, output_csv):
    print(f"[+] Processing {pcap_path}...")
    raw_df = run_tshark(pcap_path)

    # Debugging: Check for C2 traffic
    print(f"[+] Total packets in capture: {len(raw_df)}")
    print(f"[+] Total C2 packets found: {raw_df['c2_label'].sum()}")

    # Compute Time Since Last Packet
    raw_df["time_since_last"] = raw_df["frame.time_relative"].diff().fillna(0)

    # Compute Ratio of Time Between Packets
    raw_df["delta_t_ratio"] = raw_df["time_since_last"] / raw_df["time_since_last"].shift(1).replace(0, np.nan)
    raw_df["delta_t_ratio"] = raw_df["delta_t_ratio"].fillna(1)

    # Compute Rolling Window Features (Mean & Standard Deviation)
    window_sizes = [3, 5, 10]
    for window in window_sizes:
        raw_df[f"rolling_mean_delta_t_{window}"] = raw_df["time_since_last"].rolling(window=window, min_periods=1).mean()
        raw_df[f"rolling_std_delta_t_{window}"] = raw_df["time_since_last"].rolling(window=window, min_periods=1).std()

    # Drop unnecessary columns
    raw_df.drop(columns=["ip.src", "ip.dst", "frame.time_relative", "frame.number", "tcp.flags"], inplace=True)
    # Handle NaNs in the first row
    raw_df.iloc[0] = raw_df.iloc[0].fillna(0)


    raw_df.to_csv(output_csv, index=False)
    print(f"[+] Feature extraction complete. Output saved to: {output_csv}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_features_mixed.py <input_pcap> <output_csv>")
        sys.exit(1)

    extract_features(sys.argv[1], sys.argv[2])
