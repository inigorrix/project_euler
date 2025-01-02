function sum_even_fibo(x)
    a, b, c = 1, 1, 2
    sum = 0
    while c<x
        #println(c)
        sum += c

        a = b + c
        b = c + a
        c = a + b
    end
    return sum
end

println(sum_even_fibo(4e6))

