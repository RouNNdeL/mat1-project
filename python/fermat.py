import math


def factorize(n):
    x = math.ceil(math.sqrt(n))
    y = x ** 2 - n
    while not math.sqrt(y).is_integer():
        x += 1
        y = x ** 2 - n
    return x + math.sqrt(y), x - math.sqrt(y)
