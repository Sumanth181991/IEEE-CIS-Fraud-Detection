from pathlib import Path

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent

# Data Paths
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Model Paths
MODEL_DIR = BASE_DIR / "models"
MODEL_FILE = MODEL_DIR / "fraud_detection_pipeline.pkl"

# Notebook Path
NOTEBOOK_DIR = BASE_DIR / "notebooks"

# Random State
RANDOM_STATE = 42

# Train/Test Split
TEST_SIZE = 0.20

# Target Column
TARGET_COLUMN = "isFraud"

# Primary Key
PRIMARY_KEY = "TransactionID"

# Logging
LOG_LEVEL = "INFO"