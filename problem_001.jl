function sum_multiples(a, b, limit)
    return sum(0:a:limit-1) + sum(0:b:limit-1) - sum(0:a*b:limit-1)
end

println(sum_multiples(3,5,1000))