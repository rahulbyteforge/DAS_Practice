arr = [2,5,8,11,14]
Even = 0
odd = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        Even+=1
    else:
        odd+=1
print("Even: ",Even)
print("Odd: ",odd)