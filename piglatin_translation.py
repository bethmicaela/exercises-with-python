introduction = """\n¡Welcome to the Pig Latin translation!\n"""

def translation():
    word = (input("Enter a word: ")).lower()
    # print(word[0])
    
    first_letter = word[0]
    # print(first_letter)
    vowels = ("a", "e", "i", "o", "u")  # array -> funciona como una variable, pero guarda muchos elementos y con for i puedo entrar a cada uno de ellos.
    # print(vowels)

    for i in vowels:
        if first_letter == i:
            palabra = word[1:] + first_letter + "ay"
            return print(palabra)
        else: # ARREGLAR
            palabra = word + "way"
            return print(palabra)

if __name__ == "__main__":
    translation()