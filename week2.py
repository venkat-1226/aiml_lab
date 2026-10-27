def a_star(graph, h, start, goal):
    open_set = {start}
    closed_set = set()
    g = {start: 0}
    parent = {start: start}

    while open_set:
        n = min(open_set, key=lambda x: g[x] + h[x])

        if n == goal:
            path = []
            while parent[n] != n:
                path.append(n)
                n = parent[n]
            path.append(start)
            path.reverse()
            return path

        open_set.remove(n)
        closed_set.add(n)

        for m, cost in graph[n]:
            new_cost = g[n] + cost

            if new_cost < g.get(m, float('inf')):
                g[m] = new_cost
                parent[m] = n

                if m in closed_set:
                    closed_set.remove(m)

                open_set.add(m)

    return "Path not found"


# Test Case 1: Admissible Heuristics
print("Test Case 1: Admissible Heuristics")

graph = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 2)],
    'G': []
}

h = {
    'S': 5,
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 1,
    'G': 0
}

print("Path:", a_star(graph, h, 'S', 'G'))


# Test Case 2: Multiple Possible Paths
print("\nTest Case 2: Multiple Possible Paths")

graph = {
    'S': [('A', 2), ('B', 3)],
    'A': [('C', 2), ('G', 8)],
    'B': [('C', 1), ('D', 4)],
    'C': [('G', 3)],
    'D': [('G', 2)],
    'G': []
}

h = {
    'S': 5,
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 1,
    'G': 0
}

print("Path:", a_star(graph, h, 'S', 'G'))


# Test Case 3: Direct Start to Goal
print("\nTest Case 3: Direct Start to Goal")

graph = {
    'S': [('G', 2)],
    'G': []
}

h = {
    'S': 2,
    'G': 0
}

print("Path:", a_star(graph, h, 'S', 'G'))


# Test Case 4: Goal Not Reachable
print("\nTest Case 4: Goal Not Reachable")

graph = {
    'S': [('A', 1)],
    'A': [('B', 2)],
    'B': [],
    'G': []
}

h = {
    'S': 3,
    'A': 2,
    'B': 1,
    'G': 0
}

print("Path:", a_star(graph, h, 'S', 'G'))


# Test Case 5: Misleading Heuristics
print("\nTest Case 5: Misleading Heuristics")

graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('G', 8)],
    'B': [('G', 2)],
    'G': []
}

h = {
    'S': 5,
    'A': 1,
    'B': 6,
    'G': 0
}

print("Path:", a_star(graph, h, 'S', 'G'))