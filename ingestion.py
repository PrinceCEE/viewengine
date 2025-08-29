import os


def load_files(path: str):
    fileExists = os.path.exists(path)
    if not fileExists:
        raise FileNotFoundError(f"file not found: {path}")
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()
