#CLASSIFICATION ENGINE
import csv
from collections import defaultdict
from complexity_models import models
from fit_model import fit_model

data = defaultdict(lambda: ([], []))

with open("../data/timings.csv") as f:
    reader = csv.reader(f)
    for algo, n, t in reader:
        data[algo][0].append(int(n))
        data[algo][1].append(float(t))

for algo in data:
    ns, ts = data[algo]
    errors = {}

    for name, f in models.items():
        errors[name] = fit_model(ns, ts, f)

    best = min(errors, key=errors.get)
    print(f"{algo.upper()} -> {best}")
