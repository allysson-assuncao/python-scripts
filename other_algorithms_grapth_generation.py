import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("other_results.csv")

algorithms = df['Algorithm'].unique()
sizes = df['Size'].unique()
colors = plt.cm.tab10.colors

plt.figure(figsize=(12, 8))
for i, algorithm in enumerate(algorithms):
    subset = df[df['Algorithm'] == algorithm]
    plt.plot(subset['Size'], subset['Time'],
             label=algorithm, color=colors[i], marker='o')

plt.xlabel('Tamanho do vetor')
plt.ylabel('Tempo Médio (ms)')
plt.title('Desempenho de Algoritmos de Ordenação')
plt.legend()
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.tight_layout()
plt.show()
