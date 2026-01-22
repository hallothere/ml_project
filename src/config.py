# src/config.py

"""
config.py

Shared configuration constants for the Expedia Hotel Recommendations project.

Purpose:
- Keep experiments comparable across notebooks/models by standardizing:
  - random seed
  - train/validation split size
  - top-k for MAP@K
  - project-level flags (e.g., booking-only framing)

Usage:
    from src.config import RANDOM_SEED, TEST_SIZE, TOP_K
"""


RANDOM_SEED = 42
TEST_SIZE = 0.25
TOP_K = 5

# modeling defaults
N_JOBS = -1
STRATIFY_SPLIT = True

# project flags
BOOKING_ONLY = True
