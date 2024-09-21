def checking_str(str, left, right):
    while left >= 0 and right < len(str) and str[left] == str[right]:
        left -= 1
        right += 1
    return str[left + 1:right]

def longestPalindrome(str):
    longest_palindrome = ""
    
    for i in range(len(str)):
        palindrome_odd = checking_str(str, i, i)
        if len(palindrome_odd) > len(longest_palindrome):
            longest_palindrome = palindrome_odd
        
        palindrome_even = checking_str(str, i, i + 1)
        if len(palindrome_even) > len(longest_palindrome):
            longest_palindrome = palindrome_even
    
    return longest_palindrome

i = 0
array = ["babad", "cbbd", "a", "aaaa", "abc"]
while i < 5:
    arr = array[i]
    print(longestPalindrome(arr))
    i += 1

