def analizar_texto(texto):
    vocales    = "aeiou"
    v = c = e = 0   # contadores: vocales, consonantes, espacios

    for letra in texto.lower():   # lower() convierte todo a minuscula
        if letra == " ":
            e += 1
        elif letra in vocales:
            v += 1
        elif letra.isalpha():       # isalpha() filtra signos de puntuacion
            c += 1
        # si no es ninguno de los anteriores (puntuacion, etc.) lo ignoramos

    print(f"Vocales    : {v}")
    print(f"Consonantes: {c}")
    print(f"Espacios   : {e}")

analizar_texto("Hola, mundo!")
# Vocales    : 4
# Consonantes: 6
# Espacios   : 1