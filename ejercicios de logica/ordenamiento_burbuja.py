def burbuja(lista, ascendente=True):
    nums = lista[:]   # copiamos para no modificar la lista original
    n = len(nums)

    for i in range(n):
        for j in range(0, n - i - 1):
            # comparamos pares adyacentes y los intercambiamos si estan al reves
            if ascendente:
                condicion = nums[j] > nums[j + 1]
            else:
                condicion = nums[j] < nums[j + 1]

            if condicion:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

datos = [64, 25, 12, 90, 11]
print(burbuja(datos))                    # [11, 12, 25, 64, 90]
print(burbuja(datos, ascendente=False)) # [90, 64, 25, 12, 11]