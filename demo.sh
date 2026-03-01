#!/usr/bin/env bash
# JalJeevan Score — Demo Launch Script
# This starts the entire application in multiple terminals

echo ""
echo "========================================================"
echo "  🐬 JalJeevan Score — DEMO LAUNCHER"
echo "========================================================"
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8+"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "⚠️  Virtual environment not found. Creating..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "Checking dependencies..."
pip install -q pathway fastapi uvicorn pandas numpy jinja2 python-multipart

echo ""
echo "========================================================"
echo "  Starting JalJeevan Score Components"
echo "========================================================"
echo ""

# Check if we're on macOS, Linux, or other
OS="$(uname -s)"

if [ "$OS" = "Darwin" ]; then
    echo "🍎 macOS detected — using open command"
    echo ""
    echo "Terminal 1: Starting Pipeline..."
    open -a Terminal
    echo "  Run: python pipeline.py"
    echo ""
    echo "Terminal 2: Starting API Server..."
    open -a Terminal
    echo "  Run: python app.py"
    echo ""
    echo "Terminal 3: (Optional) Simulator for live updates..."
    open -a Terminal
    echo "  Run: python simulator.py"
    echo ""
    echo "Then visit: http://localhost:8000"

elif [ "$OS" = "Linux" ]; then
    echo "🐧 Linux detected"
    echo ""
    
    # Check for available terminal emulators
    if command -v gnome-terminal &> /dev/null; then
        echo "Terminal 1: Starting Pipeline..."
        gnome-terminal -- bash -c "source .venv/bin/activate; python pipeline.py; bash"
        sleep 2
        
        echo "Terminal 2: Starting API Server..."
        gnome-terminal -- bash -c "source .venv/bin/activate; python app.py; bash"
        sleep 2
        
        echo "Terminal 3: (Optional) Simulator..."
        gnome-terminal -- bash -c "source .venv/bin/activate; python simulator.py; bash"
        
        echo ""
        echo "✅ All terminals started!"
        echo "   Visit: http://localhost:8000"
        
    elif command -v xterm &> /dev/null; then
        echo "Using xterm..."
        xterm -e "source .venv/bin/activate; python pipeline.py" &
        sleep 2
        xterm -e "source .venv/bin/activate; python app.py" &
        sleep 2
        xterm -e "source .venv/bin/activate; python simulator.py" &
        
    else
        echo "⚠️  No terminal emulator found. Please run manually:"
        echo ""
        echo "  Terminal 1: python pipeline.py"
        echo "  Terminal 2: python app.py"
        echo "  Terminal 3: python simulator.py (optional)"
    fi
else
    echo "❓ Unknown OS. Please run manually:"
    echo ""
    echo "Terminal 1: python pipeline.py"
    echo "Terminal 2: python app.py"
    echo "Terminal 3: python simulator.py (optional)"
fi

echo ""
echo "========================================================"
echo "  📊 Dashboard Components"
echo "========================================================"
echo ""
echo "  Pipeline:  http://localhost:8000/api/stats"
echo "  Alerts:    http://localhost:8000/api/alerts"
echo "  Evidence:  http://localhost:8000/api/evidence"
echo "  RAG/Legal: http://localhost:8000/api/legal?q=..."
echo "  Dashboard: http://localhost:8000"
echo "  API Docs:  http://localhost:8000/docs"
echo ""
echo "========================================================"
echo ""
