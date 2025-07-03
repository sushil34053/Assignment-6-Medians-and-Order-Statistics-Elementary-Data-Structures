# selection_algorithms.py
import random
import time
import matplotlib.pyplot as plt

# Randomized QuickSelect 
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def randomized_select(arr, low, high, k):
    if low == high:
        return arr[low]
    pivot_index = randomized_partition(arr, low, high)
    rank = pivot_index - low + 1
    if k == rank:
        return arr[pivot_index]
    elif k < rank:
        return randomized_select(arr, low, pivot_index - 1, k)
    else:
        return randomized_select(arr, pivot_index + 1, high, k - rank)

# Deterministic Select (Median of Medians)
def partition(arr, pivot):
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]
    return low, equal, high

def deterministic_select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k - 1]
    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    median_of_medians = deterministic_select(medians, len(medians) // 2 + 1)
    low, equal, high = partition(arr, median_of_medians)
    if k <= len(low):
        return deterministic_select(low, k)
    elif k <= len(low) + len(equal):
        return median_of_medians
    else:
        return deterministic_select(high, k - len(low) - len(equal))

# Empirical Analysis
def test_selection_algorithms():
    sizes = [1000, 2000, 5000, 10000]
    results_rand = []
    results_det = []

    for size in sizes:
        test_data = [random.randint(1, size * 10) for _ in range(size)]
        k = size // 2

        start = time.time()
        randomized_select(test_data.copy(), 0, size - 1, k)
        results_rand.append(time.time() - start)

        start = time.time()
        deterministic_select(test_data.copy(), k)
        results_det.append(time.time() - start)

        print(f"Size {size}: Randomized = {results_rand[-1]:.6f}s, Deterministic = {results_det[-1]:.6f}s")

    # Plotting
    plt.plot(sizes, results_rand, label='Randomized Select')
    plt.plot(sizes, results_det, label='Deterministic Select (MoM)')
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Empirical Comparison of Selection Algorithms')
    plt.legend()
    plt.grid(True)
    plt.savefig("selection_algorithms_comparison.png")
    plt.show()

if __name__ == "__main__":
    test_selection_algorithms()
