#Had we implemented the scale function (page 25) as follows, does it work properly?
def scale(data, factor): 
    for val in data:
        val = factor
#Explain why or why not.

#It will work very well but you have to append the val into a new list

def scale(data, factor): 
    new_data = []
    for val in data:
        val *= factor
        new_data.append(val)

    return new_data

nums = [1,2,3,4,5]
result = scale(nums, 2)
print(result)