#
#Write a Python program that can simulate a simple calculator, using the console as the 
# exclusive input and output device. That is, each input to the calculator, be it a 
# number, like 12.34 or 1034, or an operator, like + or =, can be done on a separate line. 
# After each such input, you should output to the Python console what would be 
# displayed on your calculator.


num1 = int(input())
operation = input()
num2 = int(input())
result = 0
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "x" or operation == "X" or operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2

print(result)
