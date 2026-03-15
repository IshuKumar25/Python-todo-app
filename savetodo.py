import json
import os
FILENAME = "tasks.json"
        
def save_tasks():
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)
        
def load_tasks():
    global tasks
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            tasks.extend(json.load(f))