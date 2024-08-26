from Persona import Persona

class Instructor (Persona):
    def __init__(self, identificacion, nombre, correo, especialidad):
        super().__init__(identificacion, nombre, correo)
        self.__especialidad=especialidad
    
    def getEspecialidad(self):
        return self.__especialidad
    
    def setEspecialidad(self, especialidad):
        self.__especialidad = especialidad
        def saludar(self):
            print(f"Desde Instructor... Hola soy un objeto de tipo {type(self).__name__}")