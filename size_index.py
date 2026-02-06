import numpy as np
import matplotlib.pyplot as plt

size = []
avg_index = []

with open("linear_search_analysis.txt") as f:
    next(f)
    for line in f:
        s, _, _, _, idx = line.split()
        size.append(int(s))
        avg_index.append(float(idx))

size = np.array(size)
avg_index = np.array(avg_index)

plt.figure(figsize=(10,6))
plt.plot(size, avg_index, color="purple", linewidth=2)

plt.xlabel("Array Size (n)")
plt.ylabel("Average Index Found")
plt.title("Linear Search: Average Index Found vs Array Size")
plt.grid(True)
plt.tight_layout()
plt.show()