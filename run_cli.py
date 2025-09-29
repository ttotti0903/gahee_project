
import json, sys
import calc_core

def main():
    if len(sys.argv) < 3:
        print("Usage: python run_cli.py <sheet_func> <inputs_json>")
        print("Example: python run_cli.py compute_horizontal_pipeline \"{'B3': 1.2, 'C5': 0.8}\"")
        sys.exit(1)
    fn = getattr(calc_core, sys.argv[1])
    inputs = json.loads(sys.argv[2])
    out = fn(inputs)
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
