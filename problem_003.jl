function get_factor(x, f)
    while x % f == 0
        println(f)
        x = x/f
    end
    return x
end

function prime_factors(x)
    primes = [2]
    i = 2
    x = get_factor(x, i)
    while i < x
        i += 1
        for j = primes
            if i%j==0
                break
            elseif j>sqrt(i) || j == last(primes)
                push!(primes, i)
                x = get_factor(x, i)
                break
            end
        end
    end
end


prime_factors(600851475143)
