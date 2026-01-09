import numpy as np

def constant(n):
    n = np.array(n, dtype=float)
    return np.ones_like(n)

def logn(n):
    n = np.array(n, dtype=float)
    return np.log(n + 1)

def linear(n):
    n = np.array(n, dtype=float)
    return n

def nlogn(n):
    n = np.array(n, dtype=float)
    return n * np.log(n + 1)

def quadratic(n):
    n = np.array(n, dtype=float)
    return n**2

models = {
    "O(1)": constant,
    "O(log n)": logn,
    "O(n)": linear,
    "O(n log n)": nlogn,
    "O(n^2)": quadratic
}
