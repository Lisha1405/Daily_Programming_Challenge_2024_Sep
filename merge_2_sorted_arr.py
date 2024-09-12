def merge(arr1, arr2):
    pointer1 = 0
    pointer2 = 0
    while pointer1 < len(arr1):  
        if arr1[pointer1] > arr2[pointer2]:
            arr1[pointer1], arr2[pointer2] = arr2[pointer2], arr1[pointer1]
            curr = arr2[pointer2]
            i = pointer2 + 1
            while i < len(arr2) and arr2[i] < curr:
                arr2[i - 1] = arr2[i]
                i += 1
            arr2[i - 1] = curr

        
        pointer1 += 1

    return arr1, arr2


i=0
array = [ [1, 3, 5], [2, 4, 6],[10, 12, 14], [1, 3, 5],[2, 3, 8],[4, 6, 10],[1],[2]]
for i in range(0,len(array), 2):
    arr1 = array[i]
    arr2 = array[i+1]
    print(merge(arr1, arr2))
 
            
        
