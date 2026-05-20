def es_bisiesto(anio):
    # regla oficial del calendario gregoriano:
    # divisible por 4 -> bisiesto, SALVO si es divisible por 100
    # pero si ademas es divisible por 400 -> bisiesto de nuevo
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print(f"{anio} es bisiesto")
    else:
        print(f"{anio} no es bisiesto")

es_bisiesto(2024)   # es bisiesto
es_bisiesto(1900)   # no es bisiesto (div por 100 pero no por 400)
es_bisiesto(2000)   # es bisiesto (div por 400)
es_bisiesto(2023)   # no es bisiesto