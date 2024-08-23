def sumaLista(listaNumeros):
    suma = 0
    for numero in listaNumeros:
        suma += numero
    return suma


numeros = [5, 8, 6, 7, 4, 9, 5, 12]
sumaNumeros = sumaLista(numeros)

print(sumaNumeros)
