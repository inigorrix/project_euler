function primes(x)
    primes_list = [2]
    i = 1
    while i < x-1
        i += 2
        for j in primes_list
            if i%j==0
                break
            elseif j>sqrt(i) || j == last(primes_list)
                push!(primes_list, i)
                break
            end
        end
    end
    return primes_list
end

primes_list = primes(2e6)
println(sum(primes_list))