from pathlib import Path


def get_input_path(file: str) -> Path:

    data_file = file.rstrip(".py") + ".txt"
    return Path(file).parent / f"data/{data_file}"
