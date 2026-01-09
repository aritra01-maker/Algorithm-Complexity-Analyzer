import csv
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
import os
from complexity_model import models
from fit_model import fit_model

os.makedirs("plots", exist_ok=True)

# Read CSV
data = defaultdict(lambda: ([], []))
with open("data/timings.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for algo, n, t in reader:
        data[algo][0].append(int(n))
        data[algo][1].append(float(t))

# Classify
for algo in data:
    ns, ts = data[algo]
    ns = np.array(ns)
    ts = np.array(ts)
    
    errors = {}
    fitted_curves = {}

    for name, f in models.items():
        error = fit_model(ns, ts, f)
        errors[name] = error

        # compute curve for plotting
        f_values = f(ns)
        fitted_curves[name] = f_values

    best = min(errors, key=errors.get)
    print(f"{algo.upper()} -> {best}")

    # Plot
    plt.figure(figsize=(6,4))
    plt.scatter(ns, ts, color='red', label="Actual Data")
    for name, curve in fitted_curves.items():
        plt.plot(ns, curve, label=name)
    plt.title(f"Algorithm: {algo.upper()} -> Best Fit: {best}")
    plt.xlabel("Input size n")
    plt.ylabel("Runtime t")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"plots/{algo}_fit.png", dpi=300)
    plt.show()
    plt.close()
