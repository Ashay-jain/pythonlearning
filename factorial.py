def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 4
factorial = factorial(num)
print("factorial of",num, "is",factorial)