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
# # }

# # def dijkstra(graph, start):
# #     queue = []
# #     heapq.heappush(queue, (0, start))
# #     distances = {vertex: float('infinity') for vertex in graph}
# #     distances[start] = 0

# #     while queue:
# #         current_distance, current_vertex = heapq.heappop(queue)

# #         if current_distance > distances[current_vertex]:
# #             continue

# #         for neighbor, weight in graph[current_vertex].items():
# #             distance = current_distance + weight

# #             if distance < distances[neighbor]:
# #                 distances[neighbor] = distance
# #                 heapq.heappush(queue, (distance, neighbor))

# #     return distances

# # print(dijkstra(graph, "C"))

# # def get_el(arr, idx):
# #     return arr[idx]

# # def binary_search(arr, x):
# #     low, high = 0, len(arr) - 1
# #     while low <= high:
# #         mid = (low + high) // 2
# #         if arr[mid] < x:
# #             low = mid + 1
# #         elif arr[mid] > x:
# #             high = mid - 1
# #         else:
# #             return mid
        

# # def linear_search(arr, x):
# #     for i in range(len(arr)):
# #         if arr[i] == x:
# #             return i
# #     return -1

# # def has_duplicates(arr):
# #     for i in range(len(arr)):
# #         for j in range(len(arr)):
# #             if i != j and arr[i] == arr[j]:
# #                 return True

# # sales = [250, 300, 150, 400, 200]
# # sales.append(350)
# # print(sales)
# # sales.remove(150)
# # print(sales)
# # sales.sort()
# # print(sales)
# # mean = sum(sales) / len(sales)
# # print(mean)

# # def has_duplicates_slow(arr):
# #     for i in range(len(arr)):
# #         for j in range(len(arr)):
# #             if i != j and arr[i] == arr[j]:
# #                 return True
# #     return False

# # def has_duplicates_slow(arr):
# #     return len(arr) != len(set(arr))

# # tuple1 = (1, 2, 3)
# # tuple2 = (4, 5, 6)

# # tuplesum = tuple(tuple1, tuple2)
# # print(tuplesum)

# # set_1 = {1, 2, 3, 4}
# # set_2 = {1, 4}
# # set_miss = set_1 | set_2
# # print(set_miss)

# # # Створіть функцію find_user_by_email(email), яка повертає ID користувача або None, якщо такого email немає.
# # users = {
# #     101: {"name": "Alice", "email": "alice@example.com", "age": 25},
# #     102: {"name": "Bob", "email": "bob@example.com", "age": 30},
# #     103: {"name": "Charlie", "email": "charlie@example.com", "age": 22}
# # }
# # # # Створіть функцію пошуку за email
# # assert find_user_by_email("bob@example.com") == 102, "❌ Помилка у пошуку користувача!"
# # assert find_user_by_email("notfound@example.com") is None, "❌ Неправильне значення для неіснуючого користувача!"


# # def find_user_by_email(email):
# #     users = {
# #     101: {"name": "Alice", "email": "alice@example.com", "age": 25},
# #     102: {"name": "Bob", "email": "bob@example.com", "age": 30},
# #     103: {"name": "Charlie", "email": "charlie@example.com", "age": 22}
# #     }
# #     for user_id, user_data in users.items():
# #         if user_data["email"] == email:
# #             return user_id

# # assert find_user_by_email("bob@example.com") == 102, "❌ Помилка у пошуку користувача!"
# # assert find_user_by_email("notfound@example.com") is None, "❌ Неправильне значення для неіснуючого користувача!"

# # def check_list(inp_list):
# #     return list(set(inp_list))

# # Напишіть програму, яка приймає список рядків та повертає список,
# # в якому кожен елемент — це рядок, який містить першу літеру кожного слова в вхідному рядку.

# # def first_letters(strings):
# #     result = []

# #     for text in strings:
# #         letters = ""
# #         for word in text.split():
# #             letters += word[0]
# #         result.append(letters)

# #     return result

# # strings = [
# #     "Hello World",
# #     "Python is awesome",
# #     "Open AI ChatGPT"
# # ]

# # print(first_letters(strings))

# # def word(inp_list):
# #     return ", ".join(inp_list)


# # Тобі дано список з цілими числами. Твоя задача в цій місії - продублювати нулі
# # my_list =  [100, 10, 0, 101, 1000] # -> [100, 10, 0, 0, 101, 1000]

# # def duplicate_zeros(my_list):
# #     result = []
# #     for num in my_list:
# #         result.append(num)
# #         if num == 0:
# #             result.append(0)
# #     return result

# # print(duplicate_zeros([100, 10, 0, 101, 1000]))



# # FIFO


# class Queue:
#     def __init__(self):
#         self.items = []

#     def enqueue(self, item) -> None:
#         self.items.append(item)

#     def dequeue(self):
#         # self.items[0] # O(1)
#         if not self.is_empty():
#             return self.items.pop(0) # O(n)
#         # return None

#     def is_empty(self):
#         return self.size() == 0
#         # return if not self.items

#     def peek(self):
#         if not self.is_empty():
#             return self.items[0]

#     def size(self):
#         return len(self.items) # O(n)


# # queue = Queue()
# # queue.enqueue(2)
# # queue.enqueue(5)
# # print(queue.peek())
# # queue.enqueue(9)
# # print(queue.dequeue())
# # print(queue.size())
# # print(queue.peek())
# # print(queue.dequeue())
# # print(queue.dequeue())
# # print(queue.size())
# # print(queue.peek())


# from collections import deque
# import random
# import time


# class Car:
#     def __init__(self, id):
#         self.id = id


# class Traffic:
#     def __init__(self, green_time=3, red_time=3):
#         self.green_time = green_time
#         self.red_time = red_time
#         self.is_green = True
#         self.timer = 0

#     def update(self):
#         self.timer += 1
#         if self.is_green and self.green_time <= self.timer:
#             self.is_green = False
#             self.timer = 0
#         elif not self.is_green and self.red_time <= self.timer:
#             self.is_green = True
#             self.timer = 0


# def autocad(green_time=3, red_time=3, probability=0.3):
#     queue = deque()
#     traffic = Traffic(green_time, red_time)

#     for _ in range(20):
#         if random.random() <= probability:
#             car = Car(id=random.randint(1, 500))
#             queue.append(car)
#             print(f"Під'їхало нове авто з id {car.id}")

#         traffic.update()
#         print(f"Світло зелене?->{traffic.is_green}")

#         if traffic.is_green:
#             if len(queue):
#                 print(f"Авто з id '{queue.pop().id}' проїхало на зелений")

#         print(f"Залишилось {len(queue)} авто")

#         time.sleep(.5)


# autocad(2, 4, 0.7)

# LIF0

# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item) -> None:
#         self.items.append(item)

#     def undo(self):
#         # self.items[0] # O(1)
#         if not self.is_empty():
#             return self.items.pop(0) # O(n)
#         # return None

#     def is_empty(self):
#         return self.size() == 0
#         # return if not self.items

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]

#     def size(self):
#         return len(self.items) # O(n)

# class Text:
#     def __init__(self, content):
#         self.content = content

#     def __str__(self):
#         return f"Text: {self.content}"

# class TextEditor:
#     def __init__(self):
#         self.items = []

#     def push(self, text) -> None:
#             self.items.append(text)

#     def undo(self, count):
#             for _ in range(count):
#                 if self.is_empty():
#                      return

#                 self.items.pop()

    
#     def is_empty(self):
#             return self.size() == 0
#             # return if not self.items
    
#     def peek(self):
#             if not self.is_empty():
#                 return self.items[-1]
    
#     def size(self):
#             return len(self.items) # O(n)

# У браузері можна зберігати історію відвіданих
# сторінок у вигляді стека: коли ви переходите
# на нову сторінку, вона “накладається” поверх
# # попередньої. Якщо натиснути “Назад” (Back),
# # ми вилучимо з вершини останню сторінку й повернемося до тієї, що була раніше.

# class BrowserHistory:
#     def __init__(self):
#         self.items = []

#     def visit(self, url):
#         # Додайте код для "зайти" на нову сторінку (push)
#         self.items.append(url)

#     def back(self):
#         # Додайте код для повернення (pop) на попередню сторінку
#         if not self.is_empty():
#             return self.items.pop()

#     def is_empty(self):
#         return self.size() == 0

#     def current_page(self):
#         # Визначте, яка сторінка зараз на "верхівці" (peek) або None, якщо історія порожня
#         if not self.is_empty():
#             return self.items[-1]

#     def size(self):
#         return len(self.items)

# browser = BrowserHistory()
# browser.visit("google.com")
# browser.visit("wikipedia.org")
# browser.visit("stackoverflow.com")
# print("Поточна сторінка:", browser.current_page())
# browser.back()
# print("Після натискання BACK, сторінка:", browser.current_page())



# У корпоративному чаті повідомлення від
# користувачів надходять одне за одним і
# тимчасово складаються у буфер (чергу), перш
# ніж система їх розподілить. Необхідно
# реалізувати цю логіку із затримкою — наприклад,
# щоб кожне отримане повідомлення “прочиталося” за секунду.
# import time

# class MessageQueue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, msg):
#         # Додайте нове повідомлення в кінець черги
#         self.queue.append(msg)

#     def dequeue(self):
#         # Якщо черга не порожня, поверніть перший елемент і вилучіть його
#         if not self.is_empty():
#             return self.queue.pop(0)

#     def is_empty(self):
#         return len(self.queue) == 0

# chat_buffer = MessageQueue()
# # Додайте три повідомлення у різний час
# chat_buffer.enqueue("hi")
# time.sleep(0.5)
# chat_buffer.enqueue("ok")
# time.sleep(0.5)
# chat_buffer.enqueue("bye")

# while not chat_buffer.is_empty():
#     msg = chat_buffer.dequeue()
#     print("Обробляємо:", msg)
#     time.sleep(1)


# Є лабораторна система, де формується черга
# документів на аналіз. Наприклад, PDF-файли
# чи будь-які інші файли надходять послідовно
# та стають у чергу, поки не доходить черга
# до аналізатора, котрий бере перший документ і «перевіряє» його.

# import random

# class DocumentQueue:
#     def __init__(self):
#         self.docs = []

#     def enqueue(self, doc):
#         self.docs.append(doc)

#     def dequeue(self):
#         ...

#     def size(self):
#         return len(self.docs)

# doc_queue = DocumentQueue()
# doc_types = ["PDF", "DOC", "IMG", "TXT"]

# for i in range(5):
#     doc_type = random.choice(doc_types)
#     doc_name = f"File_{i}.{doc_type.lower()}"
#     doc_queue.enqueue(doc_name)
#     print("Надійшов документ:", doc_name)

# print("Загальна кількість документів:", doc_queue.size())

# while doc_queue.size() > 0:
#     current_doc = doc_queue.dequeue()
#     print(f"Обробляємо: {current_doc}")


# У графічному редакторі кожен крок (наприклад,
# малювання лінії, заливка кольором) може зберігатися
# у стек. Кнопка «Undo» дозволяє видалити останню зроблену дію.

# class EditorAction:
#     def __init__(self, description):
#         self.description = description

#     def __str__(self):
#         return f"Action: {self.description}"

# class ActionStack:
#     def __init__(self):
#         self.stack = []

#     def push(self, action):
#         # Додайте операцію вставки зверху
#         ...

#     def pop(self):
#         # Вилучайте верхній елемент, якщо він існує
#         ...

#     def peek(self):
#         # Перевірте верхній елемент без вилучення
#         ...

#     def is_empty(self):
#         return len(self.stack) == 0
# actions = ActionStack()
# actions.push(EditorAction("Draw line"))
# actions.push(EditorAction("Fill color"))
# print("Остання дія:", actions.peek())
# last = actions.pop()
# print("Скасовано:", last)
# print("Нова верхівка:", actions.peek())


# def fib(n):
#   if n <= 0:
#     return 0
#   elif n == 1:
#     return 1
#   else:
#     return fib(n - 1) + fib(n - 2)

# def sum_item_list(lst):
#     if not lst:
#         return 0
#     lst[0] + sum_item_list[1:]

# ЗАВДАННЯ 1
# Створіть рекурсивну функцію, що обчислює степінь числа x у натуральній степені n.
# Базовий випадок: якщо n=0, повернути 1.
# Якщо n>0, повернути x∗power(x,n−1).
# x∗power(x,n−1)x * power(x, n-1)


# def power(x, n):
#     if n == 0:
#         return 1
#     return x * power(x, n-1)

# print(power(5,0))

# ЗАВДАННЯ 2
# Напишіть рекурсивну функцію, що визначає, чи є список упорядкованим (зростаючим).
# Якщо список довжиною 0 або 1 — він упорядкований.
# Для довшого списку перевірити, чи перші два елементи задовольняють
# умову зростання, і рекурсивно викликати для «хвоста» списку.

# ЗАВДАННЯ 2
# Напишіть рекурсивну функцію, що визначає, чи є список упорядкованим (зростаючим).
# Якщо список довжиною 0 або 1 — він упорядкований.
# Для довшого списку перевірити, чи перші два елементи задовольняють
# умову зростання, і рекурсивно викликати для «хвоста» списку.


# def is_sorted_asc(lst):
#     if len(lst) < 2:
#         return True

#     if lst[0] > lst[1]:
#         return False

#     return is_sorted_asc(lst[1:])


# print(is_sorted_asc([1, 2, 4, 3, 5]))  

# def swap_elements(lst, i):
#     lst[i], lst[i + 1] = lst[i + 1], lst[i]
#     return lst


# lst = [1, 2, 3, 4, 5]

# print(swap_elements(lst, 1))

# def bubble_sort(lst):
# #     count = 0

# #     for _ in range(len(lst) - 1):
# #         swapped = False

# #         for i in range(len(lst) - 1):
# #             if lst[i] > lst[i + 1]:
# #                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
# #                 count += 1
# #                 swapped = True

# #         print(lst)

# #         if not swapped:
# #             break

# #     print("Кількість замін:", count)
# #     return lst


# # numbers = [5, 2, 9, 1, 7]

# # bubble_sort(numbers)
# # print(numbers)

# # def bubble_sort_by_age(lst):
# #     for _ in range(len(lst) - 1):
# #         swapped = False

# #         for i in range(len(lst) - 1):
# #             if lst[i]['age'] > lst[i + 1]['age']:
# #                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
# #                 swapped = True

# #         if not swapped:
# #             break

# #     return lst


# # people_data = [
# #     {'name': 'Bob', 'age': 25},
# #     {'name': 'Alice', 'age': 30},
# #     {'name': 'Charlie', 'age': 20}
# # ]

# # bubble_sort_by_age(people_data)

# # print(people_data)

# # def bubble_sort(lst):
# #     count = 0

# #     for _ in range(len(lst) - 1):
# #         swapped = False

# #         for i in range(len(lst) - 1):
# #             if lst[i] > lst[i + 1]:
# #                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
# #                 count += 1
# #                 swapped = True

# #         print(lst)

# #         if not swapped:
# #             break

# #     print("Кількість замін:", count)
# #     return lst

# def selection_sort(arr) -> None:
#     n = len(arr)
#     comparisons = 0
#     swaps = 0

#     for i in range(n - 1):
#         idx_min_number = i

#         for j in range(i + 1, n):
#             comparisons += 1
#             if arr[j] < arr[idx_min_number]:
#                 idx_min_number = j

#         if idx_min_number != i:
#             swaps += 1
#             print(f"Знайдено мінімум: {arr[idx_min_number]}")
#             print(f"Міняємо {arr[i]} і {arr[idx_min_number]}")

#             arr[i], arr[idx_min_number] = arr[idx_min_number], arr[i]
            

#             print("Список після заміни:", arr)
#             print()

#     print("Відсортований список:", arr)
#     print("Compa4risons: ", comparisons)


# numbers = [5, 7, 1, 3, 2, 8, 12, 5, 3, 7, 8]

# selection_sort(numbers)

# def insertion_sort(arr) -> None:
#     n = len(arr)
#     comparisons = 0
#     count_shifts = 0

#     for i in range(1, n):
#         curr_number = arr[i]
#         j = i - 1

#         while j >= 0 and arr[j] > curr_number:
#             comparisons += 1
#             arr[j + 1] = arr[j]
#             print("Переміщення: ", arr)
#             j -= 1

#         arr[j + 1] = curr_number
#         count_shifts += 1


# arr = [5, 4, 9, 1, 3, 2]

# insertion_sort(arr)

# print(arr)

# def insertion_sort_2(arr) -> None:
#     n = len(arr)

#     for i in range(1, n):
#         curr_number = arr[i]
#         for j in range(i-1, -1, -1):
#             if arr[j] > curr_number:
#                 arr[j + 1] = arr[j]
#             else:
#                 j += 1
#                 break

#         arr[j] = curr_number
        

# arr = [5, 4, 9, 1, 3, 2]
# players = [
#     {'name': 'Alice', 'score': 50},
#     {'name': 'Bob', 'score': 20},
#     {'name': 'Charlie', 'score': 50},
#     {'name': 'David', 'score': 10}
# ]

# insertion_sort_2(arr)

# # print(arr)
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[-1]
#     left = []
#     right = []

#     for i in range(len(arr) - 1):
#         if arr[i] < pivot:
#             right.append(arr[i])
#         else:
#             left.append(arr[i])

#     print("Контрольне число:", pivot)
#     print("Ліва частина:", left)
#     print("Права частина:", right)

#     return quick_sort(left) + [pivot] + quick_sort(right)


# arr = [5, 4, 9, 1, 3, 2]

# print(quick_sort(arr))

# def linear_search(x, lst):
#     comparisons = 0
#     for i in range(len(lst)):
#         comparisons += 1
#         if lst[i] == x:
#             return (i, comparisons)
#     return (-1, comparisons)

# numbers = [5, 7, 9, 3]
# print(linear_search(7, numbers))

# def linear_search_max(arr):
#     max_index = 0

#     for i in range(1, len(arr)):
#         if arr[i] > arr[max_index]:
#             max_index = i

#     return max_index


# arr = [5, 2, 9, 1, 7]

# print("Масив: ", arr)
# print("Індекс максимального елемента: ", linear_search_max(arr))
# print("Максимальний елемент: ", arr[linear_search_max(arr)])

# def linear_search_all(lst, target):
#     indexes = []

#     for i in range(len(lst)):
#         if lst[i] == target:
#             indexes.append(i)

#     return indexes


# arr = [5, 6, 6,  7, 6,  8, 2, 7, 3]

# result = linear_search_all(arr, 6)

# print("Індекси:", result)

# def recursive_linear_search(arr, target, index=0):
#     if index >= len(arr):
#         return -1

#     if arr[index] == target:
#         return index

#     return recursive_linear_search(arr, target, index + 1)

# arr = [10, 25, 7, 15, 7, 30]

# print(recursive_linear_search(arr, 7))
# print(recursive_linear_search(arr, 30))
# print(recursive_linear_search(arr, 100))

# def find_first_above(arr, threshold):
#     for i in range(len(arr)):
#         if arr[i] > threshold:
#             return i
#     return -1

# arr = [10, 25, 7, 15, 7, 30]
# print(find_first_above(arr, 25))

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1

# arr = [1, 3, 5, 7, 9, 11, 15]
# target = 7

# print(binary_search(arr, target))

# Реалізуйте просту функцію find_substring(text, substring),
# яка використовує вбудований метод find() для пошуку першого входження підрядка у рядок.
# Початковий код:

# def find_substring(text, substring):
#     index = text.find(substring)
#     return index

# text = "Hello, welcome to Python programming!"
# result = find_substring(text, "Python")
# print("Перший індекс входження 'Python':", result)

# Реалізуйте функцію find_substring_range(text, substring, start, end),
# яка знаходить позицію підрядка, обмежуючи область пошуку параметрами start та end.
# Початковий код:

# def find_substring_range(text, substring, start, end):
#     index = text.find(substring, start, end)
#     return index

# text = "banana"
# result = find_substring_range(text, "na", 2, 5)
# print("Позиція 'na' в тексті 'banana' у діапазоні 2-5:", result)

# Реалізуйте функцію find_all_occurrences(text, substring),
# яка повертає список усіх позицій, де входить заданий підрядок у тексті, використовуючи метод find().
# # Початковий код:

# # def find_all_occurrences(text, substring):
# #     indicies = []
# #     start = 0

# #     while True:
# #         index = text.find(substring, start)

# #         if index == -1:
# #             break

# #         indicies.append(index)
# #         start = index + 1

# #     return indicies


# # text = "abracadabra"
# # result = find_all_occurrences(text, "abra")
# # print("Усі позиції входження 'abra':", result)

# # Реалізуйте функцію custom_find(text, substring), яка імітує роботу методу find()
# # за допомогою циклу (без використання вбудованого методу).
# # Функція має повертати індекс першого входження або -1, якщо підрядок не знайдено.
# # Початковий код:

# # def custom_find(text, substring):
# #     for i in range(len(text) - len(substring) + 1):
# #         if text[i:i + len(substring)] == substring:
# #             return i

# #     return -1


# # text = "Hello, world!"
# # result = custom_find(text, "world")
# # print("Перший індекс входження 'world':", result)

# # text = " ... фівцвар цвіашцвр 055-457-89-77. фвацщрівш пагшвціща фівщ ашіфп. ..."

# # import re

# # pattern = r"\d\d\d-\d\d\d-\d\d-\d\d"
# # number = re.search(pattern, text)

# # if number:
# #     print(number.group())


# import re

# # text = "Телефони: 055-457-89-77, 067-123-45-67 та 093-987-65-43."

# # pattern = r"\d\d\d-\d\d\d-\d\d-\d\d"

# # numbers = re.findall(pattern, text)

# # # print(numbers)

# # text = "My numbers are 123 and 4567"

# # import re

# # text = "my numbers are 123 and 4567"

# # numbers = re.findall(r"\d+", text)

# # print(numbers)
# import re

# # text = "Контактний номер менеджера: +380 (67) 123-45-67, зателефонуйте завтра."

# # pattern = r"\+380\s\((\d{2})\)\s(\d{3}-\d{2}-\d{2})"

# # result = re.findall(pattern, text)

# # print(result)

# # if result:
# #     operator_code = result[0][0]
# #     number = result[0][1]

# #     print("Код оператора:", operator_code)
# #     print("Номер:", number)

# # алгоритм Бойера–Мура
# def boyer_moore_search(text, pattern):
#     n = len(text)
#     m = len(pattern)
#     if m == 0:
#         return 0

#     bad_char_shift = {}
#     for index, char in enumerate(pattern):
#         bad_char_shift[char] = index

#     s = 0
#     while s <= n - m:
#         j = m - 1
#         while j >= 0 and pattern[j] == text[s + j]:
#             j -= 1
#         if j < 0:
#             return s
#         else:
#             shift = max(1, j - bad_char_shift.get(text[s + j], -1))
#             s += shift
#     return -1


# # text = "HERE IS A SIMPLE EXAMPLE"
# # pattern = "EXAMPLE"
# # index = boyer_moore_search(text, pattern)
# # print(f"Підрядок '{pattern}' знайдено на позиції: {index}")

# # Реалізуйте функцію bm_search_all(text, pattern),
# # яка знаходить всі входження зразка в тексті за
# # алгоритмом Бойера–Мура та повертає список індексів.
# # Початковий код:

# def bm_search_all(text, pattern):
#     occurrences = []
#     # Побудуйте таблицю для "поганого символу" для pattern
#     # Виконайте пошук по тексту за алгоритмом Бойера–Мура, додаючи кожен знайдений індекс до occurrences
#     pass

# class NodeTree:
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right

# def print_tree(tree, level=0):
#     if isinstance(tree, NodeTree):
#         print_tree(tree.right, level+1)
#         print("   " * level + str(tree.data))
#         print_tree(tree.left, level+1)

# root = NodeTree(
#      10,
#      NodeTree(5, NodeTree(1), NodeTree(7)),
#      NodeTree(12, None, NodeTree(15))
# )

# # print_tree(root)

# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.children = []


# def print_tree(tree, level=0):
#     if not tree:
#         return []

#     print("  " * level + str(tree.data))

#     for child in tree.children:
#         print_tree(child, level + 1)


# root = Tree("A")
# node_B = Tree("B")
# node_C = Tree("C")
# node_D = Tree("D")
# node_E = Tree("E")

# root.children += [node_B, node_C, node_E]
# node_C.children.append(node_D)

# print_tree(root)

# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.children = []

# def build_tree():
#     root = TreeNode("A")

#     B = TreeNode("B")
#     C = TreeNode("C")
#     D = TreeNode("D")

#     E = TreeNode("E")
#     F = TreeNode("F")
#     G = TreeNode("G")

#     root.children.append(B)
#     root.children.append(C)
#     root.children.append(D)

#     B.children.append(E)

#     D.children.append(F)
#     D.children.append(G)

#     return root


# root = build_tree()

# def print_tree(node, level=0):
#     if node:
# #         print("  " * level + node.value)

# #     for child in node.children:
# #         print_tree(child, level + 1)


# # print_tree(root)

# # class BinaryNode:
# #     def __init__(self, value, left=None, right=None):
# #         self.value = value
# #         self.left = left
# #         self.right = right


# # def build_binary_tree():
# #     root = BinaryNode(10)

# #     root.left = BinaryNode(5)
# #     root.right = BinaryNode(15)

# #     root.left.left = BinaryNode(2)
# #     root.left.right = BinaryNode(7)

# #     root.right.right = BinaryNode(20)

# #     return root


# # root = build_binary_tree()

# class NodeTree():
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right

# def build_tree():
#     root = NodeTree(
#         10,
#         NodeTree(5, NodeTree(1), NodeTree(7)),
#         NodeTree(12, None, NodeTree(15))
# )
#     return root

# def tree_height(root):
#     if root is None:
#         return 0
#     return 1 + max(tree_height(root.left), tree_height(root.right))

# root = build_tree()
# result = tree_height(root)
# print(result)

# def count_nodes(root):
#     if root is None:
#         return 0

#     return 1 + count_nodes(root.left) + count_nodes(root.right)

# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# def binary_tree_search(root, target):
#     if root is None:
#         return False

#     if root.value == target:
#         return True

#     if target < root.value:
#         return binary_tree_search(root.left, target)
#     else:
#         return binary_tree_search(root.right, target)


# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(15)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(7)
# root.right.left = TreeNode(12)
# root.right.right = TreeNode(20)


# # Пошук
# print(binary_tree_search(root, 7))   
# print(binary_tree_search(root, 13)) 

# graph = {
#     'A': ['B', 'C'],
# #     'B': ['A', 'D', 'E'],
# #     'C': ['A', 'F'],
# #     'D': ['B'],
# #     'E': ['B', 'F'],
# #     'F': ['C', 'E']
# # }

# # class Graph:

# #     def init(self):
# #         self.adjacency = {}

# #     def add_vertex(self, v) -> None:
# #         if v not in self.adjacency:
# #             self.adjacency[v] = []

# #     def add_edge(self, u, v, directed=False) -> None:
# #         if u not in self.adjacency:
# #             self.add_vertex(u)

# #         if v not in self.adjacency:
# #             self.add_vertex(v)

# #         self.adjacency[u].append(v)

# #         if not directed:
# #             self.adjacency[v].append(u)

# #     def get_neighbors(self, vertex) -> list[str]:
# #         return self.adjacency[vertex]

# #     def str(self) -> str:
# #         return "\n".join(
# #             [f"Vertex {u}: {v}" for u, v in self.adjacency.items()]
# #         )


# # g = Graph()

# # g.add_edge("A", "B")
# # g.add_edge("A", "C")
# # g.add_edge("B", "D")
# # g.add_edge("B", "E")
# # g.add_edge("C", "F")
# # g.add_edge("E", "F")

# # # # В
# # graph_matrix = [
# #     [0, 1, 1, 0, 0, 0],
# #     [1, 0, 0, 1, 1, 0],
# #     [1, 0, 0, 0, 0, 1],
# #     [0, 1, 0, 0, 0, 0],
# #     [0, 1, 0, 0, 0, 1],
# #     [0, 0, 1, 0, 1, 0]
# # ]

# # def to_adjacency_matrix(graph):
# #     vertices = sorted(graph.adjacency.keys())
# #     n = len(vertices)
# #     matrix = [[0]*n for _ in range(n)]
# #     index = {vertex: i for i, vertex in enumerate(vertices)}
# #     for vertex, neighbors in graph.adjacency.items():
# #         for neighbor in neighbors:
# #             matrix[index[vertex]][index[neighbor]] = 1
# #     return matrix




class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, u, v, directed=True):
        self.add_vertex(u)
        self.add_vertex(v)

        self.adjacency_list[u].append(v)

        if not directed:
            self.adjacency_list[v].append(u)

g = Graph()

# g.add_edge("A", "B")
# g.add_edge("A", "C")
# g.add_edge("B", "D")

# print(g.adjacency_list)

# Реалізуйте клас для орієнтованого графа.
# Створіть методи для додавання вершин і
# ребер із зазначенням напрямку.

# Реалізуйте клас для орієнтованого графа.
# Створіть методи для додавання вершин і
# ребер із зазначенням напрямку.

# class DirectedGraph:
#     def __init__(self):
#         self.adjacency = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency:
#             self.adjacency[vertex] = []

#     def add_edge(self, u, v):
#         self.add_vertex(u)
#         self.add_vertex(v)

#         self.adjacency[u].append(v)


# dg = DirectedGraph()

# dg.add_edge('A', 'B')
# dg.add_edge('A', 'C')
# dg.add_edge('B', 'D')

# print("Орієнтований граф (Adjacency List):")
# print(dg.adjacency)

# class WeightedDirectedGraph:
#     def __init__(self):
#         self.adjacency = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency:
#             self.adjacency[vertex] = []

#     def add_edge(self, u, v, weight):
#         self.add_vertex(u)
#         self.add_vertex(v)

#         self.adjacency[u].append((v, weight))


# g = WeightedDirectedGraph()

# g.add_edge('A', 'B', 5)
# g.add_edge('A', 'C', 2)
# g.add_edge('B', 'D', 7)

# print("Орієнтований граф з вагами:")
# print(g.adjacency)

# class Graph:
#     def __init__(self):
#         self.adjacency: dict[str, list[str]] = {}

#     def add_vertex(self, v):
#         if v not in self.adjacency:
#             self.adjacency[v] = []

#     def add_edge(self, u, v, directed=False):
#         if u not in self.adjacency:
#             self.add_vertex(u)
#         if v not in self.adjacency:
#             self.add_vertex(v)

#         self.adjacency[u].append(v)
#         if not directed:
#             self.adjacency[v].append(u)

#     def get_neighbors(self, vertex):
#         return self.adjacency[vertex]

#     def __str__(self) -> str:
#         return "\n".join([f"Vertex {u}: {v}" for u, v in self.adjacency.items()])


# g = Graph()
# g.add_edge("A", "B")
# g.add_edge("A", "C")
# g.add_edge("B", "D")
# g.add_edge("B", "E")
# g.add_edge("C", "F")
# g.add_edge("E", "F")


# def dfs(graph, start):
#     visited = set()
#     stack = [start]
#     result = []
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#             result.append(vertex)
#             stack.extend(reversed(graph.adjacency[vertex]))
#     return result

# print("DFS обхід:", dfs(dg, 'A'))

# S 0 0 1 0
# 1 1 0 1 0
# 0 0 0 0 0
# 0 1 1 1 0
# 0 0 0 E 1

# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }


# def dfs_recursive(node, visited=None):
#     if not visited:
#         visited = set()

#     visited.add(node)

#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             visited.add(neighbor)
#             dfs_recursive(neighbor, visited)

#     return visited


# print("Visited: ", dfs_recursive("A"))

# def dfs_iterative(node, graph):
#     visited = set()
#     stack = [node]

#     while stack:
#         node = stack.pop()

#         if node not in visited:
#             visited.add(node)
#             stack.extend(reversed(graph[node]))

#     return visited


# print("Visited: ", dfs_iterative("A", graph))

# def dfs_component(node, graph, visited):
#     visited.add(node)
#     component = [node]
#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             component.extend(dfs_component(neighbor, graph, visited))
#     return component

# def find_connected_components(graph):
#     visited = set()
#     components = []
#     for node in graph:
#         if node not in visited:
#             component = dfs_component(node, graph, visited)
#             components.append(component)
#     return components

# graph = {
#     'A': ['B'],
#     'B': ['A', 'C'],
#     'C': ['B'],
#     'D': ['E'],
#     'E': ['D'],
#     'F': []
# }

# components = find_connected_components(graph)
# for comp in components:
#     print(comp)

# def dfs_topological(node: str, graph: dict, visited: set, stack: list):
#     visited.add(node)
#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             dfs_topological(neighbor, graph, visited, stack)
#     stack.append(node)

# def topological_sort(graph):
#     visited = set()
#     stack = []
#     for node in graph:
#         if node not in visited:
#             dfs_topological(node, graph, visited, stack)
#     return stack[::-1]

# graph_dag = {
#     'A': ['C', 'D'],
#     'B': ['D'],
#     'C': ['E'],
#     'D': ['F'],
#     'E': ['F'],
#     'F': []
# }

# order = topological_sort(graph_dag)
# print("Топологічне сортування:", order)

# def dfs_cycle(node, graph, visited, rec_stack):
#     visited.add(node)
#     rec_stack.add(node)
#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             if dfs_cycle(neighbor, graph, visited, rec_stack):
#                 return True
#         elif neighbor in rec_stack:
#             return True
#     rec_stack.remove(node)
#     return False

# def has_cycle(graph):
#     visited = set()
#     rec_stack = set()
#     for node in graph:
#         if node not in visited:
#             if dfs_cycle(node, graph, visited, rec_stack):
#                 return True
#     return False

# graph_cycle = {
#     'A': ['B'],
#     'B': ['C'],
#     'C': ['A'],
#     'D': ['E'],
#     'E': []
# }

# print("Граф містить цикл:", has_cycle(graph_cycle))

# def dfs_labyrinth(maze, start, end):
#     rows, cols = len(maze), len(maze[0])
#     stack = [start]
#     visited = {start: None}

#     while stack:
#         current = stack.pop()
#         if current == end:
#             break
#         row, col = current
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             r, c = row + dr, col + dc
#             if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0 and (r, c) not in visited:
# #                 visited[(r, c)] = current
# #                 stack.append((r, c))

# #     path = []
# #     if end not in visited:
# #         return None
# #     current = end
# #     while current is not None:
# #         path.append(current)
# #         current = visited[current]
# #     path.reverse()
# #     return path

# # labyrinth = [
# #     [0, 1, 0, 0, 0],
# #     [0, 1, 0, 1, 0],
# #     [0, 0, 0, 1, 0],
# #     [0, 1, 1, 1, 0],
# #     [0, 0, 0, 0, 0]
# # ]

# # graph_matrix = [
# #     [0, 1, 1, 0, 0, 0],
# #     [1, 0, 0, 1, 1, 0],
# #     [1, 0, 0, 0, 0, 1],
# #     [0, 1, 0, 0, 0, 0],
# #     [0, 1, 0, 0, 0, 1],
# #     [0, 0, 1, 0, 1, 0]
# # ]

# # start = (0, 0)   # верхній лівий кут
# # end = (4, 4)     # нижній правий кут

# # print("Пошук шляху в лабіринті за допомогою DFS:")
# # dfs_labyrinth(labyrinth, start, end)

# graph_matrix = [
#     [0, 0, 1, 0, 0, 0],
#     [1, 0, 0, 0, 1, 0],
#     [1, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0],
#     [0, 0, 1, 0, 1, 0]
# ]

# start = (0, 0)
# end = (5, 5)



# def dfs_labyrinth(maze, start, end):
#     rows, cols = len(maze), len(maze[0])
#     stack = [start]
#     visited = {start: None}
#     count = 0

#     while stack:
#         current = stack.pop()
#         if current == end:
#             break
#         row, col = current
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             r, c = row + dr, col + dc
#             if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0 and (r, c) not in visited:
#                 visited[(r, c)] = current
#                 print(f"Курсор знаходиться на координаті {current}")
#                 count += 1
#                 stack.append((r, c))

#     path = []
#     if end not in visited:
#         return None
#     current = end
#     while current is not None:
#         path.append(current)
#         current = visited[current]
#     path.reverse()
#     return path, count


# def visualize_path_dfs(maze, path):
#     rows, cols = len(maze), len(maze[0])
#     visual_maze = [row[:] for row in maze]

#     if path:
#         for r, c in path:
#             if (r, c) != path[0] and (r, c) != path[-1]:
#                 visual_maze[r][c] = 2

#     print("Лабіринт з позначеним шляхом (0 - вільна клітинка, 1 - стіна, 2 - шлях):")
#     for row in visual_maze:
#         print(" ".join(map(str, row)))

# path, count = dfs_labyrinth(graph_matrix, start, end)
# visualize_path_dfs(graph_matrix, path)
# start = (0, 0)
# end = (5, 5)

# visualize_path_dfs(graph_matrix, start)

# # def dfs_recursive(root):
# # # Якщо вузол порожній, поверніть порожній список
# #     # Інакше, поверніть список: [root.value] + рекурсивний обхід лівого піддерева + рекурсивний обхід правого піддерева
# #     # pass

# # # Приклад дерева
# # class Node:
# #     def __init__(self, value, left=None, right=None):
# #         self.value = value
# #         self.left = left
# #         self.right = right

# # tree = Node(10,
# #             Node(5, Node(2), Node(7)),
# #             Node(15, None, Node(20))
# #            )

# # result = dfs_recursive(tree)
# # print("DFS рекурсивний обхід:", result)

# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right


# # Початковий код:
# def dfs_iterative(root):
#     # Ініціалізуйте стек з кореня
#     # Ініціалізуйте порожній список для збереження результатів
#     # Поки стек не порожній, дістаньте вузол, додайте його значення до результату
#     # Додайте спочатку праве, потім ліве піддерево у стек
#     pass

# # Використайте клас Node з попереднього завдання
# result = dfs_iterative(tree)
# print("DFS ітеративний обхід:", result)

#            [Київ] (Старт, dist=0)
#           /      \
#     (2 год)      (3 год)
#         /          \
#    [Житомир]     [Черкаси]
#       |             |
#    (2 год)       (3 год)
#         \          /
#        [Вінниця] (dist=4)
#             |
#          (1 год)
#             |
#       [Хмельницький] (Загальний час: 5 год)
import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes


def get_path(previous_nodes, target):
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = previous_nodes[current]

    return path[::-1]

# graph = {
#     "Київ": {
#         "Житомир": 2,
#         "Черкаси": 3
#     },

#     "Житомир": {
#         "Вінниця": 2,
#         "Хмельницький": 4
#     },

#     "Черкаси": {
#         "Вінниця": 3,
#         "Дніпро": 5
#     },

#     "Вінниця": {
#         "Хмельницький": 1
#     },

#     "Хмельницький": {},

#     "Дніпро": {}
# }


# start = "Київ"
# target = "Хмельницький"

# distances, previous_nodes = dijkstra(graph, start)

# path = get_path(previous_nodes, target)

# print("Найкоротший маршрут:")
# print(" -> ".join(path))

# print("Кількість годин:", distances[target])

# graph = {
#     "Старт": {
#         "Ліс": 5,
#         "Печера": 10
#     },

#     "Ліс": {
#         "Болота": 3,
#         "Замок": 8
#     },

#     "Печера": {
#         "Замок": 2
#     },

#     "Болота": {
#         "Бос": 6
#     },

#     "Замок": {
#         "Бос": 1
#     },

#     "Бос": {}
# }

# start = "Старт"
# target = "Бос"

# distances, previous_nodes = dijkstra(graph, start)

# path = get_path(previous_nodes, target)

# print("Найкоротший маршрут:")
# print(" -> ".join(path))

# print("Мінімальні витрати мани:", distances[target])

# graph_delivery = {
#     'Київ': {'Львів': 3, 'Дніпро': 2, 'Одеса': 4},
#     'Львів': {'Київ': 3, 'Харків': 5, 'Житомир': 2, 'Чернівці': 4, 'Ужгород': 4, 'Тернопіль': 2},
#     'Дніпро': {'Київ': 2, 'Харків': 2, 'Донецьк': 3, 'Одеса': 3, 'Запоріжжя': 2, 'Полтава': 3, 'Кременчук': 3},
#     'Одеса': {'Київ': 4, 'Дніпро': 3, 'Херсон': 2, 'Миколаїв': 3},
#     'Харків': {'Київ': 5, 'Львів': 5, 'Дніпро': 2, 'Луганськ': 2, 'Полтава': 2, 'Суми': 3, 'Донецьк': 3},
#     'Житомир': {'Київ': 2, 'Львів': 2, 'Вінниця': 2},
#     'Чернівці': {'Львів': 4, 'Хмельницький': 3, 'Івано-Франківськ': 3, 'Ужгород': 3},
#     'Ужгород': {'Львів': 4, 'Чернівці': 3},
#     'Тернопіль': {'Львів': 2, 'Хмельницький': 2, 'Івано-Франківськ': 2},
#     'Херсон': {'Одеса': 2, 'Донецьк': 4, 'Миколаїв': 1},
#     'Миколаїв': {'Одеса': 3, 'Херсон': 1, 'Донецьк': 4},
#     'Полтава': {'Харків': 2, 'Дніпро': 3, 'Кременчук': 3, 'Черкаси': 2, 'Суми': 3},
#     'Луганськ': {'Харків': 2, 'Донецьк': 2, 'Северодонецьк': 2},
#     'Донецьк': {'Дніпро': 3, 'Харків': 3, 'Херсон': 4, 'Миколаїв': 4, 'Луганськ': 2, 'Маріуполь': 3, 'Запоріжжя': 2},
#     'Вінниця': {'Житомир': 2, 'Хмельницький': 2, 'Черкаси': 3, 'Чернівці': 4},
#     'Черкаси': {'Полтава': 2, 'Кропивницький': 2, 'Вінниця': 3},
#     'Кропивницький': {'Черкаси': 2, 'Полтава': 2},
#     'Кременчук': {'Полтава': 2, 'Дніпро': 3, 'Суми': 4},
#     'Запоріжжя': {'Дніпро': 2, 'Маріуполь': 3, 'Мелітополь': 2},
#     'Маріуполь': {'Донецьк': 3, 'Запоріжжя': 3},
#     'Мелітополь': {'Запоріжжя': 2},
#     'Северодонецьк': {'Луганськ': 2},
#     'Івано-Франківськ': {'Тернопіль': 2, 'Львів': 3, 'Чернівці': 3},
#     'Суми': {'Харків': 4, 'Полтава': 3, 'Кременчук': 4},
#     'Хмельницький': {'Чернівці': 3, 'Вінниця': 2, 'Тернопіль': 2}
# }

# network_devices = {
#     'RouterA': {
#         'RouterB': 3,
#         'Switch1': 1,
#         'RouterC': 5
#     },
#     'RouterB': {
#         'RouterA': 3,
#         'Switch2': 2,
#         'RouterD': 4
#     },
#     'RouterC': {
#         'RouterA': 5,
#         'Firewall': 1
#     },
#     'RouterD': {
#         'RouterB': 4,
#         'Switch3': 2
#     },
#     'Switch1': {'RouterA': 1, 'PC1': 1, 'PC2': 2},
#     'Switch2': {'RouterB': 2, 'PC3': 3, 'PC4': 1},
#     'Switch3': {'RouterD': 2, 'PC5': 1, 'PC6': 2},
#     'Firewall': {'RouterC': 1},
#     'PC1': {'Switch1': 1},
#     'PC2': {'Switch1': 2},
#     'PC3': {'Switch2': 3},
#     'PC4': {'Switch2': 1},
#     'PC5': {'Switch3': 1},
#     'PC6': {'Switch3': 2}
# # }

# graph_flights = {
#     'KBP (Київ)': {'WAW (Варшава)': 70, 'IST (Стамбул)': 90, 'FRA (Франкфурт)': 140},
#     'WAW (Варшава)': {'KBP (Київ)': 70, 'LHR (Лондон)': 45, 'FRA (Франкфурт)': 50, 'CDG (Париж)': 60},
#     'IST (Стамбул)': {'KBP (Київ)': 90, 'DXB (Дубай)': 120, 'FRA (Франкфурт)': 110, 'JFK (Нью-Йорк)': 450},
#     'FRA (Франкфурт)': {'KBP (Київ)': 140, 'WAW (Варшава)': 50, 'IST (Стамбул)': 110, 'JFK (Нью-Йорк)': 320, 'CDG (Париж)': 40},
#     'CDG (Париж)': {'WAW (Варшава)': 60, 'FRA (Франкфурт)': 40, 'JFK (Нью-Йорк)': 280, 'LHR (Лондон)': 35},
#     'LHR (Лондон)': {'WAW (Варшава)': 45, 'CDG (Париж)': 35, 'JFK (Нью-Йорк)': 260},
#     'DXB (Дубай)': {'IST (Стамбул)': 120, 'JFK (Нью-Йорк)': 500},
#     'JFK (Нью-Йорк)': {'FRA (Франкфурт)': 320, 'CDG (Париж)': 280, 'LHR (Лондон)': 260, 'IST (Стамбул)': 450, 'DXB (Дубай)': 500}
# }

# start = "KBP (Київ)"
# target = "JFK (Нью-Йорк)"
# distances, previous_nodes = dijkstra(graph_flights, start)

# path = get_path(previous_nodes, target)

# print("Найкоротший маршрут:")
# print(" -> ".join(path))

# print("Кількість годин:", distances[target])

# def count_chars(text):
#     result = {}

#     for char in text:
#         if char in result:
#             result[char] += 1
#         else:
#             result[char] = 1

#     return result


# print(count_chars("hello"))

# import math

# class HashTable:
#     def init(self, m):
#         self.m = m
#         self.A = 0.6180339887
#         self.table = [[] for _ in range(m)]

#     def hash_function(self, k):
#         return math.floor(self.m * ((k * self.A) % 1))

#     def insert(self, key, value):
#         index = self.hash_function(key)

#         for i, (k, v) in enumerate(self.table[index]):
#             if k == key:
#                 self.table[index][i] = (key, value)
#                 return

#         self.table[index].append((key, value))

#     def search(self, key):
#         index = self.hash_function(key)

#         for k, v in self.table[index]:
#             if k == key:
#                 return v

#         return None

#     def delete(self, key):
#         index = self.hash_function(key)

#         for i, (k, v) in enumerate(self.table[index]):
#             if k == key:
#                 del self.table[index][i]
#                 return True

#         return False

#     def display(self):
#         for i, bucket in enumerate(self.table):
#             print(f"{i}: {bucket}")


# # Приклад використання
# ht = HashTable(10)

# ht.insert(15, "Яблуко")
# ht.insert(25, "Банан")
# ht.insert(35, "Апельсин")

# # print("Хеш-таблиця:")
# # ht.display()

# # print("Пошук ключа 25:", ht.search(25))

# # print("Видалення ключа 15:", ht.delete(15))

# # print("Пошук ключа 15:", ht.search(15))


# # def analyze_mod_hash(keys, m):
# #     collisions = {}

# #     for key in keys:
# #         h = key % m

# #         if h not in collisions:
# #             collisions[h] = []

# #         collisions[h].append(key)

# #     for h, bucket in collisions.items():
# #         if len(bucket) > 1:
# #             print(f"h={h}: {bucket}")


# # keys = list(range(1, 30))
# # m = 7
# # analyze_mod_hash(keys, m)

# # def get_quadratic_probe_sequence(key, m, c1, c2, steps):
# #     sequence = []

# #     for i in range(steps):
# #         pos = (key % m + c1 * i + c2 * i**2) % m
# #         sequence.append(pos)

# #     return sequence

# # print("Задача 4. Послідовність індексів:", get_quadratic_probe_sequence(key=7, m=11, c1=1, c2=3, steps=4))
# # i=0: 7; i=1: (7+1+3)%11=0; i=2: (7+2+12)%11=10; i=3: (7+3+27)%11=4 -> [7, 0, 10, 4]

# # def group_words_by_length(words):
# #     result = {}

# #     for word in words:
# #         length = len(word)

# #         if length not in result:
# #             result[length] = []

# #         result[length].append(word)

# #     return result


# # words = ["cat", "dog", "apple", "home", "car"]
# # print(group_words_by_length(words))

# # def find_winner(votes):
# #     counts = {}

# #     for name in votes:
# #         if name in counts:
# #             counts[name] += 1
# #         else:
# #             counts[name] = 1

# #     winner = max(counts, key=counts.get)
# #     return winner


# # votes = ["Олена", "Ігор", "Олена", "Андрій", "Ігор", "Олена"]

# # print(find_winner(votes))

# class PhoneBook:
#     def __init__(self):
#         self.contacts = {}

#     def add_contact(self, name, phone):
#         self.contacts[name] = phone

#     def get_phone(self, name):
#         return self.contacts.get(name)

#     def delete_contact(self, name):
#         if name in self.contacts:
#             del self.contacts[name]


# book = PhoneBook()

# book.add_contact("Олена", "0991234567")
# book.add_contact("Ігор", "0677654321")

# print(book.get_phone("Олена"))  
# print(book.get_phone("Ігор"))   
# print(book.get_phone("Андрій")) 

# book.delete_contact("Олена")

# print(book.get_phone("Олена")) 

# def coin_change(coins, amount):
#     result = {}

#     coins.sort(reverse=True)

#     for coin in coins:
#         count = amount // coin

#         if count > 0:
#             result[coin] = count
#             amount %= coin

#     return result


# coins = [25, 10, 5, 1]
# amount = 63

# print("Монети для здачі:", coin_change(coins, amount))

# import heapq
# from collections import Counter

# def huffman(text):
#     freq = Counter(text)

#     heap = []
#     for char, count in freq.items():
#         heapq.heappush(heap, (count, char, {char: ""}))

#     while len(heap) > 1:
#         f1, _, codes1 = heapq.heappop(heap)
#         f2, _, codes2 = heapq.heappop(heap)

#         for char in codes1:
#             codes1[char] = "0" + codes1[char]

#         for char in codes2:
#             codes2[char] = "1" + codes2[char]

#         new_codes = {codes1, codes2}

#         heapq.heappush(
#             heap,
#             (f1 + f2, min(codes1.keys() | codes2.keys()), new_codes)
#         )

#     codes = heap[0][2]

#     print("Коди Хаффмана:")
#     for char, code in sorted(codes.items()):
#         print(f"{char}: {code}")

#     print("Довжина коду для R:", len(codes['R']))


# text = "ABRACADABRA"
# huffman(text)