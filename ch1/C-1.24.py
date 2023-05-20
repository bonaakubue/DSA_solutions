#Write a short Python function that counts the number of vowels in a given character string.

vowels = ['a', 'e', 'i', 'o', 'u']

str1 = 'Hello how are you doing?'
result = len([vowel for vowel in str1 if vowel in vowels])
print(result)