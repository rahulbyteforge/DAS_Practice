arr = [2,3,2,5,2,7]
target = 2
count = 0
for i in range(len(arr)):
    if arr[i] == target:
        count+=1
print(count)