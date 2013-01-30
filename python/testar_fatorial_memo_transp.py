import fatorial
from time import time

REPETICOES = 100000

RESULTADOS = {
    1: 1,
    2: 2,
    3: 6,
    4: 24,
    5: 120,
    10: 3628800,
    20: 2432902008176640000
}

ENTRADAS = [7, 1, 5, 3, 9, 15, 11, 21, 13, 17, 19]

def memoize(fn):
    cache = fn.cache = {}

    def memoized(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    memoized.__name__ = fn.__name__
    return memoized

fatorial.iterativo = memoize(fatorial.iterativo)
fatorial.recursivo = memoize(fatorial.recursivo)

for fn in [fatorial.recursivo, fatorial.iterativo]:
    for entrada, saida in RESULTADOS.items():
        res = fn(entrada)
        assert saida == res, '%s:\t%s != %s' % (fn.__name__, saida, res)

def cronometrar(fn):
    t0 = time()
    for i in xrange(REPETICOES):
        for n in ENTRADAS:
            fn(n)
    hertz = REPETICOES / (time()-t0)  # operacoes por segundo
    print '{0}\t{1:10.3f} chamadas/s'.format(fn.__name__, hertz)

cronometrar(fatorial.recursivo)
cronometrar(fatorial.iterativo)
