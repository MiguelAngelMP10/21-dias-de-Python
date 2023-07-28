from Mammal import Mammal


class Dog(Mammal):

    def __init__(self, name, age, breed, specie="dog", hasFur=True):
        super().__init__(name, age, specie, hasFur)
        self.breed = breed

    def getInfo(self):
        salida = dict()
        salida['name'] = self.name
        salida['age'] = self.age
        salida['specie'] = self.specie
        salida['hasFur'] = self.hasFur
        salida['breed'] = self.breed
        return salida

    def bark(self):
        return "woof!"
