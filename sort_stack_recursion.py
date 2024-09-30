def sort_stack(stack):
    if not stack:
        return
    top = stack.pop()
    sort_stack(stack)
    insert(stack, top)

def insert(stack, elmt):
    if not stack or stack[-1] <= elmt:
        stack.append(elmt)
        return
    top = stack.pop()
    insert(stack, elmt)
    stack.append(top)


i = 0
arr = [[7, 1, 5], [5], [-3, 14, 8, 2], [], [3, 3, 3]]
while i < len(arr):
    sort_stack(arr[i])
    print(arr[i])
    i += 1
