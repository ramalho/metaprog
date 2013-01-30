
def iterativo(n):
    res = n
    for i in range(2, n):
        res *= i
    return res

def recursivo(n):
    return 1 if n < 2 else n * recursivo(n-1)

from operator import mul

def funcional(n):
    return reduce(mul, xrange(1, n+1))

