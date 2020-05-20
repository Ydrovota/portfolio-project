
class Car:

    def __init__(self, name="", age=(2018 - 2012), carcolor=""):
        self.name = name
        self.age = age
        self.carcolor = carcolor

    def age(self, str):
        print("" + str)

mycar = Car()

print(mycar.age)
