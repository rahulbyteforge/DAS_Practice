# n = 153
# num = n
# total = 0
# no_of_digit = len(str(n))

# while num > 0 :
#     last_digit = num % 10
#     total = total + (last_digit ** no_of_digit)
#     num = num // 10
# if total == n :
#     print("It is a armstrong number ")
# else:
#     print("It is not a armstrong number ")







def arm(n):
    num = n
    total = 0
    no_of_digit = len(str(n))

    while num > 0 : 
        last_digit = num % 10
        total = total + (last_digit ** no_of_digit)
        num = num // 10
    if total == n :
        return ("Yes it is armstrong number ")
    else:
        return ("No number is not armstrong number ")
n = 153
print(arm(n))