def find_missing(arr):
    if len(arr)>10**6:
        return "Input arr too long"
    n = len(arr) + 1
    sum = n * (n + 1) // 2
    sum_arr=0
    for i in arr:
        sum_arr+=i
    if sum - sum_arr == 0 :
        return "No missing element"
    return sum - sum_arr

i=0
array = [ [1, 2, 4, 5], [2, 3, 4, 5], [1, 2, 3, 4],[1]]
while i<4:
    arr = array[i]
    print(find_missing(arr))
    i+=1
array_last_testcase = []  
for j in range (1,1000000):
    array_last_testcase.append(j)
print(find_missing(array_last_testcase))
array_last_testcase = []  
for j in range (1,10000000):
    array_last_testcase.append(j)
print(find_missing(array_last_testcase))