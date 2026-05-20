def tabla(n):
    print(f"--- Tabla del {n} ---")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def todas_las_tablas():
    # imprime las tablas del 1 al 10 seguidas
    for n in range(1, 11):
        tabla(n)
        print()   # linea en blanco entre tablas

# tabla de un solo numero
tabla(7)

# o todas juntas
# todas_las_tablas()