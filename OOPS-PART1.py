# class is a blueprint for creating objects
# creating class

"""
class Student:
    name="karan kumar"
# creating object (instance)
s1=Student()
print(s1.name)
"""

# here i have a created a class name called Student where i am passing
# every student same name as karan and i am printing the name for every instnces
# class Student:
#     name = "karan"

# s1 = Student()
# print(s1.name)   # karan will print
# s2 = Student()
# print(s2.name)   # karan will print


"""class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)"""


# Constructor in python (__init__ function)
# constructor is invoke automatically when an object is created
# All classes have a function called __init__() which is always executed when the object is being initiated.

# the self parameter is a refrenec to the current instance of the class, and is sued to acess variables that belongs to the class.
# its basically same a s this function in cpp
# we can give the any name to the self
"""
class Student:

    # default constructors
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("kafran", 99)
print(s1.name, " ", s1.marks)
s2 = Student("arjun", 78)
print(s2.name, " ", s2.marks)
"""

# Class and Instance Attribute
# college and student example diferent student name but same college name class Student:
# object attributes has higher precedence than class attributes

"""
class Student:
    college_name = "ABC COLLEGE"   # because it is not defined with self to memory me ek hi baar create hoga 
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("kafran", 99)
print(s1.name, " ", s1.marks, " ", s1.college_name)
s2 = Student("arjun", 78)
print(s2.name, " ", s2.marks)
"""

# Methods -this are functions belong to objects

# class Student:
#     def __init__(self, fullname):
#         self.name = fullname
#     def hello(self):
#         print("hello", self.name)
# s1 = Student("karan")
# s1.hello()


"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("hello Student ", self.name)

    def get_marks(self):
        return self.marks


s1 = Student("karan", 98)
s1.welcome()
print(s1.get_marks())
"""

# Static methods
# methods that don't use the self parameter (work at class level)
"""
class Student:
    @staticmethod   # decorator
    def college():
        print("ABC College")
"""


# Abstraction - hiding the implementation details of a class and only showing the essential features to the user.

"""
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clt = False

    def start(self):
        self.clt = True
        self.acc = True
        print("car started...")

car1 = Car()
car1.start()
"""

# Encapsulation - wrapping the data and functions into a single unit(object)
