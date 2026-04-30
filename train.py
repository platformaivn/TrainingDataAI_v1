import os
import json
from pathlib import Path
from config import DATA_DIR, MODEL_DIR, EPOCHS, BATCH_SIZE, LEARNING_RATE


def load_samples(data_dir: Path):
    """Load all training samples from the data directory."""
    samples = [p for p in data_dir.iterdir() if p.is_file()]
    print(f"Found {len(samples)} training samples")
    return samples


def train(config: dict | None = None):
    """Run the training loop."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    samples = load_samples(DATA_DIR)
    if not samples:
        print("No training samples found in data/")
        return

    for epoch in range(1, EPOCHS + 1):
        # TODO: implement actual training logic
        loss = 0.0
        print(f"Epoch {epoch}/{EPOCHS}  loss={loss:.4f}")

    print("Training complete.")


if __name__ == "__main__":
    train()
