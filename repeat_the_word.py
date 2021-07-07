introduction = """\n¡REPEAT A WORD!\n"""
print(introduction)

word = (input("Enter a word: "))
amount = (int(input("Enter the number of repetitions from 1 to 100: ")))

def run(word_user, amount_user):

    count = 0
    while count < amount_user:
        print(word_user)
        count += 1

if __name__ == "__main__":
    run(word, amount)