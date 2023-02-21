import sys
N= int(sys.stdin.readline())
arr=[]

for i in range(N):
    age, name= map(str, sys.stdin.readline().split())
    arr.append([int(age), name])
arr.sort(key= lambda x: x[0])              
for j in range(N):
    print(arr[j][0], arr[j][1])