def find_leaders(arr):
    max= arr[-1]
    
    leaders = []
    leaders.append(max)
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>max:
            max = arr[i]
            leaders.append(max)
    leaders.reverse()
    return leaders
i=0
array = [  [1, 2, 3, 4, 0], [7, 10, 4, 10, 6, 5, 2], [5], [100, 50, 20, 10]]
while i<4:
    arr = array[i]
    print(find_leaders(arr))
    i+=1
array_last_testcase = [] 
for j in range (1,1000001):
    array_last_testcase.append(j)
print(find_leaders(array_last_testcase)) 
