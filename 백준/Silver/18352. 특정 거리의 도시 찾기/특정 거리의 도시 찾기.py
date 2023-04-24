import sys
from collections import deque

input= sys.stdin.readline

n, m, k, x = map(int, input().split())
visited= [0]* (n+1)
graph= [[] for _ in range(n+1)]


for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
# graph= [[], [2,3], [3,4],[]] 이런식으로 받아짐
    
result=[] # 최단거리가 k인 도시 받아서 마지막에 출력할 예정

def bfs(x):
    queue= deque([x])
    visited[x]= 1
    
    while queue:
        v= queue.popleft()
        if visited[v]== k+1:
            result.append(v)
            continue
        for i in graph[v]:
            if visited[i]==0:
                queue.append(i)
                visited[i] = visited[v]+1
                
bfs(x)
if len(result)==0:
    print(-1)
else:
    result.sort()
    print(*result, sep='\n')
        
    