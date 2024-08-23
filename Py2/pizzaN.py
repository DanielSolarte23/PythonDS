vegetariana = ["Pimiento", "Tofu"]
noVegetaria = ["Peperoni", "Jamón", "Salmón"]

opcionPizza = int(
    input("Tipo de pizza\n1.Vegetariana\n2.No Vegetariana\n Seleccione Pizza: "))

if opcionPizza==1:
    print("Ingrediente pizza vegetariana")
    print("1. ", vegetariana[0])
    print("2. ", vegetariana[1])
    ingrediente =  int(input("Seleccione ingrediente"))
    ingredientesPizza = ["Tomate", "Mozarella", vegetariana[ingrediente-1]]
else:
    print("Ingrediente pizza No vegetariana")
    print("1. ", noVegetaria[0])
    print("2. ", noVegetaria[1])
    print("3. ", noVegetaria[2])
    ingrediente =  int(input("Seleccione ingrediente 1,2,3"))
    ingredientesPizza = ["Tomate", "Mozarella", noVegetaria[ingrediente-1]]

print("Ingredientes de la pizza seleccionada\n", ingredientesPizza)