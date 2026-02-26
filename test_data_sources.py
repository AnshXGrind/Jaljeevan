# test_data_sources.py
import pandas as pd
import os

print("📊 DATA SOURCES CHECK\n")

# Check dolphin data
if os.path.exists("data/live_dolphin.csv"):
    df = pd.read_csv("data/live_dolphin.csv")
    print(f"✅ Dolphin data: {len(df)} rows")
    print(f"   Columns: {list(df.columns)}")
    print(f"   Zones: {df['zone'].unique()}")
    print(f"   Time range: {df['timestamp'].iloc[0]} to {df['timestamp'].iloc[-1]}\n")
else:
    print("❌ Dolphin data not found\n")

# Check mining data
if os.path.exists("data/live_mining.csv"):
    df = pd.read_csv("data/live_mining.csv")
    print(f"✅ Mining data: {len(df)} rows")
    print(f"   Mining events: {len(df[df['confidence'] > 0.8])}\n")

# Check legal docs
ngt_files = os.listdir("data/ngt_orders/") if os.path.exists("data/ngt_orders/") else []
print(f"✅ Legal documents: {len(ngt_files)} files")
for f in ngt_files:
    print(f"   - {f}")
