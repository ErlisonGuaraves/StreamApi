import json
import os

def load_queries():
    
    diretorio = os.path.join('shared', 'config', 'queries.json')

    try:
        with open(diretorio, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found at {diretorio}")
    except Exception as e:
        raise Exception(f"An error occurred while loading queries: {str(e)}")

queries = load_queries()
