def divisors(n):
    count = 0
    i = 1
    while i*i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
        i += 1
    return count

i = 0
array = [18, 29, 100, 1, 997]
while i < 5:
    arr = array[i]
    print(divisors(arr))
    i += 1
