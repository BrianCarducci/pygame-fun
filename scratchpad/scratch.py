class Animal:
    def __init__(self, type, name, age):
        self.type = type
        self.name = name
        self.age = age

class Chicken(Animal):
    def __init__(self, type, name, age, sound):
        self.type = type
        self.name = name
        self.age = age
        self.sound = sound