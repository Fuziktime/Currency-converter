import json
import os

FILE = "history.json"

def save_history(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_history():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)