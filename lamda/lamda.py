# python lamda

x = lambda a, b : a + b
print(x(5, 6))


def myfunc(n):
    return lambda a: a * n

doubler = myfunc(2)
trippler = myfunc(3)

print(doubler(10))
print(trippler(11))