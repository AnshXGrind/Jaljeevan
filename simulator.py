"""
JalJeevan Score — Live Data Simulator
======================================
Continuously appends realistic dolphin and mining data to CSV files.
Pathway (or simulation engine) detects these changes immediately and updates the dashboard.

Run this in a separate terminal while pipeline.py is running:
    python simulator.py

This proves the core "live streaming" requirement: new data rows are detected
and processed within 2 seconds.
"""

import time
import random
import csv
import os
from datetime import datetime
from config import DOLPHIN_CSV, MINING_CSV, ZONES

def ensure_files_exist():
    """Create CSV files with headers if they don't exist"""
    os.makedirs("data", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    
    # Dolphin CSV
    if not os.path.exists(DOLPHIN_CSV):
        with open(DOLPHIN_CSV, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "zone", "dolphin_count", "confidence"])
        print(f"✅ Created {DOLPHIN_CSV}")
    
    # Mining CSV
    if not os.path.exists(MINING_CSV):
        with open(MINING_CSV, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "zone", "confidence", "turbidity_anomaly", "night_activity"])
        print(f"✅ Created {MINING_CSV}")

ensure_files_exist()

print("\n" + "=" * 60)
print("  🐬 JalJeevan Live Simulator")
print("=" * 60)
print("  📍 Zones: Zone7 (Varanasi), Zone8 (Ramnagar), Zone9 (Mirzapur)")
print("  ⏱️  Adding new data every 10 seconds")
print("  ⛏️  Mining probability: Zone7=5%, Zone8=10%, Zone9=30%")
print("  Watch http://localhost:8000 for live updates")
print("  Press Ctrl+C to stop")
print("=" * 60 + "\n")

tick = 0
try:
    while True:
        tick += 1
        
        # Generate timestamp
        timestamp = datetime.now().isoformat()
        
        # 1. ADD DOLPHIN DATA
        with open(DOLPHIN_CSV, "a", newline="") as f:
            writer = csv.writer(f)
            for zone in ZONES:
                zone_id = zone["id"] if isinstance(zone, dict) else zone
                # Simulate Zone9 decline (mining impact) - faster decline
                if zone_id == "Zone9":
                    count = max(8, zone.get("base", 20) - (tick // 3) + random.randint(-1, 1))
                else:
                    base = zone.get("base", 30) if isinstance(zone, dict) else 30
                    count = base + random.randint(-3, 3)
                
                confidence = round(random.uniform(0.88, 0.97), 2)
                writer.writerow([timestamp, zone_id, count, confidence])
        
        # 2. MAYBE ADD MINING DATA
        mining_added = []
        for zone in ZONES:
            zone_id = zone["id"] if isinstance(zone, dict) else zone
            
            # Different mining probability per zone
            if zone_id == "Zone7":
                prob = 0.05
            elif zone_id == "Zone8":
                prob = 0.10
            else:  # Zone9
                prob = 0.30
            
            if random.random() < prob:
                with open(MINING_CSV, "a", newline="") as f:
                    writer = csv.writer(f)
                    confidence = round(random.uniform(0.85, 0.98), 2)
                    turbidity = round(random.uniform(2.0, 3.8), 1)
                    night_activity = round(random.uniform(0.75, 0.96), 2)
                    writer.writerow([timestamp, zone_id, confidence, turbidity, night_activity])
                    mining_added.append(zone_id)
        
        # 3. PRINT STATUS
        ts_str = datetime.now().strftime("%H:%M:%S")
        
        if mining_added:
            print(f"  [{ts_str}] Tick {tick:03d} ⛏️  MINING in {', '.join(mining_added)}")
        else:
            print(f"  [{ts_str}] Tick {tick:03d} ✅ Dolphin data added")
        
        time.sleep(10)

except KeyboardInterrupt:
    print("\n\n✅ Simulator stopped")

