import sys
num1= int(sys.argv[1])
op = sys.argv[2]
num2 = int(sys.argv[3])

if op == "+":
    print(num1 + num2)
else:
    print(
        num1 - num2 if op == "-" else
        num1* num2 if op == "*" else
        num1 / num2 if op == "/" else
        "Invalid operator"
    )
