# arr = [1,2,3,4,5]
# temp =  arr[len(arr) - 1]

# for i in range(len(arr) -1,0,-1):
#     arr[i] = arr[i-1]

# arr[0] = temp
# print(arr)




#  By Function

def right_rotate(arr):
    last = arr[len(arr) - 1]

    for i in range(len(arr) -1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = last
    return arr

arr = [1,2,3,4,5]
print(right_rotate(arr))