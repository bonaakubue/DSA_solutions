#Write a short program that takes as input three integers, a, b, and c, 
# from the console and determines if they can be used in a correct arithmetic 
# formula (in the given order), like "a+b = c," "a = b-c," or "a*b = c."

def calc(n=3):
    count = 0
    numbers = []
    while count < n:
        value = int(input('Enter a number: '))
        numbers.append(value)
        count+=1
    a,b,c = tuple(numbers)
    if a+b == c:
        print("a + b = c")
    elif a == b - c:
        print("a = b - c")
    elif a * b == c:
        print("a x b = c")
    else:
        print("Nothing to show!")


calc()
