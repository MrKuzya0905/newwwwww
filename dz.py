import json

def load_graph(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def dfs_component(graph, vertex, visited, component):
    visited.add(vertex)
    component.append(vertex)

    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            dfs_component(graph, neighbor, visited, component)

def find_components(graph):
    visited = set()
    components = []

    for vertex in graph:
        if vertex not in visited:
            component = []
            dfs_component(graph, vertex, visited, component)
            components.append(component)

    return components

def dfs_cycle(graph, vertex, visited, parent, path):
    visited.add(vertex)
    path.append(vertex)

    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            cycle = dfs_cycle(graph, neighbor, visited, vertex, path)

            if cycle:
                return cycle

        elif neighbor != parent:
            cycle_start = path.index(neighbor)
            return path[cycle_start:] + [neighbor]

    path.pop()
    return None

def find_cycle(graph):
    visited = set()

    for vertex in graph:
        if vertex not in visited:
            cycle = dfs_cycle(graph, vertex, visited, None, [])

            if cycle:
                return cycle

    return None

graph = load_graph("graph.json")

print("Граф:")
for vertex, neighbors in graph.items():
    print(f"{vertex}: {neighbors}")

components = find_components(graph)

print("\nЗв'язні компоненти:")

for i, component in enumerate(components, 1):
    print(f"Компонента {i}: {component}")


if len(components) == 1:
    print("\nГраф є зв'язним.")
else:
    print("\nГраф не є зв'язним.")


cycle = find_cycle(graph)

if cycle:
    print("\nУ графі знайдено цикл:")
    print(" -> ".join(cycle))
else:
    print("\nЦиклів у графі немає.")