import math

def euklides(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

#a,b do wpisania
a = 15734
b = 65676
wynik = euklides(a,b)
print("nwd(",a,",",b,") = ",wynik[0]," = ",a,"*",wynik[1]," + ",b,"*",wynik[2])
