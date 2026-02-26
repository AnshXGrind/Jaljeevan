"""
JalJeevan Score — Live Data Simulator
======================================
Run in a SEPARATE terminal while pipeline.py and app.py are running.
Appends new sensor rows every 10 seconds to prove that Pathway detects
file changes and updates output/stats.jsonl automatically — this is the
core "live streaming" requirement judges will test.

Usage:
    python simulator.py
"""

import time, random
from datetime import datetime
from config import DOLPHIN_CSV, MINING_CSV, ZONES

print("=" * 52)
print("  JalJeevan Live Simulator")
print("  Appending new sensor data every 10 seconds")
print("  Zone9 will decline (simulates upstream mining)")
print("  Watch http://localhost:8000 for live updates")
print("  Ctrl+C to stop")
print("=" * 52 + "\n")

tick = 0
while True:
    tick += 1
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(DOLPHIN_CSV, "a") as f:
        for z in ZONES:
            if z["id"] == "Zone9":
                count = max(8, z["base"] - tick * 2 + random.randint(-2, 1))
            else:
                count = z["base"] + random.randint(-2, 2)
            f.write(f"{ts},{z['id']},{count},0.{random.randint(88,97)}\n")

    print(f"[{ts}] Tick {tick:03d} -- dolphin readings written ({len(ZONES)} zones)")

    if tick % 5 == 0:
        conf  = round(random.uniform(0.86, 0.97), 2)
        turb  = round(random.uniform(2.1, 3.8), 2)
        night = round(random.uniform(0.82, 0.96), 2)
        with open(MINING_CSV, "a") as f:
            f.write(f"{ts},Zone9,{conf},{turb},{night}\n")
        print(f"  Mining event -- conf:{conf}  turbidity:{turb}")

    time.sleep(10)
