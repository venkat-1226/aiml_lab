def astar(graph, h, start, goal):
    open_list = [start]
    cost = {start: 0}
    parent = {start: None}

    while open_list:
        n = min(open_list, key=lambda x: cost[x] + h[x])
        open_list.remove(n)

        if n == goal:
            path = []
            while n:
                path.append(n)
                n = parent[n]
            return path[::-1]

        for m, c in graph[n]:
            new_cost = cost[n] + c
            if m not in cost or new_cost < cost[m]:
                cost[m] = new_cost
                parent[m] = n
                open_list.append(m)

    return "Path not found"


# Test Case 1: Multiple paths
graph = {
    'S': [('A', 2), ('B', 3)],
    'A': [('G', 5)],
    'B': [('G', 2)],
    'G': []
}
h = {'S': 4, 'A': 3, 'B': 2, 'G': 0}

print("Test Case 1:", astar(graph, h, 'S', 'G'))
# Test Case 2: Direct path
graph = {
    'S': [('G', 2)],
    'G': []
}
h = {'S': 2, 'G': 0}

print("Test Case 2:", astar(graph, h, 'S', 'G'))
