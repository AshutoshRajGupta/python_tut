# del keyword - used to delete object propeties or object itself
# del s1.name
# del s1

# """
# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("ashu")
# print(s1)
# del s1
# print(s1)


# <__main__.Student object at 0x0000026F60F7BAD0>
# Traceback (most recent call last):
#   File "c:\Users\Ashutosh Raj Gupta\Desktop\Ashutosh\study_resources\PYTHON\python_tut\OOPS-PART2.py", line 13, in <module>
#     print(s1)
#           ^^
# NameError: name 's1' is not defined
# """

# Private(like) attributes and methods
# private attributes and methods are meant to be used only within the class and are not accessible from outside the class.
# __ we use double underscore to make attribute oe method private


"""
class Persons:
    __name = "anonyomous"

    def __hello(self):
        print("Hello Usre")

    def welcome(self):
        self.__hello()


p1 = Persons()
print(p1.welcome())
"""


# Inheritance - when one class (children/derived) derives the properties and methods of another class(parent/base).
# syntax-

# class Car:
#     ...
# class ToyotaCar(Car):
#     ...


# Simple code to understand


# types of inheritance
# 1. single inheritance       ----   one base and one derived class
"""
class Car:
    color = "black"

    @staticmethod
    def start():
        print("car started....")

    @staticmethod
    def stop():
        print("car stopped....")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.color)
print(car1.start())    # here we are calling the method from the base class while my object is of derived class
print(car1.name)
"""

# 2. Multi-level inheritance -  one parent class and two child class  par---child---child
# so basically the thord class will get the propertiees of both first two classes
"""
class Car:
    @staticmethod
    def start():
        print("car started....")

    @staticmethod
    def stop():
        print("car stopped....")


class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand


class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type


car1 = Fortuner("diesel")
car1.start()
"""

# 3. Multiple Inheritance - one derived class and more than one base class
# like base1 and base2 and then derived class

"""
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

"""

# Super method - it is used to access methods of the parent class.


"""
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started....")

    @staticmethod
    def stop():
        print("car stopped....")


class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)


car1 = ToyotaCar("prius", "electric")
print(car1.type)
"""

# class method - it is used to bound to the class and recieves the class as an implicit first argument.


"""
class Person:
    name = "abcd"

    def changeName(self, name):
        self.name = name

p1 = Person()
p1.changeName("rahulkumar")
print(p1.name)        # rahulkumar
print(Person.name)    # abcd
"""
# here i want to chage the name of the class of name var but as self is creating a name in object that is different from the class name var
# so to chnage it to class atribute we can use class name in object

"""
class Person:
    name = "abcd"

    # def changeName(self, name):
    #     Person.name = name
    #     # self.__class__.name = "Rahul"
    @classmethod
    def changeName(cls, name):
        cls.name = name


# so using classmethod we are directly interacting with class name var and changing it
p1 = Person()
p1.changeName("rahulkumar")
print(p1.name)        # rahulkumar
print(Person.name)    # rahulkumar

"""

# Property Decorator - we use @property decorator or any method in the class to use the method as a property
# scenario -  i ahve three subject marks i cal percenage but i found one subject marks is changed so i update
# it but it is not updated in original value passing so to update there also so that correct percentage is
# given we are using property decorator


"""
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy+self.chem+self.math)/3)+"%"

    def calcPercentage(self):
        self.percentage = str((self.phy+self.chem+self.math)/3)+"%"


s1 = Student(98, 89, 87)
print(s1.percentage)
s1.phy = 86
print(s1.phy)
print(s1.calcPercentage())
print(s1.percentage)
"""

# here what is done that if i am not creating a fun called calcPercentage then it is not updating the percentage
# so to do this i a better way is that we can use property decorator


class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"


s1 = Student(98, 89, 87)
print(s1.percentage)
s1.phy = 86
print(s1.percentage)

# so here the property act as a attribute and then update the value heer only
