import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

df = pd.read_csv("other_results.csv")

algorithms = df['Algorithm'].unique()
orders = df['Order'].unique()
colors = plt.cm.tab10.colors
line_styles = ['-', '--', ':']

sizes = [100, 500, 1000, 5000, 20000, 50000, 100000, 500000]

time_scales = {
    "QuickSort": (0.001, 100),
    "CountingSort": (0.001, 100),
    "RadixSort": (0.001, 100),
    "BucketSort": (0.001, 100),
}

for algorithm in algorithms:
    plt.figure(figsize=(10, 6))

    for j, order in enumerate(orders):
        subset = df[(df['Algorithm'] == algorithm) & (df['Order'] == order)]
        plt.plot(subset['Size'], subset['Time'],
                 label=f'{order}',
                 color=colors[j], linestyle=line_styles[j], marker='o')

    plt.xlabel('Tamanho do Vetor')
    plt.ylabel('Tempo médio (ms)')
    plt.title(f'Desempenho do {algorithm}')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)

    plt.xscale('log')
    plt.ylim(time_scales[algorithm])

    # Configurando formatação do eixo Y para exibir inteiros
    ax = plt.gca()
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.yaxis.get_major_formatter().set_scientific(False)

    plt.xticks(sizes, labels=[str(s) for s in sizes], rotation=45)

    for size in sizes:
        plt.axvline(x=size, color='gray', linestyle=':', alpha=0.3)

    plt.tight_layout()
    plt.show()

plt.figure(figsize=(12, 8))

for i, algorithm in enumerate(algorithms):
    for j, order in enumerate(orders):
        subset = df[(df['Algorithm'] == algorithm) & (df['Order'] == order)]
        plt.plot(subset['Size'], subset['Time'],
                 label=f'{algorithm} - {order}',
                 color=colors[i], linestyle=line_styles[j], marker='o')

# Configurações do gráfico de sobreposição
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Tempo médio (ms)')
plt.title('Desempenho Comparativo dos Algoritmos')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)

# Escala logarítmica para o eixo X (tamanho do vetor)
plt.xscale('log')

# Escala linear fixa para o eixo Y (tempo em milissegundos)
plt.ylim(0, 100)  # Escala do Bubble Sort

# Marcadores para os tamanhos exatos dos vetores
plt.xticks(sizes, labels=[str(s) for s in sizes], rotation=45)

# Adicionar "riscos" abaixo de cada ponto
for size in sizes:
    plt.axvline(x=size, color='gray', linestyle=':', alpha=0.3)

plt.tight_layout()
plt.show()
