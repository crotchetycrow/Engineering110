
class Dog:

    def __init__(self, name, colour):
        self.animal_kind = "Canine"
        self.name = name
        self.colour = colour
        self.bark()

    def bark(self):
        return "Woof! Woof!"


fido = Dog("Lucky", "Brown")

print(fido.name)
print(fido.colour)
print(fido.animal_kind)
print(fido.bark())
