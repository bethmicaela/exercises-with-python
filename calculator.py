introduction = """\nWelcome to the python calculator\n"""
print(introduction)

def calculator():

    n1 = (int(input("Enter a number: ")))
    operator = (input("Enter the operator: "))
    n2 = (int(input("Enter other number: ")))

    addition = "+"
    subtraction = "-"
    multiplication = "*"
    division = "/"
    
    if operator == addition:
        print(n1 + n2)
    elif operator == subtraction:
        print(n1 - n2)
    elif operator == multiplication:
        print(n1 * n2)
    elif operator == division:
        if n1 == 0 or n2 == 0:
            print("Can't divide by zero")
        print(n1 / n2)
    else:
        print("Enter an addition, subtraction, multiplication or division")


if __name__ == "__main__":
    calculator()