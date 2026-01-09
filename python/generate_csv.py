import csv
import math
import os

os.makedirs("data", exist_ok=True)

with open("data/timings.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Algorithm", "n", "t"])

    # BINARY SEARCH -> O(log n)
    for n in [100, 1000, 10000, 100000]:
        t = math.log2(n) * 1.0
        writer.writerow(["BINARY", n, t])

    # LINEAR SEARCH -> O(n)
    for n in [1000, 10000, 100000, 1000000]:
        t = n * 0.01
        writer.writerow(["LINEAR", n, t])

    # MERGE SORT -> O(n log n)
    for n in [1000, 10000, 100000, 1000000]:
        t = n * math.log2(n) * 0.01
        writer.writerow(["MERGE", n, t])

    # BUBBLE SORT -> O(n^2)
    for n in [10, 50, 100, 500, 1000]:
        t = n**2 * 0.001
        writer.writerow(["BUBBLE", n, t])

print("CSV generated at data/timings.csv")
