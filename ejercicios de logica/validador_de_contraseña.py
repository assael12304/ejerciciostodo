def validar_contrasena(clave):
    errores = []   # lista donde acumulamos los problemas encontrados

    if len(clave) < 8:
        errores.append("Minimo 8 caracteres")

    # any() recorre la cadena y devuelve True si encuentra al menos uno
    if not any(c.isupper() for c in clave):
        errores.append("Falta una mayuscula")

    if not any(c.islower() for c in clave):
        errores.append("Falta una minuscula")

    if not any(c.isdigit() for c in clave):
        errores.append("Falta un numero")

    return errores   # lista vacia = contrasena valida

problemas = validar_contrasena("abc123")
print(problemas)
# ['Minimo 8 caracteres', 'Falta una mayuscula']

print(validar_contrasena("MiClave99"))   # [] (valida)