import random

introduction = """\nWelcome to password generator, enter an option for security:\n
1- Lower case and upper case
2- numbers
3- special characters\n"""

menu = (input(introduction + "Enter an option: "))
length = (input("Enter a length: "))

def generator():
    # lista1 = [123, 'xyz', 'zara'] # lista
    # print(len(lista1))

    option_1 = ("a", "b", "c", "d", "e", "A", "B", "C", "D", "E")
    # option_2 = ("1", "2", "3", "4", "5")
    # option_3 = ("?", "-", "=", "!", ",")

    if menu == "1":
        random.choice(option_1)

if __name__ == "__main__":
    generator()