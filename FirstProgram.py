print("my name is aashu")
print("I am an inoccent boy,", " but I have the power of the dragon.")
print(23)
print(23+45)
print(23/2)
print(55-23)


# variables in python
name = "ashutosh"
age = 23

print(name)
print(age)

print("my name is:", name)
print("my age is:", age)

age2 = age
print(age2)


# data types and type() function
num1 = 23
old = False
a = None
print(type(a))
print(type(name))
print(type(age))
print(type(old))


# sum print
a = 2
b = 5
sum = a+b
print("The sum is : ", sum)

# comments in python

#  it is a single lien comment
""" 
multi line
comment
"""

# arithmetic operators
a = 5
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)      # it will always give floating value in python
print(a % b)   # it finds the remainder of a and b
print(a**b)     # power operator


# relational operators
a = 50
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a <= b)

# logical operators
print(not True)
print(not False)

val1 = True
val2 = False
print("and operator is:", val1 and val2)
print("OR operator is:", val1 or val2)
print("OR operator is:", (a == b) or (a > b))

# type conversion

# 1. conversion
a = 2
b = 4.25
sum = a+b       # here a will get changed into float as float is superior than int so it is done automatically
print(type(sum))

# typecasting
x = 1
y = '3'

# c = int('3')
c = int(y)
sum1 = x+c
print(sum1)


# user input in python
name = input("Enter your name : ")
age = int(input("Enter your age : "))
print("My name is :", name)
print("my age is:", type(age), age)
