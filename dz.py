import matplotlib.pyplot as plt
import math

# 1

class MyHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.collisions = 0

    def hash_function(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        index = self.hash_function(key)

        if self.table[index]:
            self.collisions += 1

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return

        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)

        for k, v in self.table[index]:
            if k == key:
                return v

        return None

    def delete(self, key):
        index = self.hash_function(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True

        return False


keys = [f"key{i}" for i in range(100)]

for size in [5, 10, 20, 50, 100]:
    ht = MyHashTable(size)

    for key in keys:
        ht.add(key, "value")

    print(f"Розмір таблиці: {size}")
    print(f"Кількість колізій: {ht.collisions}")
    print()


# 2

def mod_hash(key, m):
    return key % m


def multiplicative_hash(key, m, A):
    return math.floor(m * ((key * A) % 1))


keys = list(range(1, 1001))
m = 20
A = 0.6180339887

mod_results = [mod_hash(k, m) for k in keys]

mult_results = [
    multiplicative_hash(k, m, A)
    for k in keys
]

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(mod_results, bins=range(m + 1), edgecolor="black")
plt.title("Модульне гешування")
plt.xlabel("Геш-значення")
plt.ylabel("Кількість ключів")

plt.subplot(1, 2, 2)
plt.hist(mult_results, bins=range(m + 1), edgecolor="black")
plt.title("Мультиплікативне гешування")
plt.xlabel("Геш-значення")
plt.ylabel("Кількість ключів")

plt.tight_layout()
plt.show()

# 3

def multiplicative_hash(key, m, A):
    return math.floor(m * ((key * A) % 1))


def analyze_distribution(keys, m, A):
    counts = [0] * m

    for key in keys:
        index = multiplicative_hash(key, m, A)
        counts[index] += 1

    average = len(keys) / m

    variance = sum(
        (count - average) ** 2 for count in counts
    ) / m

    print(f"Розмір таблиці: {m}")
    print(f"Константа A: {A}")
    print(f"Мінімальна кількість: {min(counts)}")
    print(f"Максимальна кількість: {max(counts)}")
    print(f"Дисперсія: {variance:.2f}")
    print()


keys = list(range(1, 1001))

for m in [10, 20, 50, 100]:
    for A in [0.5, 0.6180339887, 0.75]:
        analyze_distribution(keys, m, A)

# 4

class PhoneBook:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, name):
        return sum(ord(char) for char in name) % self.size

    def add_contact(self, name, phone):
        index = self.hash_function(name)

        for i, (n, p) in enumerate(self.table[index]):
            if n == name:
                self.table[index][i] = (name, phone)
                return

        self.table[index].append((name, phone))
        print("Контакт додано!")

    def search_contact(self, name):
        index = self.hash_function(name)

        for n, p in self.table[index]:
            if n == name:
                return p

        return None

    def delete_contact(self, name):
        index = self.hash_function(name)

        for i, (n, p) in enumerate(self.table[index]):
            if n == name:
                del self.table[index][i]
                print("Контакт видалено!")
                return

        print("Контакт не знайдено!")

    def show_contacts(self):
        for bucket in self.table:
            for name, phone in bucket:
                print(f"{name}: {phone}")


book = PhoneBook()

while True:
    print("\n--- ТЕЛЕФОННА КНИГА ---")
    print("1. Додати контакт")
    print("2. Знайти контакт")
    print("3. Видалити контакт")
    print("4. Показати всі контакти")
    print("5. Вийти")

    choice = input("Оберіть дію: ")

    if choice == "1":
        name = input("Введіть ім'я: ")
        phone = input("Введіть номер телефону: ")
        book.add_contact(name, phone)

    elif choice == "2":
        name = input("Введіть ім'я: ")
        result = book.search_contact(name)

        if result:
            print("Номер телефону:", result)
        else:
            print("Контакт не знайдено!")

    elif choice == "3":
        name = input("Введіть ім'я: ")
        book.delete_contact(name)

    elif choice == "4":
        book.show_contacts()

    elif choice == "5":
        print("Завершення програми.")
        break

    else:
        print("Неправильний вибір!")