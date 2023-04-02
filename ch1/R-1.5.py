#Give a single command that computes the sum from Exercise R-1.4, 
#relying on Pythons comprehension syntax and the builtin sum function.

num = 5
squares = sum([i**2 for i in range(num)])
print(squares)