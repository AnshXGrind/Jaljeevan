<h1 align="center">🐬 JalJeevan Score</h1>
<p align="center"><strong>Real-Time River Health Intelligence · Powered by Pathway</strong></p>
<p align="center">
  <img src="https://img.shields.io/badge/Pathway-Streaming-00c8ff?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTIgMkw0IDdWMTdMMTIgMjJMMjAgMTdWN0wxMiAyWiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIi8+PC9zdmc+" alt="Pathway"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Hack_For_Green_Bharat-🌿-228B22?style=for-the-badge" alt="GreenBharat"/>
</p>

---

## 🚀 Quick Start

```bash
# Clone and setup
git clone https://github.com/AnshXGrind/Jaljeevan
cd Jaljeevan

# Verify installation
python fix_errors.py

# Launch demo (choose one):

# Option 1: Windows
powershell -ExecutionPolicy Bypass -File demo.ps1

# Option 2: Linux/Mac
bash demo.sh

# Option 3: Manual (3 terminals)
# Terminal 1: python pipeline.py
# Terminal 2: python app.py
# Terminal 3: python simulator.py (optional, for live updates)

# Visit dashboard
open http://localhost:8000
```

---

## One-Line Pitch

> **JalJeevan Score uses Gangetic dolphins as living sensors to detect river pollution and illegal sand mining in real time, auto-generating court-ready evidence and auto-filing FIRs for prosecution.**

---

## 🌊 Problem

India's rivers are dying — and enforcement is impossible:

| Issue | Reality |
|-------|---------|
| **Pollution testing** | Happens monthly — too late to act |
| **Sand mining** | Happens at night — no evidence captured |
| **Gangetic dolphins** | India's national aquatic animal, down to ~6,327 |
| **Legal enforcement** | NGT orders exist but no automated monitoring |
| **Data fragmentation** | CPCB, Sentinel-2, WII data sits in silos |

---

## 💡 Solution — Causal Chain

```
┌──────────────────┐    ┌─────────────────────┐    ┌──────────────────┐
│  Sentinel-2 SAR  │───▶│ Sand Mining Detected │───▶│ Turbidity Spike  │
│  (Night Activity)│    │ confidence > 0.80    │    │ anomaly > 2.0    │
└──────────────────┘    └─────────────────────┘    └────────┬─────────┘
                                                            │
                                                            ▼
┌──────────────────┐    ┌─────────────────────┐    ┌──────────────────┐
│  Hydrophone Data │───▶│ Dolphin Count Drops  │◀──│ Upstream Causal  │
│  (WII Acoustic)  │    │ > 20% below 48h avg │    │ JOIN (Pathway)   │
└──────────────────┘    └─────────────────────┘    └──────────────────┘
                                │
                                ▼
                ┌──────────────────────────────┐
                │  AUTO-GENERATE EVIDENCE PKG  │
                │  + File FIR to District Mag. │
                │  + Cite NGT Order 38/2024    │
                └──────────────────────────────┘
```

The core insight: **dolphins are bio-indicators**. When they flee a zone, something upstream is killing the river. Pathway's streaming joins correlate the cause (mining) with the effect (dolphin decline) in real time.

---

## 📊 Dashboard Preview

The live dashboard displays:
- **Real-time Zone Status**: Dolphins per zone with health indicators (🟢 healthy / 🟡 warning / 🔴 critical)
- **Live Alerts**: Mining events with automatic FIR filing buttons
- **Evidence Packages**: Court-ready documentation auto-generated from causal analysis
- **Legal Search**: BM25 RAG search over 6+ NGT environmental orders
- **Causal Timeline**: Visual representation of mining → dolphin decline → automatic prosecution

**Access at**: `http://localhost:8000`

---

## 🔥 How We Used Pathway (10 Requirements)

| # | Hackathon Requirement | Our Implementation | Code Reference |
|---|----------------------|-------------------|----------------|
| 1 | **Live Streaming Ingestion** | `pw.io.csv.read(..., mode="streaming", autocommit_duration_ms=2000)` — watches CSV for new rows every 2s | `pipeline.py` L132–L140 |
| 2 | **Stateful Aggregations** | `.groupby(zone).reduce(avg, min, max, latest, count)` — 48h rolling windows per zone | `pipeline.py` L142–L151 |
| 3 | **Temporal Joins** | `stats.join_left(mining_events, left.zone == right.zone)` — correlates dolphin decline with mining | `pipeline.py` L160–L172 |
| 4 | **Event-Driven Updates** | Output files update within 2s of new CSV row — proven by `simulator.py` | `simulator.py` (entire file) |
| 5 | **Document Store (Live Indexing)** | `data/ngt_orders/` folder with 6 detailed NGT orders; BM25 keyword search | `app.py` bm25_rag() function |
| 6 | **RAG (Retrieval Augmented Generation)** | `/api/legal?q=...` endpoint — hybrid BM25+dynamic search over NGT orders | `app.py` L42–L57 |
| 7 | **Exactly-Once Output** | `pw.io.jsonlines.write()` (real); content-hash dedup `_row_hash()` (simulation) | `pipeline.py` L186, L243 |
| 8 | **Persistence** | `pw.persistence.Config(Backend.filesystem("./persistence/"))` — survives restarts | `pipeline.py` L191–L195 |
| 9 | **Alert Generation** | Causal filter: `mining_detected AND decline > 20%` → auto-generates evidence + auto-files FIR | `pipeline.py` L174–L185 |
| 10 | **Output Sinks** | JSONL sinks: `output/stats.jsonl`, `output/alerts.jsonl` with exactly-once deduplication | `pipeline.py` L188–L189 |

> **Dual-Engine Architecture:** On Linux/WSL the real Pathway binary runs natively.
> On Windows, a semantically identical pure-Python simulation engine runs automatically —
> same schemas, same logic, same output format. Set `PATHWAY_REAL=1` on Linux to force the real engine.

---

## 🏗️ Architecture

```
                    ┌─────────────────────────────────────┐
                    │          PATHWAY ENGINE              │
                    │  (streaming, stateful, exactly-once) │
                    └──────────┬──────────┬────────────────┘
                               │          │
          ┌────────────────────┴──┐   ┌───┴────────────────────┐
          │  pw.io.csv.read()     │   │  pw.io.csv.read()      │
          │  data/live_dolphin.csv│   │  data/live_mining.csv   │
          │  (hydrophone data)    │   │  (satellite detections) │
          └───────────┬───────────┘   └───────────┬────────────┘
                      │                           │
                      ▼                           ▼
              ┌───────────────┐          ┌────────────────┐
              │ groupby(zone) │          │ filter(>0.80)  │
              │ .reduce(      │          │ .groupby(zone) │
              │   avg, count, │          │ .reduce(       │
              │   min, max)   │          │   max_conf)    │
              └───────┬───────┘          └───────┬────────┘
                      │                          │
                      └──────────┬───────────────┘
                                 │
                          ┌──────▼──────┐
                          │  join_left  │  ← CAUSAL CHAIN
                          │  on zone    │
                          └──────┬──────┘
                                 │
                    ┌────────────┼────────────┐
                    ▼            ▼            ▼
            ┌───────────┐ ┌──────────┐ ┌──────────────┐
            │stats.jsonl│ │alerts    │ │evidence.jsonl│
            │           │ │.jsonl    │ │              │
            └─────┬─────┘ └────┬─────┘ └──────┬───────┘
                  │            │               │
                  └────────────┼───────────────┘
                               ▼
                    ┌─────────────────────┐
                    │  FastAPI Dashboard   │
                    │  http://localhost:8000│
                    │  • Zone cards        │
                    │  • Live alerts       │
                    │  • FIR filing        │
                    │  • Legal RAG query   │
                    └─────────────────────┘
```

---

## 📊 Data Sources (All FREE & Public)

| Data Source | Provider | Access | What We Use |
|------------|----------|--------|-------------|
| Dolphin acoustic counts | Wildlife Institute of India (WII) | Free research data | Hydrophone sighting counts per zone |
| Water quality sensors | CPCB (`cpcbedb.nic.in`) | Free government API | BOD, DO, pH, turbidity readings |
| Satellite imagery | Sentinel-2 (ESA Copernicus) | Free | SAR night-activity & turbidity anomaly detection |
| Legal orders | National Green Tribunal | Free public portal | NGT orders for automated legal citation |

> In this demo, we **simulate** sensor data using `simulator.py` which appends realistic rows to CSV files every 10 seconds, proving that Pathway detects and processes changes in real time.

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.9+**
- **Linux/WSL** for real Pathway engine (optional — Windows simulation works for demos)

### 5-Step Launch

```bash
# Step 1 — Clone & enter
git clone https://github.com/YOUR_REPO/Jaljeevan.git
cd Jaljeevan

# Step 2 — Install dependencies
pip install -r requirements.txt

# Step 3 — Start the streaming pipeline (Terminal 1)
python pipeline.py

# Step 4 — Start the dashboard server (Terminal 2)
python app.py

# Step 5 — Start live data simulation (Terminal 3)
python simulator.py
```

Then open **http://localhost:8000** — watch the dashboard update every 5 seconds as `simulator.py` feeds new data.

### WSL/Linux (Real Pathway Engine)

```bash
# Inside WSL Ubuntu:
cd /mnt/d/websites/Jaljeevan   # or your path
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PATHWAY_REAL=1 python pipeline.py   # uses real Pathway binary
```

---

## 📡 Live Streaming Proof

Run all three terminals simultaneously and watch real-time updates:

```
Terminal 1 (pipeline.py):
  ══════════════════════════════════════════════
    JalJeevan Score -- Pathway Streaming Pipeline
  ══════════════════════════════════════════════
  Engine: Simulation (Windows -- identical semantics)
  Streaming:  ACTIVE  (new rows detected every 2000ms)
  Stateful:   ACTIVE  (causal: mining -> dolphin decline)
  Doc Store:  ACTIVE  (watching data/ngt_orders/)
  Persist:    ACTIVE  (./persistence/)

Terminal 2 (app.py):
  Dashboard -> http://localhost:8000
  API docs  -> http://localhost:8000/docs

Terminal 3 (simulator.py):
  [2025-07-27 14:30:10] Tick 001 -- Dolphin data for 3 zones
  [2025-07-27 14:30:20] Tick 002 -- Dolphin data for 3 zones
  ...
  [2025-07-27 14:31:00] Tick 005 -- Dolphin data for 3 zones
    Mining event -- conf:0.92  turbidity:2.7     ← triggers alert!
```

Zone9 (Mirzapur) dolphin count **gradually declines** as mining events accumulate — the dashboard detects this within 2 seconds and fires a causal alert.

---

## 🔌 API Reference

| Endpoint | Method | Description | Response |
|----------|--------|-------------|----------|
| `/` | GET | Dark-themed live dashboard | HTML |
| `/api/stats` | GET | Per-zone dolphin stats with mining flags | `[{zone, dolphin_count, avg_48h, mining_detected, ...}]` |
| `/api/alerts` | GET | Active causal alerts (decline + mining) | `[{zone, decline_pct, case_id, mining_conf, ...}]` |
| `/api/legal?q=...` | GET | BM25 RAG search over NGT legal docs | `{answer, sources, confidence, method}` |
| `/api/fir/{case_id}` | POST | Auto-file FIR (demo) | `{fir_number, submitted_to, legal_sections}` |
| `/api/health` | GET | System health check | `{pathway, stats_file, alerts_file, ngt_docs}` |
| `/docs` | GET | Auto-generated Swagger UI (FastAPI) | Interactive API docs |

---

## 📁 Project Structure

```
Jaljeevan/
├── pipeline.py          # Pathway streaming pipeline (real + simulation engine)
├── app.py               # FastAPI server + dark-themed dashboard (embedded HTML)
├── simulator.py         # Live data appender — proves streaming works
├── config.py            # Central configuration (zones, thresholds, paths)
├── requirements.txt     # Python dependencies
├── .gitignore           # Excludes runtime artifacts
├── README.md            # This file
├── data/
│   ├── live_dolphin.csv # Dolphin sighting stream (auto-generated)
│   ├── live_mining.csv  # Mining detection stream (auto-generated)
│   └── ngt_orders/      # NGT legal documents (RAG corpus)
│       ├── sand_mining_order.txt
│       ├── pollution_order.txt
│       └── stp_order.txt
├── output/              # Pipeline outputs (auto-generated)
│   ├── stats.jsonl      # Per-zone stats (Pathway sink)
│   ├── alerts.jsonl     # Causal alerts (Pathway sink)
│   ├── stats.json       # Dashboard snapshot
│   └── alerts.json      # Dashboard snapshot
└── persistence/         # Pathway state (survives restarts)
    └── state.json
```

---

## ✅ Verification Checklist

| # | What to Check | How to Verify |
|---|--------------|---------------|
| 1 | Pipeline starts without errors | `python pipeline.py` prints "Streaming: ACTIVE" |
| 2 | Dashboard loads | Open `http://localhost:8000` — dark theme with zone cards |
| 3 | Live updates work | Run `simulator.py`, watch dashboard update every 5s |
| 4 | Zone9 declines over time | After ~5 ticks, Zone9 dolphin count drops visibly |
| 5 | Alerts fire automatically | Zone9 shows "CRITICAL" when count drops below 80% of avg |
| 6 | RAG query works | Type "sand mining penalty" in Legal RAG box → returns NGT order |
| 7 | FIR filing works | Click "AUTO-FILE FIR" button → shows FIR number + legal sections |
| 8 | API returns JSON | Visit `http://localhost:8000/docs` → try `/api/stats` |
| 9 | Persistence survives restart | Stop pipeline, restart — data preserved in `persistence/` |
| 10 | Exactly-once output | Check `output/stats.jsonl` — no duplicate rows |

---

## 🏆 Impact

- **6,327 Gangetic dolphins** remain — every detection matters
- **Rs 5 lakh/hectare** environmental compensation per NGT Order 38/2024
- **48-hour FIR deadline** for District Magistrates — our system auto-files immediately
- **Zero-cost data** — all sources (CPCB, Sentinel-2, WII, NGT) are free and public
- **Scalable** — add any Ganga basin zone by editing `config.py`

---

<p align="center">
  <strong>Built with ❤️ and Pathway for Hack For Green Bharat 🌿</strong><br>
  <em>Protecting India's rivers, one dolphin at a time</em>
</p>
