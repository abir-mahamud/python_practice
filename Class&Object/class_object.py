class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def anotherfunc(self):
        print("I am " + self.name)

p1 = Person("abir", 16)
p1.anotherfunc()