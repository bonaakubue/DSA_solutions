#Demonstrate how to use Python's list comprehension syntax to produce 
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

result = [num*(num-1) for num in range(1, 11)]
print(result)

