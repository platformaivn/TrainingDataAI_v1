from pathlib import Path

# Directories
DATA_DIR = Path("data")
MODEL_DIR = Path("models")

# Model
MODEL_NAME = "lotus-ai"

# Training hyperparameters
LEARNING_RATE: float = 1e-4
BATCH_SIZE: int = 32
EPOCHS: int = 50

# Data processing
MAX_SEQ_LENGTH: int = 512
NUM_WORKERS: int = 4
VAL_SPLIT: float = 0.1
