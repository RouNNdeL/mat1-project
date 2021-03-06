import math

def pollard(n):
    #funkcja g(x) = (x^2 + 1) mod n
    x_fixed = 2
    cycle_size = 2
    x = 2
    factor = 1

    while factor == 1:
        count = 1
        while count <= cycle_size and factor <= 1:
            x = (x * x + 1) % n
            factor = math.gcd(x - x_fixed, n)
            count += 1
        cycle_size *= 2
        x_fixed = x
    print("nietrywialny czynnik to: ",factor)
    return factor

