"""JalJeevan Score — Configuration"""

# Pathway engine
PERSISTENCE_DIR = "./persistence"
AUTOCOMMIT_MS   = 2000          # Pathway polls for new CSV rows every 2s

# Alert thresholds
DOLPHIN_DECLINE_THRESHOLD   = 0.20   # Alert when count drops >20% below 48h avg
MINING_CONFIDENCE_THRESHOLD = 0.80   # Minimum Sentinel-2 detection confidence

# River zones — Ganga, Varanasi to Mirzapur stretch
ZONES = [
    {"id": "Zone7", "name": "Varanasi North", "lat": 25.3176, "lon": 82.9739, "base": 41},
    {"id": "Zone8", "name": "Ramnagar",        "lat": 25.4102, "lon": 82.8912, "base": 28},
    {"id": "Zone9", "name": "Mirzapur",        "lat": 25.5012, "lon": 82.8123, "base": 34},
]

# File paths
DATA_DIR     = "data"
OUTPUT_DIR   = "output"
NGT_DIR      = "data/ngt_orders"
DOLPHIN_CSV  = "data/live_dolphin.csv"
MINING_CSV   = "data/live_mining.csv"
STATS_JSONL  = "output/stats.jsonl"
ALERTS_JSONL = "output/alerts.jsonl"
