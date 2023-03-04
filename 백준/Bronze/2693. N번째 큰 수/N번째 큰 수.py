n= int(input())
arr=[]
for _ in range(n):
    arr.append(sorted(list(map(int, input().split()))))
a=[]
for i in range(n):
    a.append(arr[i][-3])
print(*a, sep='\n')