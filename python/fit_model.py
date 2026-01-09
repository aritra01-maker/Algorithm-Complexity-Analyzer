import numpy as np

def fit_model(ns, ts, f):
    ns = np.array(ns)
    ts = np.array(ts)
    
    # Scale factor 'a' using least squares
    f_values = f(ns)
    a = np.sum(ts * f_values) / np.sum(f_values ** 2)
    
    # Compute squared error
    error = np.sum((ts - a * f_values) ** 2)
    return error

