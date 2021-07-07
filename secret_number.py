import random

def number():
    random_number = random.randint(1, 100)
    random_username = (int(input("Enter a number from 1 to 100: ")))

    while random_number != random_username:
        if random_number < random_username:
            random_username = (int(input("Choose a smaller number: ")))
        else:
            random_username = (int(input("Choose a bigger number: ")))
        
    print("Correct")

    

if __name__ == "__main__":
    number()