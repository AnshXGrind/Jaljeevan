"""
JalJeevan Score — Configuration File
All settings centralized here
"""

import os
from pathlib import Path

# ============================================================================
# PATHS
# ============================================================================
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
NGT_DIR = DATA_DIR / "ngt_orders"
PERSISTENCE_DIR = BASE_DIR / "persistence"

# CSV Files
DOLPHIN_CSV = DATA_DIR / "live_dolphin.csv"
MINING_CSV = DATA_DIR / "live_mining.csv"

# Output Files
STATS_JSONL = OUTPUT_DIR / "stats.jsonl"
ALERTS_JSONL = OUTPUT_DIR / "alerts.jsonl"

# ============================================================================
# STREAMING CONFIGURATION
# ============================================================================
AUTOCOMMIT_MS = 2000  # Check for new data every 2 seconds

# ============================================================================
# THRESHOLDS
# ============================================================================
DOLPHIN_DECLINE_THRESHOLD = 0.20  # Alert if >20% drop from 48h average
MINING_CONFIDENCE_THRESHOLD = 0.80  # Only consider mining with >80% confidence

# ============================================================================
# RIVER ZONES
# ============================================================================
ZONES = [
    {"id": "Zone7", "name": "Varanasi North", "base": 40, "lat": 25.3176, "lon": 82.9739},
    {"id": "Zone8", "name": "Ramnagar", "base": 30, "lat": 25.4102, "lon": 82.8912},
    {"id": "Zone9", "name": "Mirzapur", "base": 20, "lat": 25.5012, "lon": 82.8123},
]

# Zone lookup dictionary
ZONE_DICT = {z["id"]: z for z in ZONES}

# ============================================================================
# RAG CONFIGURATION
# ============================================================================
RAG_CONFIG = {
    "chunk_size": 500,
    "embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
    "retrieval_strategy": "hybrid",  # BM25 + semantic
    "bm25_weight": 0.3,
    "semantic_weight": 0.7,
    "k_retrieval": 3
}

# ============================================================================
# LLM CONFIGURATION
# ============================================================================
LLM_CONFIG = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.1,
    "max_tokens": 500
}

# ============================================================================
# API CONFIGURATION
# ============================================================================
API_HOST = "0.0.0.0"
API_PORT = 8000
API_REFRESH_MS = 5000  # Dashboard refresh every 5 seconds
