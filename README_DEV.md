Developer setup (Windows PowerShell)

1. Create and activate a venv:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If `python` is not found, install Python from https://www.python.org/ and ensure it's added to PATH.

2. Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Run all example scripts:

```powershell
python run_examples.py
```

4. Start Jupyter:

```powershell
jupyter notebook
```

Notes:
- The repository includes `utils/A_Geometry_Helpers/geometry_helpers.py` for helper functions.
- If you want a different venv name, update the paths accordingly.
