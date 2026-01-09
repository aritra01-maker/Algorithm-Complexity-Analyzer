import csv
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
from complexity_model import models
from fit_model import fit_model

data = defaultdict(lambda: ([], []))

# Read CSV
with open("../data/timings.csv") as f:
    reader = csv.reader(f)
    for algo, n, t in reader:
        data[algo][0].append(int(n))
        data[algo][1].append(float(t))

# Classify each algorithm
for algo in data:
    ns, ts = data[algo]
    ns = np.array(ns)
    ts = np.array(ts)
    
    errors = {}
    fitted_curves = {}
    
    for name, f in models.items():
        error = fit_model(ns, ts, f)
        errors[name] = error
        
        # Compute scaled model for plotting
        scale = np.sum(ts * f(ns)) / np.sum(f(ns) ** 2)
        fitted_curves[name] = scale * f(ns)
    
    best = min(errors, key=errors.get)
    print(f"{algo.upper()} -> {best}")
    
    # Plot actual vs models
    plt.figure(figsize=(6,4))
    plt.scatter(ns, ts, color='red', label="Actual Data")
    
    for name, curve in fitted_curves.items():
        plt.plot(ns, curve, label=name)
    
    plt.title(f"Algorithm: {algo.upper()} -> Best Fit: {best}")
    plt.xlabel("Input size n")
    plt.ylabel("Runtime t")
    plt.legend()
    plt.grid(True)
    plt.show()

