import random
import string

def generar_contrasena(longitud=12, simbolos=True, numeros=True, mayusculas=True):
    # construimos el grupo de caracteres disponibles
    chars = list(string.ascii_lowercase)   # minusculas siempre incluidas
    obligatorios = []                       # al menos uno de cada tipo pedido

    if mayusculas:
        chars += list(string.ascii_uppercase)
        obligatorios.append(random.choice(string.ascii_uppercase))

    if numeros:
        chars += list(string.digits)
        obligatorios.append(random.choice(string.digits))

    if simbolos:
        chars += list(string.punctuation)
        obligatorios.append(random.choice(string.punctuation))

    # rellenamos el resto hasta llegar a la longitud deseada
    resto = longitud - len(obligatorios)
    clave = obligatorios + [random.choice(chars) for _ in range(resto)]

    random.shuffle(clave)   # mezclamos para que los obligatorios no queden al inicio
    return "".join(clave)

print(generar_contrasena(12))
print(generar_contrasena(8, simbolos=False))