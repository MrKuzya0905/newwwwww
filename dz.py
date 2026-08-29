# 1

def selection_sort_max(arr):
    n = len(arr)

    for i in range(n - 1, 0, -1):
        max_index = i

        for j in range(i):
            if arr[j] > arr[max_index]:
                max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


numbers = [64, 25, 12, 22, 11]

print("До сортування:", numbers)

selection_sort_max(numbers)

print("Після сортування:", numbers)

# 3

import random
import time


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


numbers = [random.randint(1, 1000) for _ in range(100)]

# Вставки
start = time.perf_counter()
insertion_sort(numbers.copy())
insertion_time = time.perf_counter() - start

# Вибір
start = time.perf_counter()
selection_sort(numbers.copy())
selection_time = time.perf_counter() - start

# QuickSort
start = time.perf_counter()
quick_sort(numbers.copy())
quick_time = time.perf_counter() - start


print("Час виконання:")
print("Insertion Sort:", insertion_time)
print("Selection Sort:", selection_time)
print("QuickSort:", quick_time)

# 5

def median_of_three(a, b, c):
    values = [a, b, c]
    values.sort()
    return values[1]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    first = arr[0]
    middle = arr[len(arr) // 2]
    last = arr[-1]

    pivot = median_of_three(first, middle, last)

    left = [x for x in arr if x < pivot]
    middle_part = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle_part + quick_sort(right)


arrays = [
    [5, 2, 8, 1, 9, 3],
    [1, 2, 3, 4, 5, 6],
    [6, 5, 4, 3, 2, 1],
    [10, 1, 7, 3, 8, 2],
    [5, 5, 2, 5, 1, 5]
]


for arr in arrays:
    print("До:", arr)
    print("Після:", quick_sort(arr))
    print()