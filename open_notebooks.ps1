Param(
    [string[]]$Notebooks
)

# Activate portable venv if present
$venvActivate = Join-Path (Get-Location) ".venv_portable\Scripts\Activate.ps1"
if (Test-Path $venvActivate) {
    Write-Host "Activating .venv_portable..."
    . $venvActivate
} else {
    Write-Host ".venv_portable not found; continuing with system Python." -ForegroundColor Yellow
}

if (-not $Notebooks -or $Notebooks.Count -eq 0) {
    Write-Host "Starting Jupyter Notebook in repo root..."
    jupyter notebook
    exit $LASTEXITCODE
}

# If specific notebooks were passed, open each one (the first command will start the server)
foreach ($nb in $Notebooks) {
    if (-not (Test-Path $nb)) {
        Write-Host "Notebook not found: $nb" -ForegroundColor Yellow
        continue
    }
    Write-Host "Opening notebook: $nb"
    jupyter notebook "$nb"
}
