#Write a Python program that can take a positive integer greater than 2 as input and write out 
#the number of times one must repeatedly divide this number by 2 before getting a value less than 2.

#using recursion

def factor(n):
    if n // 2 == 1 and n > 1:
        return 1
    else:
        return factor(n//2) + 1

result =  factor(4)

#confirming result
assert 2, result