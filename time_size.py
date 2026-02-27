import matplotlib.pyplot as plt

size = []
time = []

with open("dataset-2.txt") as f:
    next(f)  # skip header
    for line in f:
        cols = line.split()

        s = int(cols[0])        # Array size
        t = float(cols[3])     # AvgTime_us or ms (label accordingly)

        size.append(s)
        time.append(t)

# ---------------- O(n) BENCHMARK ----------------
# Scale linear function to last data point
c = time[-1] / size[-1]
on_benchmark = [c * s for s in size]

# ---------------- PLOTTING ----------------
plt.figure(figsize=(10, 6))

# Measured time
plt.plot(size, time, label="Measured Time", linewidth=2)

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