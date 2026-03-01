# JalJeevan Score — Demo Launch Script (PowerShell)
# This starts the entire application in PowerShell terminals

Write-Host ""
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  🐬 JalJeevan Score — DEMO LAUNCHER (Windows)" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

# Check Python installation
$pythonCheck = python --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Python not found. Please install Python 3.8+" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Python found: $pythonCheck" -ForegroundColor Green
Write-Host ""

# Check if virtual environment exists
if (-Not (Test-Path ".\.venv")) {
    Write-Host "⚠️  Virtual environment not found. Creating..." -ForegroundColor Yellow
    python -m venv .venv
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\.venv\Scripts\Activate.ps1

# Install dependencies
Write-Host "Checking dependencies..." -ForegroundColor Yellow
pip install -q pathway fastapi uvicorn pandas numpy jinja2 python-multipart

Write-Host ""
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  Starting JalJeevan Score Components" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "📋 MANUAL STARTUP INSTRUCTIONS:" -ForegroundColor Cyan
Write-Host ""
Write-Host "Open 3 PowerShell windows (or use VS Code Terminal):" -ForegroundColor White
Write-Host ""

Write-Host "Terminal 1 - Start Pipeline:" -ForegroundColor Yellow
Write-Host "  cd d:\websites\Jaljeevan" -ForegroundColor Gray
Write-Host "  . .\.venv\Scripts\Activate.ps1" -ForegroundColor Gray
Write-Host "  python pipeline.py" -ForegroundColor Gray
Write-Host ""

Write-Host "Terminal 2 - Start API Server:" -ForegroundColor Yellow
Write-Host "  cd d:\websites\Jaljeevan" -ForegroundColor Gray
Write-Host "  . .\.venv\Scripts\Activate.ps1" -ForegroundColor Gray
Write-Host "  python app.py" -ForegroundColor Gray
Write-Host ""

Write-Host "Terminal 3 (Optional) - Start Simulator:" -ForegroundColor Yellow
Write-Host "  cd d:\websites\Jaljeevan" -ForegroundColor Gray
Write-Host "  . .\.venv\Scripts\Activate.ps1" -ForegroundColor Gray
Write-Host "  python simulator.py" -ForegroundColor Gray
Write-Host ""

Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  📊 Dashboard & API Endpoints" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  🌐 Full Dashboard:  http://localhost:8000" -ForegroundColor Cyan
Write-Host "  📊 Get Stats:       http://localhost:8000/api/stats" -ForegroundColor Cyan
Write-Host "  🚨 Get Alerts:      http://localhost:8000/api/alerts" -ForegroundColor Cyan
Write-Host "  📋 Get Evidence:    http://localhost:8000/api/evidence" -ForegroundColor Cyan
Write-Host "  ⚖️  Legal Search:   http://localhost:8000/api/legal?q=sand+mining" -ForegroundColor Cyan
Write-Host "  📚 API Docs:        http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Press any key to continue..." -ForegroundColor White
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
