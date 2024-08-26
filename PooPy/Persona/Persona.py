class Persona():
    def __init__(self, identificacion, nombre, correo):
        self.__identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        
    def getIdentificacion(self) -> str:
        return self.__identificacion
    
    def setIdentificacion(self, identificacion):
        self.__identificacion=identificacion
    
    def getNombre(self) -> str:
        return self.nombre
    
    def setNombre(self, nombre) -> None:
        self.nombre = nombre
    
    def getCorreo(self) -> str:
        return self.correo
    
    def setCorreo(self, correo) -> None:
        self.correo=correo
    
    def infoPersona(self) -> str:
        print(f"Hola mi nombre es {self.nombre} y mi correo es {self.correo}")        
