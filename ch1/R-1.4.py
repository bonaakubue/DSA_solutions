#Write a short Python function that takes a positive integer n 
# and returns the sum of the squares of all the positive 
# integers smaller than n.

def func(n):
    if n > 0:
        squares = sum([i**2 for i in range(n)])
    return squares


#Testing
num = 5
result = func(num)
print(result)
