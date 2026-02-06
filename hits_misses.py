import matplotlib.pyplot as plt

# Read the last line (largest array size)
with open("linear_search_analysis.txt") as f:
    lines = f.readlines()

last = lines[-1].split()

hit_perc = float(last[1])
miss_perc = float(last[2])

labels = ["Hits", "Misses"]
sizes = [hit_perc, miss_perc]

plt.figure(figsize=(6, 6))
plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90,
    colors=["cyan", "orange"]
)

plt.title("Hit vs Miss Distribution (Average Case)")
plt.tight_layout()
plt.show()