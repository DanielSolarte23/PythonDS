from Persona import Persona

class Aprendiz(Persona):
    def __init__(self, identificacion, nombre, correo, puntajeIcfes):
        super().__init__(identificacion, nombre, correo)
        self.__puntajeIcfes = puntajeIcfes
        
    def getPuntajeIcfes(self):
        return self.__puntajeIcfes
    
    def setPuntajeIcfes(self, puntajeIcfes):
        self.__puntajeIcfes= puntajeIcfes
        
    def saludar(self):
            print(f"Desde Aprendiz... Hola soy un objeto de tipo {type(self).__name__}")