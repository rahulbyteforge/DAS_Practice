def duplicates(arr):
    j = 1

    for i in range(1,len(arr)):
        if arr[i] != arr[i - 1]:
            arr[j] = arr[i]
            j+=1
    return j
arr = [1,1,2,2,3,3,4]
k = duplicates(arr)
print("Unique element ", arr[:k])
print("Length: ",k)