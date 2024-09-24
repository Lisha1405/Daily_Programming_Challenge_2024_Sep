def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a,b):
    return (a*b)//gcd(a,b)

i=0
array = [[4,6],[5,10],[7,3],[1,987654321], [123456,789012]]
while i<5:
    a,b= array[i]
    print(lcm(a,b))
    i+=1
