# Find Smallest Element
# [10, 25, 7, 40, 15]
# Output:
# 7





arr = [10,25,7,40,15]
smallest = arr[0]

for i in range(len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]

print("The smallest number in the list: ", smallest)