# arr = [10,25,7,40,15]
# largest = arr[0]
# second_largest = arr[0]

# for i in range(len(arr)):
#     if arr[i] > largest:
#         second_largest = largest
#         largest = arr[i]
#     elif arr[i] > second_largest and arr[i] != largest:
#         second_largest = arr[i]
# print (second_largest)





arr = [10, 25, 7, 40, 15]

smallest = arr[0]
second_smallest = arr[0]

for i in range(len(arr)):
    if arr[i] < smallest:
        second_smallest = smallest
        smallest = arr[i]
    elif  arr[i] < second_smallest:
        second_smallest = arr[i]
print(smallest)
print(second_smallest)