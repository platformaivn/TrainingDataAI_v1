from pathlib import Path
from config import DATA_DIR


def preprocess(input_path: Path, output_path: Path) -> None:
    """Basic preprocessing: read, clean, and save a sample."""
    raw = input_path.read_bytes()
    # TODO: add domain-specific preprocessing steps
    output_path.write_bytes(raw)


def run():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    files = list(DATA_DIR.iterdir())
    print(f"Preprocessing {len(files)} files in {DATA_DIR}")
    for f in files:
        if f.is_file():
            preprocess(f, f)  # in-place by default
    print("Preprocessing done.")


if __name__ == "__main__":
    run()
