#Write a short Python program that takes two arrays a and b of length n storing 
# int values, and returns the dot product of a and b. That is, it
#returns an array of c for length n such that c[i] = a[i],b[i], for i=0,,,,,n-1.


def dot_product(arr1, arr2):
    if len(arr1) == len(arr2):
        n =  len(arr1)
        result =[arr1[i]*arr2[i] for i in range(n)]
        return result

array1 = [1,2,3,4,5]
array2 = [2,2,2,2,2]
result = dot_product(array1, array2)
print(result)
