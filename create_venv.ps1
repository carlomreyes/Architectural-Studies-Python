Param(
    [switch]$InstallDeps,
    [switch]$RunExamples
)

function Find-PythonExe {
    $py = Get-Command python -ErrorAction SilentlyContinue
    if ($py) { return $py.Source }
    $py = Get-Command py -ErrorAction SilentlyContinue
    if ($py) { return $py.Source }
    return $null
}

$pythonExe = Find-PythonExe
if (-not $pythonExe) {
    Write-Host "Python not found in PATH. Please install Python from https://www.python.org/ and ensure 'python' is on PATH." -ForegroundColor Yellow
    exit 1
}

Write-Host "Using Python: $pythonExe"

# Create venv
& $pythonExe -m venv .venv
if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed to create virtual environment." -ForegroundColor Red
    exit $LASTEXITCODE
}

$activateScript = Join-Path (Get-Location) ".venv\Scripts\Activate.ps1"
if (Test-Path $activateScript) {
    Write-Host "Activating virtual environment in this session..."
    . $activateScript
} else {
    Write-Host "Activation script not found at $activateScript" -ForegroundColor Yellow
}

if ($InstallDeps) {
    if (-not (Test-Path "requirements.txt")) {
        Write-Host "requirements.txt not found, skipping install." -ForegroundColor Yellow
    } else {
        Write-Host "Installing dependencies from requirements.txt..."
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        if ($LASTEXITCODE -ne 0) {
            Write-Host "Dependency installation failed." -ForegroundColor Red
            exit $LASTEXITCODE
        }
    }
}

if ($RunExamples) {
    if (-not (Test-Path "run_examples.py")) {
        Write-Host "run_examples.py not found, skipping run." -ForegroundColor Yellow
    } else {
        Write-Host "Running run_examples.py..."
        python run_examples.py
        if ($LASTEXITCODE -ne 0) {
            Write-Host "Running examples failed (see errors above)." -ForegroundColor Red
            exit $LASTEXITCODE
        }
    }
}

Write-Host "create_venv.ps1 finished. To activate the venv in a new session: .\\.venv\\Scripts\\Activate.ps1"
