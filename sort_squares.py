def sortedSquares(arr):
    result = [0] * len(arr)

    left = 0
    right = len(arr) - 1
    pos = len(arr) - 1
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result[pos] = arr[left] ** 2
            left +=1
        else:
            result[pos] = arr[right] ** 2
            right -=1
        pos -= 1
    return result

arr = [-4, -1, 0, 3, 10]
print(sortedSquares(arr))