import random, time, heapq

# def linear_search(arr, x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i
#     return -1


# def binary_search(arr, x):
#     low, high = 0, len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] < x:
#             low = mid + 1
#         elif arr[mid] > x:
#             high = mid - 1
#         else:
#             return mid


# size = 10000000
# data = sorted([random.randint(1, 1000000000) for _ in range(size)])
# target = random.choice(data)

# time_start1 = time.time()
# linear_search(data, target)
# time_1 = time.time() - time_start1
# print(f"Time search: {time_1:0.8f}")

# time_start2 = time.time()
# binary_search(data, target)
# time_2 = time.time() - time_start2
# print(f"Time search: {time_2:0.8f}")
# print(time_1/time_2)

# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1},
#     'D': {'B': 5, 'C': 1}
# }

# def dijkstra(graph, start):
#     queue = []
#     heapq.heappush(queue, (0, start))
#     distances = {vertex: float('infinity') for vertex in graph}
#     distances[start] = 0

#     while queue:
#         current_distance, current_vertex = heapq.heappop(queue)

#         if current_distance > distances[current_vertex]:
#             continue

#         for neighbor, weight in graph[current_vertex].items():
#             distance = current_distance + weight

#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(queue, (distance, neighbor))

#     return distances

# print(dijkstra(graph, "C"))

# def get_el(arr, idx):
#     return arr[idx]

# def binary_search(arr, x):
#     low, high = 0, len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] < x:
#             low = mid + 1
#         elif arr[mid] > x:
#             high = mid - 1
#         else:
#             return mid
        

# def linear_search(arr, x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i
#     return -1

# def has_duplicates(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if i != j and arr[i] == arr[j]:
#                 return True

# sales = [250, 300, 150, 400, 200]
# sales.append(350)
# print(sales)
# sales.remove(150)
# print(sales)
# sales.sort()
# print(sales)
# mean = sum(sales) / len(sales)
# print(mean)

# def has_duplicates_slow(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if i != j and arr[i] == arr[j]:
#                 return True
#     return False

# def has_duplicates_slow(arr):
#     return len(arr) != len(set(arr))

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)

# tuplesum = tuple(tuple1, tuple2)
# print(tuplesum)

# set_1 = {1, 2, 3, 4}
# set_2 = {1, 4}
# set_miss = set_1 | set_2
# print(set_miss)

# # Створіть функцію find_user_by_email(email), яка повертає ID користувача або None, якщо такого email немає.
# users = {
#     101: {"name": "Alice", "email": "alice@example.com", "age": 25},
#     102: {"name": "Bob", "email": "bob@example.com", "age": 30},
#     103: {"name": "Charlie", "email": "charlie@example.com", "age": 22}
# }
# # # Створіть функцію пошуку за email
# assert find_user_by_email("bob@example.com") == 102, "❌ Помилка у пошуку користувача!"
# assert find_user_by_email("notfound@example.com") is None, "❌ Неправильне значення для неіснуючого користувача!"


# def find_user_by_email(email):
#     users = {
#     101: {"name": "Alice", "email": "alice@example.com", "age": 25},
#     102: {"name": "Bob", "email": "bob@example.com", "age": 30},
#     103: {"name": "Charlie", "email": "charlie@example.com", "age": 22}
#     }
#     for user_id, user_data in users.items():
#         if user_data["email"] == email:
#             return user_id

# assert find_user_by_email("bob@example.com") == 102, "❌ Помилка у пошуку користувача!"
# assert find_user_by_email("notfound@example.com") is None, "❌ Неправильне значення для неіснуючого користувача!"

# def check_list(inp_list):
#     return list(set(inp_list))

# Напишіть програму, яка приймає список рядків та повертає список,
# в якому кожен елемент — це рядок, який містить першу літеру кожного слова в вхідному рядку.

# def first_letters(strings):
#     result = []

#     for text in strings:
#         letters = ""
#         for word in text.split():
#             letters += word[0]
#         result.append(letters)

#     return result

# strings = [
#     "Hello World",
#     "Python is awesome",
#     "Open AI ChatGPT"
# ]

# print(first_letters(strings))

# def word(inp_list):
#     return ", ".join(inp_list)


# Тобі дано список з цілими числами. Твоя задача в цій місії - продублювати нулі
# my_list =  [100, 10, 0, 101, 1000] # -> [100, 10, 0, 0, 101, 1000]

def duplicate_zeros(my_list):
    result = []
    for num in my_list:
        result.append(num)
        if num == 0:
            result.append(0)
    return result

print(duplicate_zeros([100, 10, 0, 101, 1000]))