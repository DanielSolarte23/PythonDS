class Animal():
    def __init__(self, peso) :
        self.peso = peso
    
    def respirar(self):
        print(f"soy un {type(self).__name__} Estoy  respirando y que")
        