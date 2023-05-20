#Write a short Python function that takes a sequence of integer values and determines 
# if there is a distinct pair of numbers in the sequence whose product is odd.

def func(seq):
    first = seq[0]
    for num in range(1, len(seq)):
        second = seq[num]
        if (first * second) % 2 != 0:
            return True
        first =  second

        return False


result = func([1,2,3,4,5,5,7])
print(result)
