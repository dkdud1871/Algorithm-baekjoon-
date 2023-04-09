from collections import deque
import sys

n, m, r = map(int, sys.stdin.readline().split())
visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
count = 1

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()


def bfs(graph, start, visited):
    global count
    queue = deque([start])
    visited[start] = count

    while queue:
        v = queue.popleft()
        for j in graph[v]:
            if visited[j] == 0:
                queue.append(j)
                count += 1
                visited[j] = count


bfs(graph, r, visited)

for i in range(1, n + 1):
    print(visited[i])
