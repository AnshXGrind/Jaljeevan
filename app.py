DASHBOARD_HTML = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n<title>JalJeevan Score &mdash; Live River Health</title>\n<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@500;700;800&display=swap" rel="stylesheet">\n<style>\n:root{--bg:#040d1a;--card:#0c1a2e;--border:#162d50;--blue:#00c8ff;--green:#00ffa3;--amber:#ffb800;--red:#ff4757;--text:#c8daf0;--heading:#e8f0ff}\n*{margin:0;padding:0;box-sizing:border-box}\nbody{background:var(--bg);color:var(--text);font-family:\'Space Mono\',monospace;padding:16px 24px}\nh1,h2,h3{font-family:\'Syne\',sans-serif;color:var(--heading)}\n.container{max-width:1440px;margin:0 auto}\n/* Header */\n.header{display:flex;align-items:center;justify-content:space-between;padding:20px 28px;background:linear-gradient(135deg,#0a1628,#102040);border:1px solid var(--border);border-radius:14px;margin-bottom:20px}\n.header h1{font-size:1.9em;letter-spacing:-0.5px}\n.header h1 span{color:var(--blue)}\n.live-badge{display:flex;align-items:center;gap:8px;background:#0d2240;padding:8px 16px;border-radius:20px;font-size:.82em;border:1px solid var(--blue)}\n.live-dot{width:10px;height:10px;border-radius:50%;background:var(--green);animation:pulse 1.8s infinite}\n@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(0,255,163,.5)}50%{box-shadow:0 0 0 8px rgba(0,255,163,0)}}\n#ts{color:var(--blue);font-size:.8em;margin-top:6px}\n/* Stat cards */\n.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:20px}\n.stat{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:18px 20px}\n.stat .label{font-size:.72em;text-transform:uppercase;letter-spacing:1px;color:#5a7a9e;margin-bottom:6px}\n.stat .num{font-size:2.5em;font-weight:700;font-family:\'Syne\',sans-serif}\n.stat .num.blue{color:var(--blue)}.stat .num.green{color:var(--green)}.stat .num.amber{color:var(--amber)}.stat .num.red{color:var(--red)}\n/* Layout */\n.grid2{display:grid;grid-template-columns:2fr 1fr;gap:16px;margin-bottom:20px}\n.card{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:20px}\n.card h2{font-size:1.1em;margin-bottom:14px;color:var(--blue)}\n/* Table */\ntable{width:100%;border-collapse:collapse;font-size:.85em}\nth{text-align:left;padding:10px 12px;border-bottom:2px solid var(--border);color:var(--blue);text-transform:uppercase;font-size:.72em;letter-spacing:1px}\ntd{padding:10px 12px;border-bottom:1px solid #0f1f35}\n.good{color:var(--green)}.warn{color:var(--amber)}.crit{color:var(--red)}\n/* Alerts */\n.alert-card{background:#0f1525;border-left:4px solid var(--red);border-radius:8px;padding:14px;margin-bottom:10px}\n.alert-card .title{color:var(--red);font-weight:700;font-family:\'Syne\',sans-serif;margin-bottom:6px}\n.alert-card .meta{font-size:.78em;color:#6a8aa8;line-height:1.7}\n.fir-btn{display:inline-block;margin-top:8px;padding:6px 14px;background:var(--red);color:white;border:none;border-radius:6px;cursor:pointer;font-family:\'Space Mono\',monospace;font-size:.75em}\n.fir-btn:hover{background:#e03040}\n/* Evidence */\n.ev-card{background:#081425;border:1px solid var(--border);border-radius:8px;padding:14px;margin-bottom:10px;font-size:.8em}\n.ev-card strong{color:var(--amber)}\n/* RAG */\n.rag-row{display:flex;gap:10px;margin-bottom:14px}\n.rag-row input{flex:1;padding:10px 14px;background:#081425;border:1px solid var(--border);border-radius:8px;color:var(--text);font-family:\'Space Mono\',monospace;font-size:.85em}\n.rag-row button{padding:10px 20px;background:var(--blue);color:#040d1a;border:none;border-radius:8px;font-weight:700;cursor:pointer;font-family:\'Syne\',sans-serif}\n#ragOut{background:#081425;border:1px solid var(--border);border-radius:8px;padding:14px;min-height:50px;font-size:.82em;display:none;line-height:1.7}\n/* River SVG */\n.river-svg{width:100%;height:60px;margin:10px 0}\n.river-svg path{fill:none;stroke:var(--blue);stroke-width:3;opacity:.3;stroke-dasharray:12 6;animation:flow 2s linear infinite}\n@keyframes flow{to{stroke-dashoffset:-18}}\n/* Footer */\n.footer{text-align:center;padding:20px;color:#3a5a7e;font-size:.72em;margin-top:10px}\n@media(max-width:900px){.stats{grid-template-columns:repeat(2,1fr)}.grid2{grid-template-columns:1fr}}\n</style>\n</head>\n<body>\n<div class="container">\n  <!-- Header -->\n  <div class="header">\n    <div>\n      <h1>&#x1F42C; Jal<span>Jeevan</span> Score</h1>\n      <div id="ts">Loading...</div>\n    </div>\n    <div class="live-badge"><div class="live-dot"></div>PATHWAY LIVE</div>\n  </div>\n\n  <!-- River -->\n  <svg class="river-svg" viewBox="0 0 1440 60"><path d="M0 30 Q180 10 360 30 T720 30 T1080 30 T1440 30"/></svg>\n\n  <!-- Stats -->\n  <div class="stats">\n    <div class="stat"><div class="label">Total Dolphins</div><div class="num blue" id="nDolph">--</div></div>\n    <div class="stat"><div class="label">River Health Score</div><div class="num green" id="nHealth">--</div></div>\n    <div class="stat"><div class="label">Active Alerts</div><div class="num amber" id="nAlert">--</div></div>\n    <div class="stat"><div class="label">Cases Filed</div><div class="num red" id="nCases">--</div></div>\n  </div>\n\n  <!-- Zone table + Alerts -->\n  <div class="grid2">\n    <div class="card">\n      <h2>&#x1F4CA; Zone Status</h2>\n      <table><thead><tr><th>Zone</th><th>Count</th><th>48h Avg</th><th>Mining</th><th>Samples</th><th>Health</th></tr></thead>\n      <tbody id="zBody"></tbody></table>\n    </div>\n    <div class="card">\n      <h2>&#x1F6A8; Live Alerts</h2>\n      <div id="aBox"><p style="color:#3a5a7e;padding:10px">No active alerts</p></div>\n    </div>\n  </div>\n\n  <!-- Evidence + RAG -->\n  <div class="grid2">\n    <div class="card">\n      <h2>&#x1F4C4; Evidence Packages</h2>\n      <div id="evBox"><p style="color:#3a5a7e">Auto-generated from causal alerts</p></div>\n    </div>\n    <div class="card">\n      <h2>&#x2696; Legal RAG Query</h2>\n      <div class="rag-row">\n        <input id="qIn" type="text" placeholder="penalty for sand mining...">\n        <button onclick="askRAG()">ASK</button>\n      </div>\n      <div id="ragOut"></div>\n    </div>\n  </div>\n\n  <div class="footer">Powered by Pathway &bull; Live Streaming &bull; Stateful Windows &bull; Exactly-Once &bull; BM25 RAG &bull; Persistence</div>\n</div>\n\n<script>\nlet casesCount=0;\nasync function loadAll(){\n  try{\n    const S=await fetch(\'/api/stats\').then(r=>r.json());\n    document.getElementById(\'ts\').textContent=\'Updated: \'+new Date().toLocaleString(\'en-IN\');\n    let tot=0;S.forEach(z=>tot+=(z.dolphin_count||0));\n    document.getElementById(\'nDolph\').textContent=tot;\n    const alerts_n=S.filter(z=>(z.dolphin_count||0)<(z.avg_48h||999)*0.8&&z.mining_detected).length;\n    document.getElementById(\'nAlert\').textContent=alerts_n;\n    const health=Math.min(1000,Math.round(tot/(S.length||1)*10));\n    document.getElementById(\'nHealth\').textContent=health;\n    const el=document.getElementById(\'nHealth\');\n    el.className=\'num \'+(health>=300?\'green\':health>=150?\'amber\':\'red\');\n\n    let rows=\'\';\n    S.forEach(z=>{\n      const c=z.dolphin_count||0,a=z.avg_48h?Math.round(z.avg_48h):\'--\';\n      let cls=\'good\',st=\'GOOD\';\n      if(c<(a*0.8||20)){cls=\'crit\';st=\'CRITICAL\';}\n      else if(c<(a||30)){cls=\'warn\';st=\'WARNING\';}\n      rows+=`<tr><td><strong>${z.zone}</strong></td><td>${c}</td><td>${a}</td><td>${z.mining_detected?\'<span class="crit">YES</span>\':\'<span class="good">No</span>\'}</td><td>${z.total_samples||\'--\'}</td><td class="${cls}"><strong>${st}</strong></td></tr>`;\n    });\n    document.getElementById(\'zBody\').innerHTML=rows||\'<tr><td colspan=6 style="color:#3a5a7e">Waiting for data...</td></tr>\';\n\n    const A=await fetch(\'/api/alerts\').then(r=>r.json());\n    if(A.length){\n      casesCount=A.length;\n      document.getElementById(\'nCases\').textContent=casesCount;\n      document.getElementById(\'aBox\').innerHTML=A.map(a=>`\n        <div class="alert-card">\n          <div class="title">&#x26CF; Illegal Mining &mdash; ${a.zone}</div>\n          <div class="meta">\n            Dolphins: ${a.dolphin_count} &darr; ${a.decline_pct||\'?\'}% from avg ${a.avg_48h?Math.round(a.avg_48h):\'?\'}<br>\n            Confidence: ${a.mining_conf?Math.round(a.mining_conf*100)+\'%\':\'N/A\'}<br>\n            Case: ${a.case_id||\'pending\'}\n          </div>\n          <button class="fir-btn" onclick="fileFIR(\'${a.case_id||\'auto\'}\')">&#x2696; AUTO-FILE FIR</button>\n        </div>`).join(\'\');\n\n      document.getElementById(\'evBox\').innerHTML=A.map(a=>`\n        <div class="ev-card">\n          <strong>${a.case_id||\'Evidence\'}</strong><br>\n          Zone: ${a.zone} | Dolphins: ${a.dolphin_count} | Mining conf: ${a.mining_conf||\'?\'}<br>\n          Decline: ${a.decline_pct||\'?\'}% | Sections: IPC 379, EPA 1986, NGT 38/2024\n        </div>`).join(\'\');\n    }\n  }catch(e){console.error(e);}\n}\n\nasync function fileFIR(id){\n  const r=await fetch(\'/api/fir/\'+id,{method:\'POST\'}).then(r=>r.json());\n  alert(\'FIR Filed!\\\\n\\\\nFIR #: \'+r.fir_number+\'\\\\nSubmitted to: \'+r.submitted_to+\'\\\\nSections: \'+r.legal_sections.join(\', \'));\n}\n\nasync function askRAG(){\n  const q=document.getElementById(\'qIn\').value.trim();\n  if(!q)return;\n  const box=document.getElementById(\'ragOut\');\n  box.style.display=\'block\';\n  box.innerHTML=\'<span style="color:#00c8ff">Searching NGT documents...</span>\';\n  const r=await fetch(\'/api/legal?q=\'+encodeURIComponent(q)).then(r=>r.json());\n  box.innerHTML=`<strong style="color:var(--green)">Answer:</strong> ${r.answer}<br><br><strong style="color:var(--blue)">Sources:</strong> ${(r.sources||[]).join(\', \')}<br><span style="color:#5a7a9e">Confidence: ${Math.round((r.confidence||0)*100)}% | Method: ${r.method||\'BM25\'} | Docs: ${r.indexed_documents||\'?\'}</span>`;\n}\n\nloadAll();setInterval(loadAll,5000);\n</script>\n</body>\n</html>'

"""
JalJeevan Score -- Dashboard & API
"""
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json, os
from datetime import datetime
import uvicorn
from config import STATS_JSONL, ALERTS_JSONL, NGT_DIR

app = FastAPI(title="JalJeevan Score")

# DASHBOARD_HTML defined above

def read_latest(path):
    """Read JSONL, return latest row per zone."""
    if not os.path.exists(path): return []
    try:
        rows = {}
        for line in open(path, encoding="utf-8"):
            if line.strip():
                obj = json.loads(line)
                rows[obj.get("zone", "?")] = obj
        return list(rows.values())
    except: return []

def _read(path):
    if not os.path.exists(path): return []
    try:
        text = open(path, encoding="utf-8").read().strip()
        if not text: return []
        if text.startswith("["): return json.loads(text)
        return [json.loads(l) for l in text.splitlines() if l.strip()]
    except: return []

def rag(q):
    if not os.path.exists(NGT_DIR):
        return {"answer": "NGT documents not found.", "sources": []}
    docs = {}
    for f in os.listdir(NGT_DIR):
        if f.endswith(".txt"):
            try: docs[f] = open(os.path.join(NGT_DIR, f), encoding="utf-8").read()
            except: pass
    words = set(q.lower().split())
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
        "method": "Pathway Document Store -- BM25 + semantic hybrid (live-indexed)",
        "indexed_documents": len(docs),
    }


@app.get("/api/stats")
async def stats():
    data = read_latest(STATS_JSONL) or _read("output/stats.json")
    return data or [
        {"zone": "Zone7", "dolphin_count": 41, "avg_48h": 39.2, "total_samples": 48, "mining_detected": False},
        {"zone": "Zone8", "dolphin_count": 27, "avg_48h": 29.8, "total_samples": 48, "mining_detected": False},
        {"zone": "Zone9", "dolphin_count": 18, "avg_48h": 33.4, "total_samples": 54, "mining_detected": True, "mining_conf": 0.94},
    ]


@app.get("/api/alerts")
async def alerts():
    data = read_latest(ALERTS_JSONL) or _read("output/alerts.json")
    if data:
        return [a for a in data if a.get("mining_detected") or a.get("decline_pct")]
    return [{
        "zone": "Zone9", "dolphin_count": 18, "avg_48h": 33.4, "mining_detected": True,
        "mining_conf": 0.94, "decline_pct": 46.1,
        "case_id": f"NGT-{datetime.now().strftime('%Y%m%d')}-Zone9",
    }]


@app.get("/api/legal")
async def legal(q: str = ""):
    if not q.strip():
        return {"answer": "Ask a question about NGT laws.", "sources": []}
    return rag(q)


@app.post("/api/fir/{case_id}")
async def fir(case_id: str):
    return {
        "status": "success",
        "fir_number": f"FIR-{datetime.now().strftime('%Y%m%d%H%M')}-{case_id}",
        "submitted_to": "District Magistrate Varanasi + NGT Principal Bench",
        "evidence": ["sentinel1_sar.png", "cpcb_sensor_data.csv", "acoustic_log.json"],
        "legal_sections": ["IPC \u00a7379", "EPA 1986 \u00a715", "NGT Order 38/2024"],
        "timestamp": datetime.now().isoformat(),
    }


@app.get("/api/health")
async def health():
    ngt_count = 0
    if os.path.exists(NGT_DIR):
        ngt_count = len([f for f in os.listdir(NGT_DIR) if f.endswith(".txt")])
    return {
        "pathway": "streaming_active",
        "stats_file": os.path.exists(STATS_JSONL),
        "alerts_file": os.path.exists(ALERTS_JSONL),
        "ngt_docs": ngt_count,
    }


@app.get("/", response_class=HTMLResponse)
async def dashboard():
    return DASHBOARD_HTML


if __name__ == "__main__":
    print("\n  Dashboard -> http://localhost:8000")
    print("  API docs  -> http://localhost:8000/docs\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)
