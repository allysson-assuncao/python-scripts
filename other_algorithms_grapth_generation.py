import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")

algorithms = df['Algorithm'].unique()
sizes = df['Size'].unique()
colors = plt.cm.tab10.colors

plt.figure(figsize=(12, 8))
for i, algorithm in enumerate(algorithms):
    subset = df[df['Algorithm'] == algorithm]
    plt.plot(subset['Size'], subset['TimeMillis'],
             label=algorithm, color=colors[i], marker='o')

plt.xlabel('Size of Array')
plt.ylabel('Average Time (milliseconds)')
plt.title('Performance of Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.tight_layout()
plt.show()
