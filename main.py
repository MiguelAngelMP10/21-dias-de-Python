# This is a sample Python script.

from Car import Car
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    toyota = Car("Toyota", "Corolla", 2020, 0)
    toyota.turnOn()
    toyota.drive(100)
    print(toyota)