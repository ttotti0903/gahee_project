
# Concrete Pumping Calculator — No Excel (Transpiled)

This version **does not require Excel**. It transpiles formulas from your workbook into pure Python
and provides:
- `calc_core.py` — generated compute functions per sheet
- `app_noxl.py` — GUI (PySide6) with two tabs
- `run_cli.py` — CLI to test

## Install (dev)
```
pip install -r requirements_noxl.txt
python app_noxl.py
```

## Build EXE (on Windows)
```
pyinstaller --noconsole --onefile --name ConcretePumping_NoExcel app_noxl.py
```

Then distribute the EXE alone.

## Notes
- Supported Excel functions: + - * / ^, IF, SUM, AVERAGE, MIN, MAX, ABS, SQRT, POWER, EXP,
  LN/LOG, LOG10, SIN, COS, TAN, PI(), RADIANS, DEGREES, comparisons.
- If the workbook uses other functions, add mapping in the generator.
