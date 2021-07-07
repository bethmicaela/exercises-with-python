def prime():

    contador = 0

    for i in range(1, 10):
        if i == 1:
            continue
        elif contador % i == 0:
            contador +=1
        elif contador == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    prime()

# ESTA MAL LA LOGICA Y NO FUNCIONA