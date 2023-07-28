from Animal import Animal


class Mammal(Animal):

    def __init__(self, name, age, specie, hasFur):
        super().__init__(name, age, specie)
        self.hasFur = hasFur

    def getInfo(self):
        salida = dict()
        salida['name'] = self.name
        salida['age'] = self.age
        salida['specie'] = self.specie
        salida['hasFur'] = self.hasFur
        return salida
