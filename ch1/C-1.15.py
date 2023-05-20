#Write a Python function that takes a sequence of numbers and determines if all 
# the numbers are different from each other (that is, they are distinct).

def func(seq):
    if len(seq) == len(set(seq)):
        return True
    return False


nums = [1,2,3,4,5]
result = func(nums)
print(result)