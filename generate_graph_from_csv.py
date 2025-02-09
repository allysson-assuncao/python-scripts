import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("different_results.csv")

algorithms = df['Algorithm'].unique()
orders = df['Order'].unique()
colors = plt.cm.tab10.colors
line_styles = ['-', '--', ':']

time_scale = [0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000, 1000000]

sizes = [100, 500, 1000, 5000, 20000, 50000, 100000, 500000]

for algorithm in algorithms:
    plt.figure(figsize=(10, 6))

    for j, order in enumerate(orders):
        subset = df[(df['Algorithm'] == algorithm) & (df['Order'] == order)]
        plt.plot(subset['Size'], subset['Time'],
                 label=f'{order}',
                 color=colors[j], linestyle=line_styles[j], marker='o')

    plt.xlabel('Size of Array')
    plt.ylabel('Average Time (milliseconds)')
    plt.title(f'Performance of {algorithm}')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)

    plt.xscale('log')
    plt.yscale('log')

    plt.yticks(time_scale, labels=[str(t) for t in time_scale])

    plt.xticks(sizes, labels=[str(s) for s in sizes], rotation=45)

    for size in sizes:
        plt.axvline(x=size, color='gray', linestyle=':', alpha=0.3)

    plt.tight_layout()
    plt.show()