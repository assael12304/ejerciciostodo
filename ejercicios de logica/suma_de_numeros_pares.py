# version con for
def suma_pares_for(n):
    total = 0
    for i in range(2, n + 1, 2):   # range de 2 en 2 da solo los pares
        total += i
    return total

# version con while
def suma_pares_while(n):
    total = 0
    i = 2                 # empezamos en el primer par
    while i <= n:
        total += i
        i += 2            # avanzamos de dos en dos
    return total

print(suma_pares_for(10))     # 2+4+6+8+10 = 30
print(suma_pares_while(10))   # 30