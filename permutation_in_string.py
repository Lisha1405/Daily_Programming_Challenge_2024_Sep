def permutation_in_string(str):
    permuation = {''}
    for char in str:
        new_permuation = set()  

        for perm in permuation:
            for i in range(len(perm) + 1):
                new_string = perm[:i] + char + perm[i:]
                new_permuation.add(new_string)
        permuation = new_permuation

    return list(permuation)

i=0
array = [ "abc", "aab", "aaa","a", "abcd"]
while i<5:
    arr = array[i]
    print(permutation_in_string(arr))
    i+=1