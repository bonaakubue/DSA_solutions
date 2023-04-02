#Give a single command that computes the sum from Exercise R-1.6, 
# relying on Pythons comprehension syntax and the built-in sum function.

num = 10
squares = sum([i**2 for i in range(num) if i % 2 != 0])

print(squares)