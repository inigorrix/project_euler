function difference_squares(x)
    result = sum(1:x)^2
    for i = 1:x
        result -= i^2
    end
    return result
end

println(difference_squares(100))
