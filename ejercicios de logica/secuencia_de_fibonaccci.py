def fibonacci(n):
    if n <= 0:
        print("Ingresa un numero positivo.")
        return

    a, b = 0, 1   # los dos primeros terminos

    for _ in range(n):
        print(a)           # imprimimos el termino actual
        a, b = b, a + b    # avanzamos: el nuevo par es (b, a+b)

fibonacci(8)
# 0  1  1  2  3  5  8  13