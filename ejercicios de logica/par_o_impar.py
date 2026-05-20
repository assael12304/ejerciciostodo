def par_o_impar(numero):
    # el operador % devuelve el resto de la division
    # si el resto al dividir entre 2 es 0, el numero es par
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

# prueba — funciona con negativos y cero tambien
print(par_o_impar(4))    # par
print(par_o_impar(7))    # impar
print(par_o_impar(0))    # par
print(par_o_impar(-3))   # impar