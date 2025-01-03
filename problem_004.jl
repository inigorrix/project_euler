function max_palind(limit)
    max_p = 0
    prod = 1, 1

    for i = 1:limit
        for j = i:limit
            n = i * j
            if string(n)==reverse(string(n)) && n > max_p
                max_p = n
                prod = i, j
            end
        end
    end
    return max_p, prod
end

println(max_palind(999))
