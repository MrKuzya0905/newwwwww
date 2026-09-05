# 4

def linear_search_2d(arr, target):
    for row, lst in enumerate(arr):
        for col, number in enumerate(lst):
            if number == target:
                return (row, col)


arr = [
    [4, 7, 2],
    [9, 5, 8],
    [1, 6, 3]
]

print(linear_search_2d(arr, 5))