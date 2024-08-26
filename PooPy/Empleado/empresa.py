from empleado import Empleado

class Empresa():
    def __init__(self, nombre:str):
        self.__nombre=nombre
        self.__Empleado=[]
        
    def agregarEmpleado(self, nombre:str, cargo:str, sueldo:int):
        empleado= Empleado(nombre=nombre, cargo=cargo, sueldo= sueldo)
        self.__empleados.append(empleado)
        
    def getNombre(self)->str:
        return self.__nombre
    
    def getEmplead(self) ->list:
        return self.__empleados
    
    def __str__(self) ->str:
        return self.__nombre
    
    def __del__(self):
        print("Eliminado")
        
    
        