import sys
if len(sys.argv)==4:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print("Addition of two numbers:", num1 + num2)
    print("Subtraction of two numbers:", num1 - num2)
    print("Multplication of two numbers:", num1 * num2)
    print("Division of two numbers:",  num1 / num2)
else:
    num1 = 2
    num2 = 4
    print("Invalid try again")
