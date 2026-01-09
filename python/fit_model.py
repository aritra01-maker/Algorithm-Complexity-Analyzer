import numpy as np

def fit_model(ns, ts, f):
    """
    Instead of scaling via least squares, compute growth ratios
    and compare to expected ratios for each candidate function.
    Returns a measure of mismatch (lower is better).
    """
    ns = np.array(ns, dtype=float)
    ts = np.array(ts, dtype=float)
    f_values = f(ns)

    # Compute observed ratios
    obs_ratios = ts[1:] / ts[:-1]
    expected_ratios = f_values[1:] / f_values[:-1]

    # Avoid division by zero
    expected_ratios = np.maximum(expected_ratios, 1e-8)

    # Compute error as sum of squared relative differences
    error = np.sum(((obs_ratios - expected_ratios) / expected_ratios) ** 2)
    return error

