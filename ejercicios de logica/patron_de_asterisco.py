def triangulo(n, invertido=False):
    if invertido:
        # empieza con n asteriscos y va bajando
        for i in range(n, 0, -1):
            print("*" * i)
    else:
        # empieza con 1 asterisco y va subiendo
        for i in range(1, n + 1):
            print("*" * i)

# triangulo normal
triangulo(5)
# *
# **
# ***
# ****
# *****

print()

# triangulo invertido
triangulo(5, invertido=True)
# *****
# ****
# ***
# **
# *