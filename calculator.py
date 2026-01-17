import sys

if len(sys.argv) == 2:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    print("Addition of two numbers:", num1 + num2)
    print("Subtraction of two numbers:", num1 - num2)
    print("Multiplication of two numbers:", num1 * num2)

    if num2 != 0:
        print("Division of two numbers:", num1 / num2)
    else:
        print("Division not possible (division by zero)")
else:
    print("Invalid input")
 
