# n = 1234
# num = n
# result = 0

# while num > 0 :
#     last_digit = num % 10
#     result = (result * 10 ) + last_digit
#     num = num // 10
# if n  == result:
#     print("Yes it is a palindrome ")
# else:
#     print("No it is not a palindrome ")




def pali(n):
    num = n
    result = 0

    while num > 0:
        last_digit = num % 10
        result = ( result * 10 ) + last_digit
        num = num // 10
    if n == result:
        return("Yes it is a palindrome ")
    else:
     return("No it is not a palindrome ")
n = 1234
print(pali(n))
    