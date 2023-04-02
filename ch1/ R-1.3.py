"""Write a short Python function, minmax(data), that takes a sequence 
of one or more numbers, and returns the smallest and largest numbers, 
in the form of a tuple of length two. Do not use the built-in functions 
min or max in implementing your solution.
"""

def minmax(data):
    min_num = max_num = data[0]
    for num in data:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num

    return(min_num, max_num)


#Testing

nums = [6,1,2,7,4,5]
result = minmax(nums)
print(result)
