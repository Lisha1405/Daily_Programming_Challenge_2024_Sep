def repeat(arr, k):
    count = {}
    
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    for num in arr:
        if count[num] == k:
            return num
    
    return -1

i = 0
arr = [([3, 1, 4, 4, 5, 2, 6, 1, 4], 2),  ([2, 3, 4, 2, 2, 5, 5], 2),
       ([1, 1, 1, 1], 1),([10], 1),([6, 6, 6, 6, 7, 7, 8, 8, 8], 3)]

while i < len(arr):
    array, k = arr[i]
    print(repeat(array, k))
    i += 1
