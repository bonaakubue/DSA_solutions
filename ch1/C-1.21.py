#Write a Python program that repeatedly reads lines from standard input until 
# an EOFError is raised, and then outputs those lines in reverse order 
# (a user can indicate end of input by typing ctrl-D).

data = []

try:
    while True:
        value = input('write something: ')
        data.append(value)
except EOFError:
    pass
finally:
    data.reverse()

print(data)

