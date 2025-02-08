import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")

algorithms = df['Algorithm'].unique()
orders = df['Order'].unique()
colors = plt.cm.tab10.colors
line_styles = ['-', '--', ':']

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
    plt.tight_layout()
    plt.show()