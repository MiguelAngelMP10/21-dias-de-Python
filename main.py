# This is a sample Python script.

from Car import Car
from product import Product
from User import User

from Animal import Animal
from Dog import Dog
from Mammal import Mammal

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    toyota = Car("Toyota", "Corolla", 2020, 0)
    toyota.turnOn()
    toyota.drive(100)
    print(toyota.mileage)


    class Article(Product):
        def __init__(self, name, price, quantity):
            super().__init__(name, price, quantity)

        def addToCart(self):
            return f"Agregando {self.quantity} unidades del articulo {self.name}"


    class Service(Product):
        def __init__(self, name, price, quantity):
            super().__init__(name, price, quantity)

        def addToCart(self):
            return f"Agregando el servicio {self.name} al carrito"


    class Cart:
        def __init__(self):
            self.products = []

        def addProduct(self, product):
            product.addToCart()
            self.products.append(product)

        def deleteProduct(self, product):
            self.products = [item for item in self.products if item.name != product.name]

        def calculateTotal(self):
            total = sum(item.price * item.quantity for item in self.products)
            return total

        def getProducts(self):
            return self.products


    book = Article("Libro", 100, 2)
    course = Service("Curso", 120, 1)

    cart = Cart()
    cart.addProduct(book)
    cart.addProduct(course)
    total = cart.calculateTotal()
    print(total)

    usuario1 = User("Juan", 20)
    usuario2 = User("Maria", 25)
    usuario3 = User("Pedro", 30)
    usuario4 = User("Lina", 25)

    print(usuario1.name, usuario1.age)
    print(usuario2.name, usuario2.age)

    usuario1.addFriend(usuario2)
    usuario1.addFriend(usuario3)
    usuario1.addFriend(usuario4)
    print(usuario1.getFriends())

    usuario1.sendMessage("Hola Maria!", usuario2)
    print(usuario1.showMessages())

    # Playground - Jerarquía de animales usando herencia
    bird = Animal("pepe", 1, "bird")
    print(bird.getInfo())

    hippo = Mammal("bartolo", 3, "hippo", False)
    print(hippo.getInfo())

    dog = Dog("fido", 4, "pastor aleman");
    print(dog.bark())
    print(dog.getInfo())
