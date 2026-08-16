from collections import deque

queue = deque()

queue.append("Олексій")
queue.append("Марія")
queue.append("Іван")
queue.append("Анна")

print("Черга:", queue)

print("Перший у черзі:", queue[0])

while queue:
    client = queue.popleft()
    print("Обслуговуємо:", client)

print("Черга порожня")


# Друге завдання

def check_brackets(text):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in text:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack or stack[-1] != pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0

print(check_brackets("()"))          # True
print(check_brackets("({[]})"))      # True
print(check_brackets("([{}])"))      # True
print(check_brackets("(]"))          # False
print(check_brackets("([)]"))        # False
print(check_brackets("((("))         # False
print(check_brackets("abc"))         # True