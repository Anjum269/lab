 import sys

a = int(sys.argv[1])
op = sys.argv[2]
b = int(sys.argv[3])

if op == "+":
    print(a + b)
else:
    print(
        a - b if op == "-" else
        a * b if op == "*" else
        a / b if op == "/" else
        "Invalid operator"
    )
