def longest_substring(str):
    char_set = set()
    start, length = 0, 0
    
    for e in range(len(str)):
        while str[e] in char_set:
            char_set.remove(str[start])
            start += 1
        char_set.add(str[e])
        length = max(length, e - start + 1)
    
    return length
i=0
array = ["abcabcbb","bbbbb", "pwwkew","abcdefgh", "a"]
while i<5:
    arr = array[i]
    print(longest_substring(arr))
    i+=1
