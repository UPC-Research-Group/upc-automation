
# Metadata validator example script

import json, sys
from pathlib import Path

def validate(path):
    data = json.loads(Path(path).read_text())
    req = ["title", "abstract", "keywords", "version", "license"]
    missing = [k for k in req if k not in data]
    if missing:
        print("Missing:", missing)
        sys.exit(1)
    print("Valid metadata.")

if __name__ == "__main__":
    validate(sys.argv[1])
