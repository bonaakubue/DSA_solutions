"""Write a short Python function, is even(k), that takes an integer value 
# and returns True if k is even, and False otherwise. However, your function 
# cannot use the multiplication, modulo, or division operators.
"""

def is_even(k):
    #using bit values
    if k & 1 == 0:
        return True
    else:
        return False


#Testing
assert is_even(4)
# assert is_even(3)