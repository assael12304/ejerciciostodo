def clasificar_edad(edad):
    # usamos elif para revisar los rangos en orden
    # Python evalua de arriba hacia abajo y se detiene en el primero que se cumpla
    if edad < 0:
        return "edad invalida"
    elif edad <= 2:
        return "infante"
    elif edad <= 12:
        return "nino"
    elif edad <= 17:
        return "adolescente"
    elif edad <= 64:
        return "adulto"
    else:
        return "senior"

print(clasificar_edad(1))    # infante
print(clasificar_edad(10))   # nino
print(clasificar_edad(15))   # adolescente
print(clasificar_edad(40))   # adulto
print(clasificar_edad(70))   # senior