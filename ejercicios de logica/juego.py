import random

def juego_adivinar():
    secreto   = random.randint(1, 100)
    intentos  = 0
    max_intentos = 10

    print("Adivina el numero entre 1 y 100. Tienes 10 intentos.")

    while intentos < max_intentos:
        intento = int(input(f"Intento {intentos + 1}: "))
        intentos += 1

        if intento == secreto:
            print(f"Has ganado en {intentos} intento(s).")
            return
        elif intento < secreto:
            print("El numero es mayor.")
        else:
            print("El numero es menor.")

    # si sale del while sin adivinar, mostrar el numero correcto
    print(f"Fin del juego. El numero era {secreto}.")

juego_adivinar()