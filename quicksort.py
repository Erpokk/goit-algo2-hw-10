import random
import time
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def measure_time(sort_function, arr, iterations=5):
    times = []
    for _ in range(iterations):
        test_arr = arr.copy()
        start_time = time.time()
        sort_function(test_arr)
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times)


sizes = [10_000, 50_000, 100_000, 500_000]
results_randomized = []
results_deterministic = []

for size in sizes:
    test_array = [random.randint(0, 10**6) for _ in range(size)]
    random_time = measure_time(randomized_quick_sort, test_array)
    deterministic_time = measure_time(deterministic_quick_sort, test_array)

    results_randomized.append(random_time)
    results_deterministic.append(deterministic_time)

    print(f"Array Size: {size}")

    print(f"Determined QuickSort: {random_time:.4f} seconds")

    print(f"Determined QuickSort: {deterministic_time:.4f} seconds")

plt.plot(
    sizes, results_randomized, label="Randomize QuickSort", marker="o", color="g"
)
plt.plot(
    sizes,
    results_deterministic,
    label="Determined QuickSort",
    marker="s",
    color="b",
)
plt.xlabel("Array Size")
plt.ylabel("Avg time (seconds)")
plt.title("Compare QuickSort")
plt.legend()
plt.grid()
plt.show()