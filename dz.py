def count_vowels(s):
    vowels = "aeiou"
    count = 0

    for char in s.lower():
        if char in vowels:
            count += 1

    return count


print(count_vowels("hello world"))


def flatten_list(nested_list):
    result = []

    for sublist in nested_list:
        for item in sublist:
            result.append(item)

    return result


print(flatten_list([[1, 2], [3, 4], [5, 6]]))

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b

    return a


print(fibonacci(10))