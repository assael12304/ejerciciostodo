def convertir(valor, direccion):
    # 1 metro = 3.28084 pies
    if direccion == "m2ft":
        resultado = valor * 3.28084
        return round(resultado, 4)
    elif direccion == "ft2m":
        resultado = valor / 3.28084
        return round(resultado, 4)
    else:
        print('Direccion invalida. Usa "m2ft" o "ft2m".')
        return None

print(convertir(1, "m2ft"))    # 3.2808 pies
print(convertir(10, "ft2m"))   # 3.048 metros
print(convertir(5, "km2m"))    # Direccion invalida