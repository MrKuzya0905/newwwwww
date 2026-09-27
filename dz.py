from collections import deque


class SocialGraph:
    def __init__(self):
        self.graph = {}

    def add_person(self, person):
        if person not in self.graph:
            self.graph[person] = []

    def add_connection(self, person1, person2):
        self.graph[person1].append(person2)
        self.graph[person2].append(person1)

    def bfs_distance_2(self, start):
        queue = deque([(start, 0)])
        visited = {start}
        result = []

        while queue:
            person, distance = queue.popleft()

            if distance > 0:
                result.append(person)

            if distance == 2:
                continue

            for friend in self.graph[person]:
                if friend not in visited:
                    visited.add(friend)
                    queue.append((friend, distance + 1))

        return result


g = SocialGraph()

people = ["Анна", "Богдан", "Віктор", "Ганна", "Дмитро", "Олег", "Ірина"]

for person in people:
    g.add_person(person)

g.add_connection("Анна", "Богдан")
g.add_connection("Анна", "Віктор")
g.add_connection("Богдан", "Ганна")
g.add_connection("Віктор", "Дмитро")
g.add_connection("Ганна", "Олег")
g.add_connection("Дмитро", "Ірина")

result = g.bfs_distance_2("Анна")

print("Люди на відстані не більше 2 кроків від Анни:")
print(result)