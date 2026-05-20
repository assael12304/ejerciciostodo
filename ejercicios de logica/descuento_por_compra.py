def aplicar_descuento(precio):
    # primero verificamos el descuento mayor (es mas restrictivo)
    if precio > 100:
        descuento = precio * 0.10   # 10%
    elif precio > 50:
        descuento = precio * 0.05   # 5%
    else:
        descuento = 0               # sin descuento

    precio_final = precio - descuento
    return round(precio_final, 2)   # dos decimales

print(aplicar_descuento(150))   # 135.0  (10% de descuento)
print(aplicar_descuento(75))    # 71.25  (5% de descuento)
print(aplicar_descuento(30))    # 30     (sin descuento)