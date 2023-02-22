import sys
N, K= map(int, sys.stdin.readline().split())
money= []
for _ in range(N):
    money.append(int(sys.stdin.readline()))

money.sort()
count=0
for i in range(N-1, -1, -1):
    if K % money[i] !=0:
        count+= K //money[i]
        K-= (K //money[i])*money[i]
        
    else:
        count+= K //money[i]
        K-= (K //money[i])*money[i]
        break
        
print(count)