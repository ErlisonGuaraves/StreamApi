import json
from pathlib import Path

count_file_path = Path("json/row_count.json")

def save_row_count(count: int):
    try:
        count_file_path.parent.mkdir(parents=True, exist_ok=True) 
        with open(count_file_path, "w") as file:
            json.dump({"count": count}, file)
    except IOError as e:
        print(f"Error saving row count: {e}")



def load_row_count() -> int:
    if not count_file_path.exists():
        return 0
    try:
        with open(count_file_path, "r") as file:
            data = json.load(file)
            return data.get("count", 0)
    except (json.JSONDecodeError, ValueError, IOError) as e:
        print(f"Error loading row count: {e}")
        return 0



def count_rows_updated(last_rows_counted: int = 0, current_rows: int = 0) -> str:
   
    if last_rows_counted < current_rows: return "increased"
    
    elif last_rows_counted > current_rows: return "decreased"
    
    return "no updated"
