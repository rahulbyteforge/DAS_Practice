# n = 123456

# num = n
# count = 0

# while num > 0:
#     count+=1
#     num = num  // 10

# print(count)




#  By Function


def cot(n):
    num = n
    count = 0
    while num > 0:
        count+=1
        num = num // 10
    return count
n = 123456
print(cot(n))