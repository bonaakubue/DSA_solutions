#Demonstrate how to use Python's list comprehension syntax 
# to produce the list[] a , b , c ,,,, z ],but without having to
# type all 26 such characters literally.

#determine the code point of the letter -a 
first = ord('a')

#determine the code point of the letter -z
last = ord('z')

letters = [chr(letter) for letter in range(first, last+1)]
print(letters)