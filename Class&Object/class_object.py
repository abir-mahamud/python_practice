class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def anotherfunc(self):
        print("I am " + self.name)

p1 = Person("abir", 16)
p1.anotherfunc()

class Student:
    def __init__(kaka, name, roll):
        kaka.name = name
        kaka.roll = roll

    def anofunc(lala):
        print("Hello my name is " + lala.name)

t1 = Student("abir", 25521)
t1.anofunc()