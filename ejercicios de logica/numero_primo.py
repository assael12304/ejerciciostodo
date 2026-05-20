import math

def es_primo(n):
    if n < 2:
        return False   # por definicion, los primos son >= 2

    # solo verificamos divisores hasta la raiz cuadrada de n
    # si n no tiene divisores hasta ahi, no los tendra despues
    limite = int(math.sqrt(n)) + 1

    for i in range(2, limite):
        if n % i == 0:
            return False   # encontramos un divisor: no es primo

    return True

print(es_primo(7))    # True
print(es_primo(12))   # False
print(es_primo(97))   # True
print(es_primo(1))    # False