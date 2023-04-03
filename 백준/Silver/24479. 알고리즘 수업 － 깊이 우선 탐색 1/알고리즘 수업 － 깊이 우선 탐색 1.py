# 백준24479. 알고리즘 수업 - 깊이 우선 탐색 1
# 1에서 다음으로 갈 수 있는 정점이 궁금한 문제가 아닌, 12345가 각각 몇 번째 순서로 출력되는지가 궁금한 문제

# 파이썬의 기본 재귀 깊이 한계는 1000이다.
# 따라서 재귀 허용 깊이를 수동으로 늘려주는 코드를 사용해야 한다.
import sys
sys.setrecursionlimit(10 ** 6)  

n,m,r= map(int,sys.stdin.readline().split())

#방문 순서 그래프 (보기 편하게 1번 노드와 인덱스 값을 같게 했다. )
graph=[[] for _ in range(n+1)]
visted =[0]*(n+1)

# 방문 순서를 기록하기 위해 만든 변수
count= 1

# index 1에는 1이 갈 수 있는 정점들을 볼 수 있다. 
# [[], [4, 2], [1, 3, 4], [2, 4], [1, 2, 3], []] --> 변경 전
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 오름차순으로 방문하는 조건을 가지고 있다. 
# [[], [2, 4], [1, 3, 4], [2, 4], [1, 2, 3], []] --> 변경 후
for i in range(n+1):
    graph[i].sort()

# global을 통해 함수 안에서 전역 변수를 수정하고,그 값을 함수 밖에서도 사용할 수 있다. 

def dfs(graph,v,visted):
    global count          
    visted[v]= count
    #연결된 노드 방문
    for i in graph[v]:
        #방문 안한 노드일 경우
        if visted[i]== 0:
            count+=1 # 1 방문 순서 기록
            dfs(graph,i,visted)

dfs(graph,r,visted)

for i in range(n+1):
    if i!=0:
        print(visted[i])