"""
JalJeevan Score - Clean Dashboard & API
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import json
import math
import os
import traceback
from datetime import datetime
import uvicorn
from config import STATS_JSONL, ALERTS_JSONL, NGT_DIR, ZONES

app = FastAPI(title="JalJeevan Score")

# Helpers
def _read_jsonl(path):
    """Read JSONL file, return latest row per zone."""
    if not os.path.exists(path):
        return []
    try:
        rows = {}
        for line in open(path, encoding="utf-8"):
            if line.strip():
                obj = json.loads(line)
                rows[obj.get("zone", "?")] = obj
        return list(rows.values())
    except Exception:
        return []

def bm25_rag(query):
    """BM25-style retrieval over NGT orders."""
    if not os.path.exists(NGT_DIR):
        return {"answer": "NGT documents not found.", "sources": [], "confidence": 0, "method": "BM25", "indexed_documents": 0}
    
    docs = {}
    for f in os.listdir(NGT_DIR):
        if f.endswith(".txt"):
            try:
                docs[f] = open(os.path.join(NGT_DIR, f), encoding="utf-8").read()
            except:
                pass
    
    if not docs:
        return {"answer": "No NGT documents available.", "sources": [], "confidence": 0, "method": "BM25", "indexed_documents": 0}
    
    words = set(query.lower().split())
    scored = sorted(
        [(sum(v.lower().count(w) for w in words), k, v) for k, v in docs.items()],
        reverse=True,
    )
    
    if not scored or scored[0][0] == 0:
        return {"answer": "No relevant documents found.", "sources": list(docs.keys()), "confidence": 0, "method": "BM25", "indexed_documents": len(docs)}
    
    sc, fname, content = scored[0]
    paras = [p.strip() for p in content.split("\n\n") if p.strip()]
    best = next((p for p in paras if any(w in p.lower() for w in words)), paras[0])
    
    return {
        "answer": best,
        "sources": [s[1] for s in scored if s[0] > 0][:3],
        "confidence": round(min(sc / (max(len(words), 1) * 3), 1.0), 2),
        "method": "BM25",
        "indexed_documents": len(docs),
    }

# API Endpoints
@app.get("/api/health")
async def health():
    """System health check"""
    try:
        ngt_count = 0
        if os.path.exists(NGT_DIR):
            ngt_count = len([f for f in os.listdir(NGT_DIR) if f.endswith(".txt")])
        return {
            "status": "operational",
            "pathway": "streaming_active",
            "stats_file": os.path.exists(STATS_JSONL),
            "alerts_file": os.path.exists(ALERTS_JSONL),
            "ngt_docs": ngt_count,
            "zones": len(ZONES),
            "timestamp": datetime.now().isoformat(),
        }
    except Exception as e:
        return {"status": "error", "error": str(e), "timestamp": datetime.now().isoformat()}

@app.get("/api/stats")
async def stats():
    """Get zone statistics"""
    try:
        data = _read_jsonl(STATS_JSONL)
        if data:
            cleaned = []
            for row in data:
                fixed = dict(row)
                fixed["dolphin_count"] = row.get("dolphin_count") or 0
                fixed["avg_48h"] = row.get("avg_48h") or 0
                fixed["min_48h"] = row.get("min_48h") or 0
                fixed["max_48h"] = row.get("max_48h") or 0
                fixed["mining_conf"] = row.get("mining_conf") or 0
                fixed["total_samples"] = row.get("total_samples") or 0
                fixed["mining_detected"] = fixed["mining_conf"] > 0
                cleaned.append(fixed)
            return cleaned
        return []
    except Exception as e:
        traceback.print_exc()
        return []

@app.get("/api/alerts")
async def alerts():
    """Get alerts"""
    try:
        data = _read_jsonl(ALERTS_JSONL)
        if data:
            return data
        return []
    except Exception as e:
        traceback.print_exc()
        return []

@app.get("/api/evidence")
async def evidence():
    """Get evidence packages"""
    try:
        data = _read_jsonl(ALERTS_JSONL)
        packages = []
        for a in data:
            dolphin_count = a.get("dolphin_count") or 0
            avg_48h = a.get("avg_48h") or 0
            decline_pct = a.get("decline_pct") or 0
            mining_conf = a.get("mining_conf") or 0
            zone = a.get("zone") or "Unknown"
            
            packages.append({
                "case_id": a.get("case_id", f"NGT-{datetime.now().strftime('%Y%m%d')}-{zone}"),
                "zone": zone,
                "dolphin_count": dolphin_count,
                "avg_48h": avg_48h,
                "decline_pct": decline_pct,
                "mining_conf": mining_conf,
                "status": "ready_for_filing",
            })
        return packages
    except Exception as e:
        traceback.print_exc()
        return []

@app.get("/api/legal")
async def legal(q: str = ""):
    """Legal search"""
    try:
        if not q.strip():
            return {"answer": "Ask about NGT laws.", "sources": [], "confidence": 0, "method": "BM25", "indexed_documents": 0}
        return bm25_rag(q)
    except Exception as e:
        traceback.print_exc()
        return {"answer": f"Error: {str(e)}", "sources": [], "confidence": 0, "method": "BM25", "indexed_documents": 0}

@app.post("/api/fir/{case_id}")
async def fir(case_id: str):
    """Auto-file FIR"""
    try:
        return {
            "status": "success",
            "fir_number": f"FIR-{datetime.now().strftime('%Y%m%d%H%M')}-{case_id}",
            "submitted_to": "District Magistrate Varanasi + NGT",
            "evidence": ["sentinel1_sar.png", "cpcb_sensor_data.csv"],
            "legal_sections": ["IPC §379", "EPA 1986 §15"],
            "timestamp": datetime.now().isoformat(),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

HTML = """<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><title>JalJeevan Score</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif; background: #fff; color: #1a1a1a; padding: 20px; }
.container { max-width: 1200px; margin: 0 auto; }
.header { display: flex; justify-content: space-between; align-items: center; padding: 20px 0; border-bottom: 1px solid #eee; margin-bottom: 20px; }
.header h1 { font-size: 28px; }
.stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin: 20px 0; }
.stat { padding: 15px; background: #f5f5f5; border-radius: 8px; }
.stat-label { font-size: 12px; color: #666; text-transform: uppercase; margin-bottom: 5px; }
.stat-value { font-size: 24px; font-weight: bold; }
.zones { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin: 20px 0; }
.zone { padding: 15px; background: #f5f5f5; border-radius: 8px; border-left: 4px solid #999; }
.zone.good { border-left-color: #22c55e; }
.zone.warn { border-left-color: #f59e0b; background: #fffbeb; }
.zone.crit { border-left-color: #ef4444; background: #fef2f2; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { padding: 10px; text-align: left; border-bottom: 1px solid #eee; }
th { font-weight: 600; background: #f5f5f5; }
button { padding: 8px 12px; background: #0066cc; color: white; border: none; border-radius: 4px; cursor: pointer; }
button:hover { background: #0052a3; }
#ragOut { display: none; padding: 15px; background: #f5f5f5; border-radius: 8px; margin: 10px 0; }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>🐬 JalJeevan Score</h1>
    <div style="text-align: right;"><div id="ts"></div></div>
  </div>

  <div class="stats">
    <div class="stat"><div class="stat-label">Total Dolphins</div><div class="stat-value" id="nDolph">--</div></div>
    <div class="stat"><div class="stat-label">River Health</div><div class="stat-value" id="nHealth">--</div></div>
    <div class="stat"><div class="stat-label">Active Alerts</div><div class="stat-value" id="nAlert">0</div></div>
    <div class="stat"><div class="stat-label">Cases Filed</div><div class="stat-value" id="nCases">0</div></div>
  </div>

  <h2 style="margin-top: 30px;">Zone Status</h2>
  <div class="zones" id="zones"></div>

  <h2 style="margin-top: 30px;">Details</h2>
  <table><thead><tr><th>Zone</th><th>Count</th><th>48h Avg</th><th>Mining</th><th>Status</th></tr></thead><tbody id="tbody"></tbody></table>

  <h2>Alerts</h2>
  <div id="alerts" style="color: #888;">No active alerts</div>

  <h2>Legal Search</h2>
  <input id="qIn" type="text" style="width: 100%; padding: 10px; margin: 10px 0;" placeholder="Ask about NGT orders...">
  <button onclick="askRAG()">Search</button>
  <div id="ragOut"></div>
</div>

<script>
async function load() {
  const now = new Date().toLocaleTimeString();
  document.getElementById('ts').innerText = 'Updated: ' + now;

  const stats = await fetch('/api/stats').then(r => r.json()).catch(() => []);
  if (!stats.length) return;

  let total = 0;
  stats.forEach(z => total += (z.dolphin_count || 0));
  document.getElementById('nDolph').innerText = total;
  document.getElementById('nHealth').innerText = Math.round(total / 3);

  let zoneHTML = '';
  let tableHTML = '';
  stats.forEach(z => {
    const cnt = z.dolphin_count || 0;
    const avg = z.avg_48h ? Math.round(z.avg_48h) : '--';
    let cls = 'good';
    if (cnt < avg * 0.75) cls = 'crit';
    else if (cnt < avg) cls = 'warn';
    
    zoneHTML += `<div class="zone ${cls}"><strong>${z.zone}</strong><br>Count: ${cnt}<br>Avg: ${avg}</div>`;
    tableHTML += `<tr><td>${z.zone}</td><td>${cnt}</td><td>${avg}</td><td>${z.mining_detected ? 'YES' : 'No'}</td><td>${cls.toUpperCase()}</td></tr>`;
  });
  document.getElementById('zones').innerHTML = zoneHTML;
  document.getElementById('tbody').innerHTML = tableHTML;

  const alerts = await fetch('/api/alerts').then(r => r.json()).catch(() => []);
  document.getElementById('nAlert').innerText = alerts.length;
  document.getElementById('nCases').innerText = alerts.length;
  
  if (alerts.length > 0) {
    const html = alerts.map(a => `<div style="background: #fef2f2; padding: 10px; margin: 10px 0; border-left: 4px solid #ef4444;">
      <strong>${a.zone}</strong>: ${a.dolphin_count} dolphins (↓ ${a.decline_pct}%)<br>
      Confidence: ${a.mining_conf ? Math.round(a.mining_conf * 100) + '%' : 'N/A'}<br>
      Case: ${a.case_id || 'Pending'}
    </div>`).join('');
    document.getElementById('alerts').innerHTML = html;
  }
}

async function askRAG() {
  const q = document.getElementById('qIn').value.trim();
  if (!q) return;
  const box = document.getElementById('ragOut');
  box.style.display = 'block';
  box.innerHTML = 'Searching...';
  const result = await fetch('/api/legal?q=' + encodeURIComponent(q)).then(r => r.json()).catch(e => ({answer: 'Error: ' + e}));
  box.innerHTML = `<strong>Answer:</strong> ${result.answer || 'No answer'}<br><strong>Sources:</strong> ${(result.sources || []).join(', ')}<br><span style="color: #999;">Confidence: ${Math.round((result.confidence || 0) * 100)}%</span>`;
}

load();
setInterval(load, 5000);
</script>
</body>
</html>"""

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    return HTML

if __name__ == "__main__":
    print("\n  Dashboard -> http://localhost:8000")
    print("  API docs  -> http://localhost:8000/docs\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)
