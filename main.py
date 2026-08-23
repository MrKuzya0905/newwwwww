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
#     count = 0

#     for _ in range(len(lst) - 1):
#         swapped = False

#         for i in range(len(lst) - 1):
#             if lst[i] > lst[i + 1]:
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#                 count += 1
#                 swapped = True

#         print(lst)

#         if not swapped:
#             break

#     print("Кількість замін:", count)
#     return lst


# numbers = [5, 2, 9, 1, 7]

# bubble_sort(numbers)
# print(numbers)

# def bubble_sort_by_age(lst):
#     for _ in range(len(lst) - 1):
#         swapped = False

#         for i in range(len(lst) - 1):
#             if lst[i]['age'] > lst[i + 1]['age']:
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#                 swapped = True

#         if not swapped:
#             break

#     return lst


# people_data = [
#     {'name': 'Bob', 'age': 25},
#     {'name': 'Alice', 'age': 30},
#     {'name': 'Charlie', 'age': 20}
# ]

# bubble_sort_by_age(people_data)

# print(people_data)

# def bubble_sort(lst):
#     count = 0

#     for _ in range(len(lst) - 1):
#         swapped = False

#         for i in range(len(lst) - 1):
#             if lst[i] > lst[i + 1]:
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#                 count += 1
#                 swapped = True

#         print(lst)

#         if not swapped:
#             break

#     print("Кількість замін:", count)
#     return lst

def selection_sort(arr) -> None:
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n - 1):
        idx_min_number = i

        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[idx_min_number]:
                idx_min_number = j

        if idx_min_number != i:
            swaps += 1
            print(f"Знайдено мінімум: {arr[idx_min_number]}")
            print(f"Міняємо {arr[i]} і {arr[idx_min_number]}")

            arr[i], arr[idx_min_number] = arr[idx_min_number], arr[i]
            

            print("Список після заміни:", arr)
            print()

    print("Відсортований список:", arr)
    print("Compa4risons: ", comparisons)


numbers = [5, 7, 1, 3, 2, 8, 12, 5, 3, 7, 8]

selection_sort(numbers)