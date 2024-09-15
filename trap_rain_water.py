def trap_water(arr):
    if not arr:
        return 0
    if len(arr)<3:
        return 0

    left, right = 0, len(arr) - 1
    left_max, right_max = arr[left], arr[right]
    trap = 0

    while left < right:
        if arr[left] < arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                trap += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                trap += right_max - arr[right]
            right -= 1

    return trap

i=0
array = [  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], [4, 2, 0, 3, 2, 5], [1, 1, 1],[5],[2, 0, 2]]
while i<5:
    arr = array[i]
    print(trap_water(arr))
    i+=1
