function get_factor(x, f)
    n = 0
    while x % f == 0
        x = x/f
        n += 1
    end
    return x, n
end

function prime_factors(x)
    primes = [2]
    factors = Dict{Int,Int}()
    i = 2
    x, n = get_factor(x, i)
    if n > 0
        factors[i] = n
    end
    i = 1
    while i < x
        i += 2
        for j = primes
            if i%j==0
                break
            elseif j>sqrt(i) || j == last(primes)
                push!(primes, i)
                x, n = get_factor(x, i)
                if n > 0
                    factors[i] = n
                end
                break
            end
        end
    end
    return factors
end

function common_prime_factors(nums)
    factors = Dict{Int,Int}()
    for i = nums
        f = prime_factors(i)
        for j in f
            if haskey(factors, j[1]) && j[2] > factors[j[1]]
                factors[j[1]] = j[2]
            elseif !haskey(factors, j[1])
                factors[j[1]] = j[2]
            end
        end
    end
    return factors
end

function lcm(nums)
    factors = common_prime_factors(nums)
    result = 1
    for i in factors
        result *= i[1]^i[2]
    end
    return result
end


println(lcm(1:20))
