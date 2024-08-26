from animal import Animal

class Gato(Animal):
    def __init__(self, peso):
        super().__init__(peso)
    
    def maullar(self):
        print(f"Hola soy un {type(self).__name__} y maullo")
    