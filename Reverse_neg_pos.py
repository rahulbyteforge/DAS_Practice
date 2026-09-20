def reverse(x):
    sing = 1
    
    if x < 0:
        sing = -1
        x = -x

    rev = 0
    while x > 0:
        digit = x % 10
        rev = rev * 10 + digit
        x = x // 10
    return sing * rev

print(reverse(123))
print(reverse(-123))
print(reverse(120))


