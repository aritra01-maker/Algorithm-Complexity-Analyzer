import numpy as np

def constant(n):
    return np.ones_like(n)

def logn(n):
    return np.log(n)

def linear(n):
    return n

def nlogn(n):
    return n * np.log(n)

def quadratic(n):
    return n ** 2

models = {
    "O(1)": constant,
    "O(log n)": logn,
    "O(n)": linear,
    "O(n log n)": nlogn,
    "O(n^2)": quadratic
}
