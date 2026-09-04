arr = [1,2,4,5,3]
issorted = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i+1]:
        issorted = False
        break
if issorted:
    print("Array is sorted ")
else:
    print("Array is not sorted ")