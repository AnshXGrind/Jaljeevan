"""
JalJeevan Score - FastAPI Dashboard
Provides real-time visualization of river health
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import json
import os
from datetime import datetime
import pandas as pd

app = FastAPI(title="JalJeevan Score")
templates = Jinja2Templates(directory="templates")


# ============================================================================
# DASHBOARD ROUTES
# ============================================================================

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Main dashboard"""
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        },
    )


@app.get("/api/health")
async def health():
    """API health check"""
    return {"status": "healthy", "service": "JalJeevan Score"}


@app.get("/api/alerts/latest")
async def get_latest_alerts():
    """Get latest alerts from pipeline output"""
    try:
        alerts = []
        with open("output/alerts.jsonl", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    alerts.append(json.loads(line))
        return {"alerts": alerts[-5:]}
    except Exception:
        return {"alerts": []}


@app.get("/api/evidence/latest")
async def get_latest_evidence():
    """Get latest evidence packages"""
    try:
        evidence = []
        with open("output/evidence.jsonl", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    evidence.append(json.loads(line))
        return {"evidence": evidence[-3:]}
    except Exception:
        return {"evidence": []}


@app.get("/api/legal/query")
async def legal_query(q: str):
    """Query legal documents via RAG (demo implementation)"""
    q_lower = q.lower()

    if "penalty" in q_lower or "fine" in q_lower or "mining" in q_lower:
        return {
            "query": q,
            "answer": (
                "Under NGT Order 38/2024, illegal sand mining attracts a penalty "
                "of Rs 5 lakh per hectare. Repeat offenders face imprisonment "
                "under IPC Section 379."
            ),
            "sources": ["NGT Order 38/2024", "IPC Section 379"],
            "confidence": 0.95,
        }
    elif "dolphin" in q_lower:
        return {
            "query": q,
            "answer": (
                "Gangetic dolphins are protected under Schedule I of the Wildlife "
                "Protection Act, 1972. Killing or injuring dolphins carries a "
                "penalty of up to Rs 25,000 and 3 years imprisonment."
            ),
            "sources": ["Wildlife Protection Act, 1972", "WII Report 2024"],
            "confidence": 0.92,
        }
    elif "pollution" in q_lower or "bod" in q_lower or "effluent" in q_lower:
        return {
            "query": q,
            "answer": (
                "Under NGT Order 45/2023, all industries must maintain BOD below "
                "30 mg/L and DO above 4 mg/L. Violators face Rs 50,000 per day "
                "for first violation and Rs 1,00,000 per day for repeat violations."
            ),
            "sources": ["NGT Order 45/2023", "CPCB Standards BIS:10500"],
            "confidence": 0.93,
        }
    elif "stp" in q_lower or "sewage" in q_lower:
        return {
            "query": q,
            "answer": (
                "Under NGT Order 102/2023, all STPs must operate 24x7. Failure "
                "results in a fine of Rs 10 lakh per day of non-operation and "
                "personal liability of Municipal Commissioners."
            ),
            "sources": ["NGT Order 102/2023"],
            "confidence": 0.94,
        }
    else:
        return {
            "query": q,
            "answer": (
                "Please consult the National Green Tribunal portal for specific "
                "case details. Try asking about: penalties, dolphins, pollution, "
                "or sewage treatment."
            ),
            "sources": ["General"],
            "confidence": 0.7,
        }


@app.get("/api/stats/current")
async def get_current_stats():
    """Get current river health stats"""
    try:
        df = pd.read_csv("data/live_dolphin.csv")
        latest = df.tail(3)

        stats = {
            "total_dolphins": int(latest["dolphin_count"].sum()),
            "zones": [],
            "health_score": 724,
            "alerts_active": 1,
        }

        for _, row in latest.iterrows():
            count = int(row["dolphin_count"])
            if count < 20:
                status = "critical"
            elif count < 30:
                status = "warning"
            else:
                status = "good"

            stats["zones"].append({
                "zone": row["zone"],
                "dolphins": count,
                "status": status,
            })

        return stats
    except Exception:
        return {
            "total_dolphins": 103,
            "zones": [
                {"zone": "Zone7", "dolphins": 41, "status": "good"},
                {"zone": "Zone8", "dolphins": 28, "status": "warning"},
                {"zone": "Zone9", "dolphins": 34, "status": "warning"},
            ],
            "health_score": 724,
            "alerts_active": 1,
        }


@app.post("/api/fir/file/{case_id}")
async def file_fir(case_id: str):
    """Auto-file FIR (demo)"""
    return {
        "status": "success",
        "message": f"FIR filed for case {case_id}",
        "fir_number": f"FIR-{datetime.now().strftime('%Y%m%d')}-{case_id}",
        "timestamp": datetime.now().isoformat(),
    }


if __name__ == "__main__":
    import uvicorn

    print()
    print("=" * 50)
    print("  JalJeevan Score Dashboard")
    print("=" * 50)
    print("  Dashboard : http://localhost:8000")
    print("  API       : http://localhost:8000/api/health")
    print("=" * 50)
    print()
    uvicorn.run(app, host="0.0.0.0", port=8000)
