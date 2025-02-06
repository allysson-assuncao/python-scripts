import matplotlib.pyplot as plt
import random
import time


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def generate_array(size, order):
    if order == 'crescente':
        return list(range(1, size + 1))
    elif order == 'decrescente':
        return list(range(size, 0, -1))
    elif order == 'aleatorio':
        return [random.randint(1, size) for _ in range(size)]


def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())
    end_time = time.time()
    return end_time - start_time


sizes = [100, 1000, 10000, 100000]
orders = ['crescente', 'decrescente', 'aleatorio']
algorithms = {
    'Selection Sort': selection_sort,
    'Insertion Sort': insertion_sort,
    'Bubble Sort': bubble_sort,
    'Merge Sort': merge_sort,
    'Quick Sort': quick_sort
}

results = {algo: {order: [] for order in orders} for algo in algorithms}

for size in sizes:
    for order in orders:
        arr = generate_array(size, order)
        for algo_name, algo_func in algorithms.items():
            time_taken = measure_time(algo_func, arr)
            results[algo_name][order].append(time_taken)
            print(f"{algo_name} - {order} - Size {size}: {time_taken:.6f} seconds")

for algo_name, algo_results in results.items():
    plt.figure(figsize=(10, 6))
    for order in orders:
        plt.plot(sizes, algo_results[order], label=order)
    plt.xlabel('Tamanho do Vetor')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title(f'Performance do {algo_name}')
    plt.legend()
    plt.grid(True)
    plt.show()