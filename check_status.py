import os
import json
from datetime import datetime

print("\n🔍 JALJEEVAN SCORE — SYSTEM CHECK\n")

# Check Pathway
try:
    import pathway as pw
    _ = pw.this   # raises AttributeError on the stub/placeholder package
    print(f"✅ Pathway (real): installed")
except AttributeError:
    print("⚠️  Pathway stub installed — real binary requires Linux/WSL (simulation mode active)")
except ImportError:
    print("❌ Pathway NOT installed")

# Check other key deps
print("\n📦 OTHER DEPENDENCIES:")
for pkg in ["fastapi", "uvicorn", "pandas", "jinja2", "numpy"]:
    try:
        mod = __import__(pkg)
        ver = getattr(mod, "__version__", "?")
        print(f"  ✅ {pkg}: {ver}")
    except ImportError:
        print(f"  ❌ {pkg}: MISSING")

# Check data files
print("\n📁 DATA FILES:")
for file in ["data/live_dolphin.csv", "data/live_mining.csv"]:
    if os.path.exists(file):
        size = os.path.getsize(file)
        mod = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%H:%M:%S')
        print(f"  ✅ {file}: {size} bytes (updated {mod})")
    else:
        print(f"  ❌ {file}: MISSING")

# Check NGT orders
print("\n📚 LEGAL DOCUMENTS:")
ngt_files = os.listdir("data/ngt_orders/") if os.path.exists("data/ngt_orders/") else []
for f in ngt_files:
    size = os.path.getsize(f"data/ngt_orders/{f}")
    print(f"  ✅ {f}: {size} bytes")
if not ngt_files:
    print("  ❌ No legal documents found")

# Show first 5 lines of dolphin CSV
print("\n📋 DOLPHIN CSV PREVIEW (first 5 lines):")
try:
    with open("data/live_dolphin.csv") as f:
        for i, line in enumerate(f):
            if i >= 5:
                break
            print(f"  {line.rstrip()}")
except:
    print("  ❌ Could not read file")

# Check output
print("\n📤 OUTPUT FILES:")
if os.path.exists("output/"):
    files = os.listdir("output/")
    if files:
        for fn in files:
            size = os.path.getsize(f"output/{fn}")
            print(f"  ✅ {fn}: {size} bytes")
    else:
        print("  ⚠️  output/ folder is empty")
else:
    print("  ❌ output/ folder missing")

# Check pipeline/app processes (Windows-compatible)
print("\n🔄 PROCESS CHECK:")
import subprocess
try:
    result = subprocess.run(
        ["tasklist", "/FI", "IMAGENAME eq python.exe", "/FO", "CSV"],
        capture_output=True, text=True
    )
    if "python.exe" in result.stdout:
        lines = [l for l in result.stdout.strip().splitlines() if "python.exe" in l]
        print(f"  ✅ {len(lines)} Python process(es) running")
    else:
        print("  ℹ️  No Python processes detected")
except:
    print("  ⚠️  Could not check processes")

print("\n" + "="*45)
print("➡️  Run 'python app.py' → open http://localhost:8000")
print("="*45 + "\n")
