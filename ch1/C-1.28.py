#The p-norm of a vector v = (v1,v2,...,vn) in n-dimensional space is defined as:
#Give an implementation of a function named norm such that norm(v, p) returns the 
# p-norm value of v and norm(v) returns the Euclidean norm of v. 
# You may assume that v is a list of numbers.


def p_norm(v, p):
    result = (sum([num**p for num in v]))**(1/p)
    return result


def norm(v):
    result = (sum([num**2 for num in v]))**(1/2)
    return result

v = [1,2,3,4,5]
p = 3
result = p_norm(v,p)
print(result)

v = (4,3)
result = norm(v)
print(result)