function sum_even_fibo(x)
    a, b, c = 1, 1, 2
    total = 0
    while c<x
        #println(c)
        total += c

        a = b + c
        b = c + a
        c = a + b
    end
    return total
end

println(sum_even_fibo(4e6))

