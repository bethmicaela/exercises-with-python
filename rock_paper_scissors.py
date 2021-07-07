player1 = (input("Gamer 1 -> Enter rock, paper or scissors: ")).lower()
player2 = (input("Gamer 2 -> Enter rock, paper or scissors: ")).lower()

def run(gamer1, gamer2):

    rock = "rock"
    paper = "paper"
    scissors = "scissors"

    if gamer1 == paper and gamer2 == rock:
        print("The winner is Gamer 1")
    elif gamer1 == rock  and gamer2 == paper:
        print("The winner is Gamer 2")
    elif gamer1 == rock and gamer2 == scissors: 
        print("The winner is Gamer 1")
    elif gamer1 == scissors and gamer2 == rock:
        print("The winner is Gamer 2")
    elif gamer1 == paper and gamer2 == scissors:
        print("The winner is Gamer 2")
    elif gamer1 == scissors and gamer2 == paper:
        print("The winner is Gamer 1")
    else:
        print("Enter rock paper or scissors please")


if __name__ == "__main__":
    run(player1, player2)