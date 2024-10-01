def sliding_window_max(arr, k):
    result = []
    max_value = max(arr[:k])
    result.append(max_value)
    
    i = 0
    while i < len(arr) - k:
        if arr[i + k] > max_value:
            max_value = arr[i + k]
        elif arr[i] <= max_value:
            max_value = max(arr[i+1:i+k+1])
        
        result.append(max_value)
        i += 1
    return result

i = 0
arr = [ [1, 5, 3, 2, 4, 6], [1, 2, 3, 4], [7, 7, 7, 7]]
k = [3, 2, 1]

while i < len(arr):
    print(sliding_window_max(arr[i], k[i]))
    i += 1
