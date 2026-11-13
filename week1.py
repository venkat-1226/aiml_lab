
from collections import deque

# Test Case 1: Connected Graph
g1 = {'A':['B','C'], 'B':['D'], 'C':['E'],
      'D':[], 'E':[]}

# Test Case 2: Disconnected Graph
g2 = {'A':['B','C'], 'B':[], 'C':[],
      'D':['E'], 'E':[]}

def bfs(g, start):
    q = deque([start])
    visited = {start}
    print("BFS:", end=" ")
    while q:
        n = q.popleft()
        print(n, end=" ")
        for x in g[n]:
            if x not in visited:
                visited.add(x)
                q.append(x)
    print()

def dfs(g, n, visited=None):
    if visited is None:
        visited = set()
        print("DFS:", end=" ")
    visited.add(n)
    print(n, end=" ")
    for x in g[n]:
        if x not in visited:
            dfs(g, x, visited)
    if n == 'A':
        print()

print("Test Case 1: Connected Graph")
bfs(g1, 'A')
dfs(g1, 'A')

print("\nTest Case 2: Disconnected Graph")
bfs(g2, 'A')
dfs(g2, 'A')