n= int(input())
a= sorted(list(map(int, input().split())))
b= list(map(int, input().split()))
sum=0
for i in range(n):
    sum += a[i]*max(b)
    del b[b.index(max(b))]
print(sum)