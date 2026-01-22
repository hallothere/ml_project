# src/model_utils.py

"""
model_utils.py

Utilities shared across model notebooks.

Currently includes:
- topk_from_proba: converts a probability matrix into top-k ranked class predictions.

Usage:
    from src.model_utils import topk_from_proba
"""

import numpy as np

def topk_from_proba(proba: np.ndarray, classes: np.ndarray, k: int = 5):
    """
    Convert predicted probabilities into top-k ranked class predictions per row.
    proba: (n_samples, n_classes)
    classes: (n_classes,)
    returns: list of arrays, each length k
    """
    return [classes[np.argsort(row)[-k:][::-1]] for row in proba]
