class Persona():
    def __init__(self, identificacion:int, nombre:str, correo:str):

        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__correo = correo
        
    def getIdentificacion(self) -> str:
        return self.__identificacion
    
    def setIdentificacion(self, identificacion):
        self.__identificacion=identificacion
    
    def getNombre(self) -> str:
        return self.__nombre
    
    def setNombre(self, nombre) -> None:
        self.__nombre = nombre
    
    def getCorreo(self) -> str:
        return self.__correo
    
    def setCorreo(self, correo) -> None:
        self.__correo=correo
    
    def saludar(self):
            print(f"Desde Persona... Hola soy un objeto de tipo {type(self).__name__}")
    # def infoPersona(self) -> str:
    #     print(f"Hola mi nombre es {self.nombre} y mi correo es {self.correo}")        
