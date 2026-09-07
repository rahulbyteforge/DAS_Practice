# arr = [1, 2, 3, 4, 5]
# tmep = arr[0]
# for i in range(len(arr)-1):
#     arr[i] = arr[i+1]

# arr[len(arr) - 1] = tmep
# print(arr)




#  By Function

def left_rotate(arr):
    first = arr[0]

    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]

    arr[len(arr) - 1] = first
    return arr
arr = [1,2,3,4,5]
print(left_rotate(arr))