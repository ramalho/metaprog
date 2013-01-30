
def iterativo(n)
    f = 1
    for i in 1..n
        f *= i
    end
    f
end

def recursivo(n)
    n < 2 ? 1 : n * recursivo(n-1)
end

def funcional(n)
    (1..n).reduce(:*)
end
