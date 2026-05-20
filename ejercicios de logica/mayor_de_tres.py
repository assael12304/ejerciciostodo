def mayor_de_tres(lista):
    maximo = max(lista)   # encontramos el valor mas alto

    # contamos cuantos elementos son iguales al maximo
    repetidos = lista.count(maximo)

    if repetidos > 1:
        print(f"El mayor es {maximo} (aparece {repetidos} veces)")
    else:
        print(f"El mayor es {maximo}")

mayor_de_tres([5, 12, 8])    # El mayor es 12
mayor_de_tres([9, 9, 3])     # El mayor es 9 (aparece 2 veces)
mayor_de_tres([7, 7, 7])     # El mayor es 7 (aparece 3 veces)