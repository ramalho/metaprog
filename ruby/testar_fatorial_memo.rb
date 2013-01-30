require 'fatorial'
require "memoize"
include Memoize

REPETICOES = 100000

RESULTADOS = {
    1 => 1,
    2 => 2,
    3 => 6,
    4 => 24,
    5 => 120,
    10 => 3628800,
    20 => 2432902008176640000
}

ENTRADAS = [7, 1, 5, 3, 9, 15, 11, 21, 13, 17, 19]

[:iterativo, :recursivo, :funcional].each {|id|
    fn = method(id)
    RESULTADOS.each {|entrada, saida|
        res = fn.call(entrada)
        if saida != res
            print saida, " != ", res, "\n"
        end
    }
}

memoize :iterativo
memoize :recursivo
memoize :funcional

def cronometrar(id)
    fn = method(id)
    t0 = Time.new.to_f
    for i in 1..REPETICOES
        ENTRADAS.each {|n| fn.call(n)}
    end
    hertz = REPETICOES / (Time.new.to_f - t0)
    print id, " ", hertz, " chamadas/s\n"
end

cronometrar(:recursivo)
cronometrar(:iterativo)
cronometrar(:funcional)
