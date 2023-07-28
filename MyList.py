class MyList:
    def __init__(self):
        self.data = dict()
        self.length = 0

    def append(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        if self.length > 0:
            dato_eliminado = self.data[self.length - 1]
            self.data.pop(self.length - 1)
            self.length -= 1
            return dato_eliminado

    def shift(self):
        if self.length > 0:
            dato_eliminado = self.data[0]
            self.data.pop(0)
            self.length -= 1
            for i in range(1, self.length + 1):
                self.data[i - 1] = self.data[i]
            self.data.pop(self.length)
            self.data = dict(sorted(self.data.items()))
            return dato_eliminado

    def unshift(self, item):
        for i in range(self.length, 0, -1):
            self.data[i] = self.data[i - 1]
        self.data[0] = item
        self.length += 1

    def map(self, func):
        salida = MyList()
        for i in range(self.length):
            salida.append(func(self.data[i]))
        return salida

    def filter(self, func):
        salida = MyList()
        for i in range(self.length):
            if func(self.data[i]) == True:
                salida.append(self.data[i])
        return salida

    def join(self, character=","):
        salida = ""
        for i in range(self.length):
            salida += str(self.data[i]) + character
        return salida[0:-1]
