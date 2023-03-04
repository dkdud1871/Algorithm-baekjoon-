N,M = map(int, input().split())
arr= sorted(list(map(int,input().split())))
sum=[]
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if arr[i]+arr[j]+arr[k] <= M:
                sum.append(arr[i]+arr[j]+arr[k])
sum.sort()
print(sum[-1])