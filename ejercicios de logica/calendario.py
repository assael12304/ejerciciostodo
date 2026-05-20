import calendar

def mostrar_calendario(mes, anio):
    # validacion basica de entrada
    if not (1 <= mes <= 12):
        print("Mes invalido. Ingresa un valor entre 1 y 12.")
        return
    if anio < 1:
        print("Anio invalido.")
        return

    # calendar.month() devuelve el calendario del mes como texto
    # los dias quedan alineados de lunes a domingo automaticamente
    cal = calendar.month(anio, mes)
    print(cal)

mostrar_calendario(5, 2025)
#       May 2025
# Mo Tu We Th Fr Sa Su
#           1  2  3  4
#  5  6  7  8  9 10 11
# 12 13 14 15 16 17 18
# 19 20 21 22 23 24 25
# 26 27 28 29 30 31

mostrar_calendario(13, 2025)   # Mes invalido