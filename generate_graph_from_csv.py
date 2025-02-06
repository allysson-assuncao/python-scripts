import pandas as pd
import matplotlib.pyplot as plt

# # Load the CSV file into a DataFrame
# df = pd.read_csv('sort_results.csv')
#
# # Plot the results
# plt.figure(figsize=(10, 6))
# for algorithm in df['Algorithm'].unique():
#     subset = df[df['Algorithm'] == algorithm]
#     for order in subset['Order'].unique():
#         order_subset = subset[subset['Order'] == order]
#         plt.plot(order_subset['Size'], order_subset['Time (ms)'], label=f'{algorithm} - {order}')
#
# plt.title('Sorting Algorithm Performance')
# plt.xlabel('Array Size')
# plt.ylabel('Time (ms)')
# plt.legend()
# plt.grid(True)
# plt.savefig('sorting_performance.png')
# plt.show()



# Ler o arquivo CSV
df = pd.read_csv("results.csv")

# Configurações dos gráficos
algorithms = df['Algoritmo'].unique()
sizes = df['Tamanho'].unique()
orders = df['Ordem'].unique()
colors = plt.cm.tab10.colors  # Cores para os tamanhos
line_styles = ['-', '--', ':']  # Estilos de linha para as ordens

# Gerar um gráfico para cada algoritmo
for algorithm in algorithms:
    plt.figure(figsize=(10, 6))
    for i, size in enumerate(sizes):
        for j, order in enumerate(orders):
            subset = df[(df['Algoritmo'] == algorithm) &
                        (df['Tamanho'] == size) &
                        (df['Ordem'] == order)]
            plt.plot(subset['Tamanho'], subset['TempoMedio'],
                     label=f'{order} (n={size})',
                     color=colors[i], linestyle=line_styles[j])

    plt.xlabel('Tamanho do Vetor')
    plt.ylabel('Tempo Médio de Execução (s)')
    plt.title(f'Desempenho do {algorithm}')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
