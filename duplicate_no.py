def duplicate_num(arr):  
   n = len(arr) - 1 
   sum = n * (n + 1) // 2
   sum_arr=0
   for i in arr:
        sum_arr+=i
   return sum_arr - sum
    
i=0
array = [ [1, 3, 4, 2, 2],  [3, 1, 3, 4, 2], [1,1],[1, 4, 4, 2, 3]]
while i<4:
    arr = array[i]
    print(duplicate_num(arr))
    i+=1
array_last_testcase = []  
for j in range (1,1000000):
    array_last_testcase.append(j)
array_last_testcase.append(5000)
print(duplicate_num(array_last_testcase))

