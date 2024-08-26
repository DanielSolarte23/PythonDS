from animal import Animal

class Perro(Animal):
    def __init__(self, peso):
        super().__init__(peso)
    
    def ladrar(self):
        print(f"Hola soy un {type(self).__name__} y estoy ladrando")