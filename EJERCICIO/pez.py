from animal import Animal

class Pez(Animal):
    def __init__(self, peso):
        super().__init__(peso)
    
    def nadar(self):
        print(f"Hola soy un {type(self).__name__} y estoy nadando")
    
        