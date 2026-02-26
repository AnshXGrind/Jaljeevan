# JalJeevan Score — Real-Time River Health Intelligence

## Hack For Green Bharat Submission

### One-Line Pitch
JalJeevan Score uses Gangetic dolphins as living sensors to detect river pollution and illegal sand mining in real time, auto-generating court-ready evidence for prosecution.

---

## Problem
- India's rivers are dying but enforcement is impossible
- Pollution testing happens monthly — too late to act
- Sand mining happens at night — no evidence
- Gangetic dolphins (India's national aquatic animal) down to ~6,327

## Solution
Real-time streaming system that:
1. **Listens** to dolphins via hydrophones (simulated from WII data)
2. **Monitors** CPCB water quality sensors (free Indian govt API)
3. **Detects** sand mining from Sentinel-2 satellite (free ESA data)
4. **Correlates** dolphin disappearance with upstream events (48h windows)
5. **Auto-generates** evidence packages with NGT legal references

---

## Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Streaming Engine** | Pathway | Real-time ingestion, temporal windows, stateful joins |
| **RAG** | Pathway LLM xPack | Live document indexing, legal retrieval |
| **Backend** | FastAPI | REST APIs for dashboard |
| **Frontend** | HTML/JS | Live dashboard |
| **Data Sources** | CPCB, Sentinel-2, WII, NGT | All FREE and public |

---

## Features Implemented

- [x] Live streaming ingestion (CSV in streaming mode)
- [x] Per-zone dolphin aggregation (stateful)
- [x] Mining event detection (confidence + night activity)
- [x] Causal chain analysis (dolphin stats joined with mining events)
- [x] Auto-generated evidence packages (JSON)
- [x] Legal RAG assistant (demo)
- [x] One-click FIR filing (demo)
- [x] Beautiful real-time dashboard
- [x] JSONL output sinks

---

## 🔥 How We Used Pathway (Hackathon Requirements)

| Requirement | Our Implementation |
|-------------|-------------------|
| **Live Streaming Ingestion** | `mode="streaming"` with `autocommit_duration_ms=2000` — watches CSV files for changes every 2 s |
| **Stateful Window Computations** | 48-hour rolling averages per zone using `pw.reducers.avg()` |
| **Document Store (Live Indexing)** | `DocumentStore` monitors `ngt_orders/` folder, auto-indexes new files |
| **LLM xPack RAG** | Legal documents indexed and retrievable via `/api/legal/query` |
| **Exactly-Once Semantics** | `exactly_once=True` on all output sinks (content-hash dedup on Windows) |
| **Persistence** | `pw.run(persistence=True)` with filesystem backend (`./persistence/`) |
| **Custom Connector Ready** | Architecture supports adding custom Python connector |

> **Windows note:** Pathway's native binary ships for Linux/macOS only.  
> On Windows the pipeline runs an exact semantic clone in pure Python.  
> To use the real Pathway engine, run in WSL/Linux and set `PATHWAY_REAL=1`.

---

## Quick Start

### Prerequisites
- Python 3.9+

### Installation

```bash
# 1. Enter directory
cd jaljeevan-pathway-monitor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run Pathway pipeline (Terminal 1)
python pipeline.py

# 4. Run FastAPI dashboard (Terminal 2)
python app.py

# 5. Open browser
# http://localhost:8000
```

---

## Project Structure

```
jaljeevan-pathway-monitor/
├── pipeline.py          # Main Pathway streaming pipeline
├── app.py               # FastAPI dashboard server
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
├── data/                # Live data streams
│   ├── live_dolphin.csv # Generated on pipeline start
│   ├── live_mining.csv  # Generated on pipeline start
│   └── ngt_orders/      # Legal documents
│       ├── sand_mining_order.txt
│       ├── pollution_order.txt
│       └── stp_order.txt
├── templates/           # HTML dashboard
│   └── dashboard.html
└── output/              # Pipeline outputs (JSONL)
```

---

## Data Sources (All FREE)

| Data | Source | Cost |
|------|--------|------|
| Dolphin acoustic | Wildlife Institute of India | Free research data |
| Water quality | CPCB (cpcbedb.nic.in) | Free API |
| Satellite imagery | Sentinel-2 (ESA) | Free |
| Legal orders | NGT portal | Free |

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Dashboard |
| `/api/health` | GET | Health check |
| `/api/stats/current` | GET | Current river stats |
| `/api/alerts/latest` | GET | Latest causal alerts |
| `/api/evidence/latest` | GET | Latest evidence packages |
| `/api/legal/query?q=...` | GET | Legal RAG query |
| `/api/fir/file/{case_id}` | POST | Auto-file FIR (demo) |

---

Built with **Pathway** for Hack For Green Bharat
