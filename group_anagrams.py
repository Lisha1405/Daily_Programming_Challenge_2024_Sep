def groupAnagrams(str):
    groups = []
    keys = []
    for s in str:
        string = ''.join(sorted(s))
        found = False
        for i in range(len(keys)):
            if keys[i] == string:
                groups[i].append(s)
                found = True
                break
        if not found:
            keys.append(string)
            groups.append([s])
    return groups
i=0
arr = [ ["eat", "tea", "tan", "ate", "nat", "bat"], [""],["a"],
       ["abc", "bca", "cab", "xyz", "zyx", "yxz"],["abc", "def", "ghi"]]
while i<5:
    print(groupAnagrams(arr[i]))
    i+=1

