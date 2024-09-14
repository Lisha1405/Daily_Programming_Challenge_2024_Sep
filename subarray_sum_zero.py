def subarray_sum_zero(arr):
    sum_dict = {}
    sum = 0
    result = []
    for i in range(len(arr)):
        sum += arr[i]        
        if sum == 0:
            result.append((0, i))
        if sum in sum_dict:
            previous_indices = sum_dict[sum]
            for j in previous_indices:
                result.append((j + 1, i))
        if sum in sum_dict:
            sum_dict[sum].append(i)
        else:
            sum_dict[sum] = [i]
    
    return result

i=0
array = [[4, -1, -3, 1, 2, -1],[1, 2, 3, 4], [0, 0, 0],  [-3, 1, 2, -3, 4, 0], ]
while i<4:
    arr = array[i]
    print(subarray_sum_zero(arr))
    i+=1  
last_testcase = [1, -1, 2, -2, 3, -3] * (10**4)
print(subarray_sum_zero(last_testcase))