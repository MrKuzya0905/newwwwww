# Завдання 1

import re

text = """
Привіт! Мої контакти:
ivan@gmail.com
test123@example.com
student@lpnu.ua

Також можна написати на support@test.org.
"""

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

emails = re.findall(pattern, text)

print("Знайдені email:")
print(emails)

# Завдання 2

def find_last_occurrence(text, sub):
    return text.rfind(sub)


def index_last_occurrence(text, sub):
    try:
        return text.rindex(sub)
    except ValueError:
        return -1


text = "Python is easy. Python is powerful."

print(find_last_occurrence(text, "Python"))
print(index_last_occurrence(text, "Python"))

print(find_last_occurrence(text, "Java"))
print(index_last_occurrence(text, "Java"))

# Завдання 3

def boyer_moore_search(text, pattern):
    if pattern == "":
        return 0

    bad_char = {}

    for i in range(len(pattern)):
        bad_char[pattern[i]] = i

    text_len = len(text)
    pattern_len = len(pattern)

    i = pattern_len - 1

    while i < text_len:
        j = pattern_len - 1

        while j >= 0 and text[i - (pattern_len - 1 - j)] == pattern[j]:
            j -= 1

        if j == -1:
            return i - pattern_len + 1

        bad_character = text[i - (pattern_len - 1 - j)]

        if bad_character in bad_char:
            shift = max(1, j - bad_char[bad_character])
        else:
            shift = j + 1

        i += shift

    return -1