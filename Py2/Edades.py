edades = []

for i in range(5):
    edad = int(input("Ingrese edad de la persona: "))
    edades.append(edad)

menor=min(edades)
mayor=max(edades)
print(f"la mayor de las edades es ${mayor}")
print(f"la menor de las edades es ${menor}")
print(edades)
