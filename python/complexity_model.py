import math

def constant(n): return 1
def logn(n): return math.log(n)
def linear(n): return n
def nlogn(n): return n * math.log(n)
def quadratic(n): return n * n

models = {
    "O(1)": constant,
    "O(log n)": logn,
    "O(n)": linear,
    "O(n log n)": nlogn,
    "O(n^2)": quadratic
}
