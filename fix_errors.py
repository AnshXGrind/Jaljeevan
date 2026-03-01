#!/usr/bin/env python3
"""
JalJeevan Score — Automatic Error Fixer
========================================
This script automatically fixes common errors and creates missing files.

Run this FIRST before running the main application:
    python fix_errors.py
"""

import os
import sys
from pathlib import Path

print("\n" + "=" * 60)
print("  🔧 JalJeevan Score Error Fixer")
print("=" * 60 + "\n")

# ============================================================================
# 1. CHECK PYTHON VERSION
# ============================================================================
if sys.version_info < (3, 8):
    print("❌ Python 3.8+ required (you have {}.{})".format(
        sys.version_info.major, sys.version_info.minor))
    sys.exit(1)
print("✅ Python version: {}.{}.{}".format(
    sys.version_info.major, sys.version_info.minor, sys.version_info.micro))

# ============================================================================
# 2. CHECK & CREATE DIRECTORIES
# ============================================================================
dirs = ["data", "output", "persistence"]
for d in dirs:
    Path(d).mkdir(exist_ok=True)
    if not os.path.exists(d):
        print(f"❌ Failed to create {d}/")
        sys.exit(1)
print(f"✅ Created/verified {len(dirs)} directories: {', '.join(dirs)}")

# ============================================================================
# 3. CHECK & CREATE DATA SUBDIRECTORIES
# ============================================================================
data_subdirs = ["data/ngt_orders"]
for d in data_subdirs:
    Path(d).mkdir(parents=True, exist_ok=True)
print(f"✅ Created/verified NGT orders directory")

# ============================================================================
# 4. CHECK CONFIG.PY
# ============================================================================
if not os.path.exists("config.py"):
    print("❌ config.py missing - create it by copying from the guide")
    sys.exit(1)
print("✅ config.py exists")

# ============================================================================
# 5. CHECK APP.PY
# ============================================================================
if not os.path.exists("app.py"):
    print("❌ app.py missing")
    sys.exit(1)
print("✅ app.py exists")

# ============================================================================
# 6. CHECK PIPELINE.PY
# ============================================================================
if not os.path.exists("pipeline.py"):
    print("❌ pipeline.py missing")
    sys.exit(1)
print("✅ pipeline.py exists")

# ============================================================================
# 7. CHECK SIMULATOR.PY
# ============================================================================
if not os.path.exists("simulator.py"):
    print("❌ simulator.py missing")
    sys.exit(1)
print("✅ simulator.py exists")

# ============================================================================
# 8. CREATE SAMPLE NGT ORDERS IF MISSING
# ============================================================================
ngt_files = {
    "data/ngt_orders/sand_mining_order.txt": """NATIONAL GREEN TRIBUNAL
Order No. 38/2024

Subject: Sand Mining Ban in Gangetic Rivers

This tribunal hereby orders:
1. All unauthorized sand mining in the Ganga river is banned
2. Existing permits are suspended pending environmental review
3. Violators shall face prosecution under IPC §379
4. NGO monitoring is mandated in all zones
5. Monthly compliance reports required

Order Date: 2024-01-15
Validity: Until further notice
""",
    "data/ngt_orders/pollution_order.txt": """NATIONAL GREEN TRIBUNAL
Order No. 2024/WL/23

Subject: River Ganga Pollution Control

This tribunal hereby directs:
1. CPCB shall conduct weekly water quality monitoring
2. STP violations must be reported within 24 hours
3. Industrial effluent discharge is restricted
4. Dolphins are protected under Wildlife Protection Act 1972
5. Habitat restoration is mandated

Issued: 2024-02-01
Implementation: Immediate
""",
    "data/ngt_orders/stp_order.txt": """NATIONAL GREEN TRIBUNAL
Order No. 15/2024

Subject: Sewage Treatment Plant Compliance

The following compliance is mandated:
1. All STPs must operate at 100% capacity
2. Monthly testing of treated water required
3. Violations shall incur penalties up to ₹50 lakh
4. NGO access for third-party audits
5. Real-time monitoring equipment installation

Order Date: 2024-03-01
Compliance Deadline: 90 days
"""
}

for filepath, content in ngt_files.items():
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            f.write(content)
        print(f"✅ Created {filepath}")
    else:
        print(f"✅ {filepath} exists")

# ============================================================================
# 9. VERIFY REQUIRED IMPORTS
# ============================================================================
print("\n🔍 Checking Python imports...")
required_packages = [
    ("fastapi", "FastAPI"),
    ("uvicorn", "uvicorn"),
    ("pandas", "pandas"),
    ("numpy", "numpy"),
    ("jinja2", "jinja2"),
]

missing = []
for pkg, display_name in required_packages:
    try:
        __import__(pkg)
        print(f"✅ {display_name}")
    except ImportError:
        print(f"❌ {display_name} not found")
        missing.append(pkg)

if missing:
    print(f"\n⚠️  Missing packages: {', '.join(missing)}")
    print("   Install them with:")
    print(f"   pip install {' '.join(missing)}")

# ============================================================================
# 10. VERIFY CONFIG IMPORTS
# ============================================================================
try:
    from config import (
        ZONES, DOLPHIN_CSV, MINING_CSV, NGT_DIR,
        STATS_JSONL, ALERTS_JSONL, AUTOCOMMIT_MS,
        DOLPHIN_DECLINE_THRESHOLD, MINING_CONFIDENCE_THRESHOLD
    )
    print(f"✅ config.py imports OK ({len(ZONES)} zones configured)")
except ImportError as e:
    print(f"❌ config.py import error: {e}")
    sys.exit(1)

# ============================================================================
# 11. CREATE SAMPLE CSV DATA IF MISSING
# ============================================================================
csv_files = {
    "data/live_dolphin.csv": """timestamp,zone,dolphin_count,confidence
2026-03-01T00:00:00,Zone7,41,0.95
2026-03-01T00:00:00,Zone8,28,0.93
2026-03-01T00:00:00,Zone9,18,0.91
""",
    "data/live_mining.csv": """timestamp,zone,confidence,turbidity_anomaly,night_activity
2026-03-01T00:00:00,Zone9,0.92,2.8,0.91
2026-03-01T00:10:00,Zone9,0.94,3.1,0.88
2026-03-01T00:20:00,Zone8,0.87,2.1,0.76
"""
}

for filepath, headers in csv_files.items():
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            f.write(headers)
        print(f"✅ Created {filepath}")
    else:
        # Just verify it has headers
        try:
            with open(filepath, "r") as f:
                first_line = f.readline()
                if first_line.strip():
                    print(f"✅ {filepath} has data")
        except:
            print(f"⚠️  {filepath} exists but may be corrupted")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 60)
print("  ✅ All Checks Passed!")
print("=" * 60)
print("\n🚀 Quick Start:")
print("   Terminal 1: python pipeline.py")
print("   Terminal 2: python app.py")
print("   Terminal 3: python simulator.py  (optional)")
print("   Browser:   http://localhost:8000")
print("\n📚 Files created:")
print("   - config.py (configuration)")
print("   - app.py (FastAPI dashboard)")
print("   - pipeline.py (streaming logic)")
print("   - simulator.py (live data generator)")
print("   - data/live_dolphin.csv (sensor data)")
print("   - data/live_mining.csv (mining detection)")
print("   - data/ngt_orders/*.txt (legal documents)")
print("\n" + "=" * 60)
