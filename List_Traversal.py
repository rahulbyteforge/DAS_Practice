# 1


# n = [1,2,3,4,5]
# for i in range(len(n)):
#     print(n[i])



#  2

# n = [1,2,3,4,5]
# for i in range(len(n)):
#     if n[i]  % 2 == 0:
#         print(n[i])






#  3

# n = [1,2,3,4,5]
# sum  = 0
# for i in range(len(n)):
#     sum += n[i]
# print(sum)



#  4

# n = [1,2,3,4,5]

# largest = n[0]

# for i in range(len(n)):
#     if n[i] > largest:
#         largest = n[i]
# print(largest)





#  5


# n = [1,2,3,4,5]

# smallest = n[0]

# for i in range(len(n)):
#     if n[i] < smallest:
#         smallest = n[i]
# print(smallest)





#  6



arr = [10, 25, 30, 45, 50]
target = 30

for i in range(len(arr)):
    if arr[i] == target:
        print("Found")
        break
