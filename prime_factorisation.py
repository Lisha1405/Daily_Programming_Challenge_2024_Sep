import math
def prime_factor(num):
    x =int(math.sqrt(num))+1
    factors = []
    for i in range(2, x,1):
        while num%i == 0 :
            factors.append(i)
            num = num/i
    if num>1:
        factors.append(int(num))
    return factors

i = 0
array = [30,49,19,64,123456]
while i < 5:
    arr = array[i]
    print(prime_factor(arr))
    i += 1