def calcular_imc(peso, altura):
    if altura <= 0 or peso <= 0:
        print("Peso y altura deben ser valores positivos.")
        return

    imc = round(peso / altura ** 2, 2)   # formula: peso / altura^2

    if imc < 18.5:
        categoria = "bajo peso"
    elif imc < 25:
        categoria = "normal"
    elif imc < 30:
        categoria = "sobrepeso"
    else:
        categoria = "obesidad"

    print(f"IMC: {imc} -> {categoria}")

calcular_imc(70, 1.75)   # IMC: 22.86 -> normal
calcular_imc(90, 1.65)   # IMC: 33.06 -> obesidad
calcular_imc(50, 1.80)   # IMC: 15.43 -> bajo peso