def factorial(n):
    if n < 0:
        print("Error: el factorial no esta definido para negativos.")
        return

    resultado = 1
    for i in range(2, n + 1):   # multiplicamos desde 2 hasta n
        resultado *= i

        # detectar overflow: si el numero es demasiado grande, avisamos
        if resultado > 10 ** 300:
            print("Overflow: el resultado es demasiado grande.")
            return

    return resultado

print(factorial(5))    # 120
print(factorial(10))   # 3628800
print(factorial(0))    # 1  (por definicion matematica)
print(factorial(-2))   # Error