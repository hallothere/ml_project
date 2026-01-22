# src/metrics.py

"""
metrics.py

Shared evaluation metrics for the Expedia project.

Primary metric:
- MAP@K (Mean Average Precision at K), aligned with Kaggle scoring.

Secondary diagnostics (optional):
- Hit Rate@K: whether the true label appears anywhere in the top-k list.

Usage:
    from src.metrics import mapk, hit_rate_at_k
"""
import numpy as np

def mapk(y_true, y_pred, k=5) -> float:
    """
    Mean Average Precision at k for single-label ground truth.
    y_true: iterable of true labels
    y_pred: iterable of ranked lists/arrays of predicted labels
    """
    scores = []
    for true, pred in zip(y_true, y_pred):
        pred = list(pred)[:k]
        if true in pred:
            scores.append(1.0 / (pred.index(true) + 1))
        else:
            scores.append(0.0)
    return float(np.mean(scores))

def hit_rate_at_k(y_true, y_pred, k=5) -> float:
    """Share of samples where true label appears in top-k predictions."""
    hits = [1 if t in list(p)[:k] else 0 for t, p in zip(y_true, y_pred)]
    return float(np.mean(hits))
