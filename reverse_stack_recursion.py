def reverse_stack(stack):
    if not stack:
        return
    top = stack.pop()
    reverse_stack(stack)
    insert(stack, top)

def insert(stack, item):
    if not stack:
        stack.append(item)
    else:
        top = stack.pop()
        insert(stack, item)
        stack.append(top)

i = 0
arr = [[3, 2, 1],[5],[-5, -10, -15],[],[3, 3, 3]]

while i < len(arr):
    array = arr[i]
    reverse_stack(array)
    print(array)
    i += 1
