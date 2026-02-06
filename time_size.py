import numpy as np
import matplotlib.pyplot as plt

size = []
time = []

with open("linear_search_analysis.txt") as f:
    next(f)  # skip header
    for line in f:
        cols = line.split()

        s = int(cols[0])        # Array size
        t = float(cols[3])     # AvgTime_us or ms (label accordingly)

        size.append(s)
        time.append(t)

size = np.array(size)
time = np.array(time)

# ---------------- SMOOTHING ----------------
window = 50
time_smooth = np.convolve(time, np.ones(window)/window, mode='valid')

# ---------------- O(n) BENCHMARK ----------------
# Scale linear function to last data point
c = time[-1] / size[-1]
on_benchmark = c * size

# ---------------- PLOTTING ----------------
plt.figure(figsize=(10, 6))

# Measured time
plt.plot(size, time, label="Measured Time", linewidth=2)

# Smoothed trend
plt.plot(size[:len(time_smooth)], time_smooth,
         label="Smoothed Trend", linewidth=2, color="green")

# Theoretical O(n)
plt.plot(size, on_benchmark, linestyle="--",
         label="Theoretical O(n)", linewidth=2, color="red")

plt.xlabel("Array Size (n)")
plt.ylabel("Average Time (µs)")
plt.title("Linear Search: Time vs Array Size")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()