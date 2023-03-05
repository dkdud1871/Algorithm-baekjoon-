n= int(input())
result=[]
for i in range(n):
    num= int(input())
    a= sorted(list(map(str, input().split())))
    b= sorted(list(map(str, input().split())))
    if a==b:
        result.append('NOT CHEATER')
    else:
        result.append('CHEATER')
print(*result, sep='\n')