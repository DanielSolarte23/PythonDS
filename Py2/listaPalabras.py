palabras = []

for i in range(10):
    palabra = input("Ingresa una palabra: ")
    palabras.append(palabra)
    
palabraBuscar = input("Ingrese la palabra a buscar: ")

if palabraBuscar in palabras:
    cantidad = palabras.count(palabraBuscar)
    print(f"La palabra '{palabraBuscar}' está en la lista y aparece {cantidad} veces en la lista.")
    print(f"Lista de palabras: {palabras}")
else:
    print("La palabra no está en la lista.")
