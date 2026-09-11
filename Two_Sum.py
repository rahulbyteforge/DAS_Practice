# arr = [2, 7, 11, 15]
# target = 9


def Tow_Sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                return [i , j]
    return []
arr = [2,7,11,15]
target = 9

print(Tow_Sum(arr , target))



# hashing


def two_sum(arr, target):
    seen = {}

    for i in range(len(arr)):
        needed = target - arr[i]
        if needed in seen:
            return [seen[needed], i]
        seen[arr[i]] = i
    return []
arr = [2, 7, 11, 15]
target = 9

print(two_sum(arr, target))