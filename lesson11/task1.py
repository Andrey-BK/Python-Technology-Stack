def factorials(num):
    len = factorial(num)
    arr = []
    for i in range(len, 0, -1):
        arr.append(factorial(i))
    return arr 


def factorial(n):
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact

print(factorials(3))

