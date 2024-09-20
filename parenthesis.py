def parenthesis(str):
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in str:
        if char in bracket_map:
            top_element = stack.pop() if stack else 'no'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)

    return len(stack)==0
i=0
array = ["()","([)]", "[{()}]", "","{[}"]
while i<5:
    arr = array[i]
    print(parenthesis(arr))
    i+=1
