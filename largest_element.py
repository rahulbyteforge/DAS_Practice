# 1. Find Largest Element
# [10, 25, 7, 40, 15]

# Output:
# 40


arr = [10,25,7,40,15]

largest = arr[0]

for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print("The largest number in the list is: ", largest)
