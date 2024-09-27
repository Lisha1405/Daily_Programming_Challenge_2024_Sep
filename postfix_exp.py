def postfix(expr):
    ip = expr.split()
    stack = []
    for i in ip:
        if i.isdigit() or (i[0] == '-'  and i[1:].isdigit()):
            stack.append(int(i))
        else:
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(int(a / b))  
            elif i == '^':
                stack.append(a**b)
            else:
                print("Invalid operator")
                return None
    return stack.pop()

i=0
array= ["5 6 +","3 4 2 * 1 5 - 2 3 ^ ^ / +","-5 6 -","15 7 1 1 + - / 3 * 2 1 1 + + -"]
while i<len(array):
    print(postfix(array[i]))
    i+=1

