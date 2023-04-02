"""
Python allows negative integers to be used as indices into a 
sequence, such as a string. If string s has length n, and expression 
s[k] is used for index -n <= k < 0, what is the 
equivalent index j >= 0 such that s[j] references the same element
"""

s = [1,2,3,4,5]
n = len(s)
num = 2
k = -num

result = s[k]
print(result)

j = n-num
result = s[j]
print(result)

