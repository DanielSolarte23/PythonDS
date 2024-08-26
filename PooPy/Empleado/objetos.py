from empleado import Empleado
from empresa import Empresa

elSena = Empresa("SENA")

elSena.agregarEmpleado("Martin Rojas", "Director Regional", 7000000)

elSena.agregarEmpleado("Pablo Ortiz", "Instructor", 5000000)

elSena.agregarEmpleado("Monik Galindo", "Tesorera", 5250000)

print(f"Lista de Empleado de la empresa {elSena}")

for empleado in elSena.getEmplead