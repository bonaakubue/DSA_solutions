#Write a Python program that outputs all possible strings formed 
# by using the characters c , a , t , d , o ,and g exactly once.

#Using recursion
chars = ['c' , 'a' , 't' , 'd' , 'o' ,'g']
def word_generator(chars, i=0):
    char_count = len(chars)
    if i == char_count:
        result =  "".join(chars)
        print(result)
    for j in range(i, char_count):
            chars[i], chars[j] = chars[j], chars[i]
            word_generator(chars, i+1)
        
result = word_generator(chars)
print(result)



