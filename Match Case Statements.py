a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter operator (+, -, /, *): ")

match c:
    case '+':
        d = a + b
    case '-':
        d = a - b
    case '/':
        if b != 0:  # Ensure denominator is not zero for division
            d = a / b
        else:
            print("Error: Division by zero!")
            exit()  # Exit the program if division by zero is attempted
    case '*':
        d = a * b
    case _:
        print("You have not entered a valid operator.")

print("{} {} {} = {}".format(a, c, b, d))
