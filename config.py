"""
Configuration file for JalJeevan Score
All settings centralized here
"""

# ============================================================================
# PATHWAY CONFIGURATION
# ============================================================================
PATHWAY_CONFIG = {
    "persistence": True,
    "persistence_path": "./persistence",
    "exactly_once": True,
}

# ============================================================================
# DATA SOURCES (All FREE)
# ============================================================================
DATA_SOURCES = {
    "dolphin": {
        "path": "data/live_dolphin.csv",
        "mode": "streaming",
        "autocommit_duration_ms": 1000
    },
    "mining": {
        "path": "data/live_mining.csv",
        "mode": "streaming",
        "autocommit_duration_ms": 1000
    },
    "ngt_orders": {
        "path": "data/ngt_orders/",
        "autoupdate": True
    }
}

# ============================================================================
# RIVER ZONES (Ganga stretches)
# ============================================================================
RIVER_ZONES = [
    {"id": "Zone7", "name": "Varanasi North", "lat": 25.3176, "lon": 82.9739},
    {"id": "Zone8", "name": "Ramnagar", "lat": 25.4102, "lon": 82.8912},
    {"id": "Zone9", "name": "Mirzapur", "lat": 25.5012, "lon": 82.8123}
]

# ============================================================================
# ALERT THRESHOLDS
# ============================================================================
THRESHOLDS = {
    "dolphin_decline_percent": 20,   # Alert if >20% drop
    "mining_confidence": 0.8,        # Mining detection threshold
    "pollution_bod": 30,             # mg/L - critical BOD level
    "pollution_do": 2                # mg/L - critical dissolved oxygen
}

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
# LLM CONFIGURATION (Using free model)
# ============================================================================
LLM_CONFIG = {
    "model": "gpt-3.5-turbo",  # Replace with local model if no API key
    "temperature": 0.1,
    "max_tokens": 500
}
