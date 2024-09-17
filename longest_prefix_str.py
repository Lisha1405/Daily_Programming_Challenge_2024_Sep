def longest_prefix_str(arr_str):
    if not arr_str:
        return ""
    for i in range(len(arr_str[0])):
        char = arr_str[0][i]        
        for s in arr_str[1:]: 
            if i >= len(s) or s[i] != char:
                return arr_str[0][:i]
    return arr_str[0]


loop_var = 0
arr = [["flower", "flow", "flight"],["dog", "racecar", "car"],["apple", "ape", "april"],[""],["alone"]]
while loop_var<5:

    print(longest_prefix_str(arr[loop_var])) 
    loop_var+=1
