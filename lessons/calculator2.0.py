number1 = float(input("Gebe die erste Zahl ein: "))
number2 = float(input("Gebe die zweite Zahl ein: "))
operation = input("Welche Operation (+, -, *, /) soll durchgeführt werden?: ")

if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
else:
    print("Ungültige Operation ...")
