lines = readlines("problem_0067_triangle.txt")

# Convert each line into a vector of integers and store in a vector of vectors
data = [parse.(Int, split(line)) for line in lines]

len = length(data) - 1
solved = data[1:len]

for i = 1:len
    k = len + 1 - i
    for j = 1:length(solved[k])
        solved[k][j] += max(data[k+1][j], data[k+1][j+1])
    end
end

# display(solved)
println(solved[1][1])
