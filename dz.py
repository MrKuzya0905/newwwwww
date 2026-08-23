# pershe

def bubble_sort_stable_check(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            # Порівнюємо тільки value
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


test_data = [
    (3, 'a'),
    (1, 'b'),
    (3, 'c'),
    (2, 'd'),
    (3, 'e')
]

print("До сортування:")
print(test_data)

bubble_sort_stable_check(test_data)

print("\nПісля сортування:")
print(test_data)


#  druge

import time
import random


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

data = random.sample(range(100000), 10000)

arr_copy = data[:]

start = time.time()

bubble_sort(data)

end = time.time()

print(f"Bubble Sort time: {end - start:.4f} с")

start = time.time()

arr_copy.sort()

end = time.time()

print(f"Built-in sort time: {end - start:.4f} с")