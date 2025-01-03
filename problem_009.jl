function pyt_triplet(x)
    for a = 1:Int(trunc(x/3))
        for b = a:Int(trunc(x/2))
            c = x - a - b
            if a^2 + b^2 == c^2
                return a, b, c
            end
        end
    end
    return "Not found"
end

a, b, c = pyt_triplet(1000)
println(a*b*c)