def countAtMostKDistinct(s, k):
    l = 0
    total_substrings = 0
    char_set = set()
    char_count = {}

    for r in range(len(s)):
        char_set.add(s[r])
        char_count[s[r]] = char_count.get(s[r], 0) + 1

        while len(char_set) > k:
            char_count[s[l]] -= 1
            if char_count[s[l]] == 0:
                char_set.remove(s[l])
            l += 1

        total_substrings += r - l + 1

    return total_substrings

def count_substring_k_diff_char(s, k):
    return countAtMostKDistinct(s, k) - countAtMostKDistinct(s, k - 1)

i=0
array = [["pqpqs", 2], ["aabacbebebe", 3], ["a", 1],["abc", 3], ["abc", 2]]
while i<5:
    s,k = array[i]
    print(count_substring_k_diff_char(s,k))
    i+=1
