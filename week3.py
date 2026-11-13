
from itertools import permutations

# Travelling Salesman Problem
def tsp(distance):
    n = len(distance)
    best_cost = float("inf")
    best_route = None

    for p in permutations(range(1, n)):
        route = (0,) + p + (0,)
        cost = sum(distance[route[i]][route[i+1]]
                   for i in range(n))

        if cost < best_cost:
            best_cost = cost
            best_route = route

    return best_route, best_cost


# Test Case 1: Complete Graph
d1 = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

route, cost = tsp(d1)
print("TSP Test Case 1: Complete Graph")
print("Shortest Path:", route)
print("Minimum Cost:", cost)

# Test Case 3: Single Node Graph
d2 = [[0]]

route, cost = tsp(d2)
print("\nTSP Test Case 3: Single Node Graph")
print("Shortest Path:", route)
print("Minimum Cost:", cost)


# Graph Coloring Problem
def graph_coloring(graph, colors):
    result = {}

    for node in graph:
        for color in colors:
            if all(result.get(n) != color for n in graph[node]):
                result[node] = color
                break
        else:
            return "Coloring not possible"

    return result


# Test Case 1: Triangle Graph
g1 = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

print("\nGraph Coloring Test Case 1: Triangle Graph")
print(graph_coloring(g1, ['Red', 'Blue', 'Green']))


# Test Case 2: Bipartite Graph
g2 = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}

print("\nGraph Coloring Test Case 2: Bipartite Graph")
print(graph_coloring(g2, ['Red', 'Blue']))
