def fibonacci(n):
    a, b = 0, 1
    while a < n:
        c = a + b
        yield a
        a, b = b, c


# for x in fibonacci(1000):
#     print(x)