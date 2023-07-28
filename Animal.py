class Animal:

    def __init__(self, name, age, specie):
        self.name = name
        self.age = age
        self.specie = specie

    def getInfo(self):
        salida = dict()
        salida['name'] = self.name
        salida['age'] = self.age
        salida['specie'] = self.specie
        return salida
