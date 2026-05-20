def cajero():
    saldo          = 1000.0   # saldo inicial
    limite_retiro  = 500.0    # maximo permitido por dia
    retirado_hoy   = 0.0      # acumulado de retiros en la sesion

    while True:   # el bucle continua hasta que el usuario elija salir
        print("\n1. Ver saldo   2. Depositar   3. Retirar   4. Salir")
        opcion = input("Opcion: ")

        if opcion == "1":
            print(f"Saldo actual: ${saldo:,.2f}")

        elif opcion == "2":
            monto = float(input("Monto a depositar: $"))
            if monto <= 0:
                print("Monto invalido.")
            else:
                saldo += monto
                print(f"Deposito aceptado. Nuevo saldo: ${saldo:,.2f}")

        elif opcion == "3":
            monto = float(input("Monto a retirar: $"))
            if monto <= 0:
                print("Monto invalido.")
            elif monto > saldo:
                print("Fondos insuficientes.")
            elif retirado_hoy + monto > limite_retiro:
                disponible = limite_retiro - retirado_hoy
                print(f"Limite diario alcanzado. Puedes retirar hasta ${disponible:,.2f} mas.")
            else:
                saldo        -= monto
                retirado_hoy += monto
                print(f"Retiro exitoso. Saldo: ${saldo:,.2f}")

        elif opcion == "4":
            print("Hasta luego.")
            break   # break termina el while True
        else:
            print("Opcion no valida.")

cajero()