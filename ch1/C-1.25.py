#Write a short Python function that takes a strings,representing a sentence, and 
#returns a copy of the string with all punctuation removed. For example, 
#if given the string "Let s try, Mike.", this function would return "Lets try Mike".

def strip_punctuations(str1):
    stripped = []
    for char in str1:
        if char.isalnum() or char == " ":
            stripped.append(char)

    return "".join(stripped)


result = strip_punctuations('hello, how are you?')
print(result)