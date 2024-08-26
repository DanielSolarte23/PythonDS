class Alumno():
    def __init__(self, nombre:str, edad:int):
        self.nombre= nombre
        self.edad=edad
    
    def __str__(self):
        return self.nombre
    
    
class Curso():
    def __init__(self, nombre):
        self.nombre=nombre
        self.alumnos = []
    
    def matricularAlumno(self, alumno):
        if alumno not in self.alumnos:
            self.alumnos.append(alumno)
        else:
            print("El alumno ya existe")
    
    def anularMatricula(self, alumno):
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)
        else:
            print("El Alumno no existe")
        

#Implementacion

nuevoCurso = Curso("ADSO")

#crear alumnos

alumno1 = Alumno("Cata", 15)
alumno2 = Alumno("Yanfri", 23)

#Matricular Alumnos
nuevoCurso.matricularAlumno(alumno1)
nuevoCurso.matricularAlumno(alumno2)

print("Alumnos")
for a in nuevoCurso.alumnos:
    print(a)
