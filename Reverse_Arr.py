# 2. Reverse an Array ⭐

# Concept: Traversal / Two Pointers

# Question:
# Given an array, reverse the array in-place without creating another array.

# Example:

# Input:  [1, 2, 3, 4, 5]

# Output: [5, 4, 3, 2, 1]


def Reverse(arr):
    i = 0
    j = len(arr) - 1

    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i+=1
        j-=1
    return arr
arr = [1,2,3,4,5]
print(Reverse(arr))

