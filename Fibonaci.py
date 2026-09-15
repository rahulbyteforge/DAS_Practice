def fibonacci(n):
    a = 5
    b = 6

    for i in range(n):
        print(a, end=" ")
        c = a + b
        b = a
        a = c
    return a
n = int(input("Enter a number: "))
print(fibonacci(n))