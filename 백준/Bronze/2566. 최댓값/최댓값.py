arr=[]
arr_max=[]
for _ in range(9):
    arr.append(list(map(int, input().split())))
for i in range(9):
    a= arr[i]
    arr_max.append(max(a))
arr_location= [[i+1,j+1] for i in range(9) for j in range(9) if arr[i][j]==max(arr_max)]
print(max(arr_max))    
print(arr_location[0][0],arr_location[0][1] )    