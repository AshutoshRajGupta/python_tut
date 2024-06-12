# string is a data type that stores a sequence of  a characters.
# str2 = 'ashutosh'
# str3 = """this is a string"""

# escape sequence characters for next line tabs etc
str1 = "this usa string. \n we are craeting it in python."
print(str1)

# operations:
# 1. concatenation       "hello"+"world"---->"helloworld"
# 2. length of str        len(str)

a = "apna"
print(len(a))

b = "aashu"
print(a+" "+b)
c = a+" "+b
print(len(c))


# Indexing
# always start from 0 and helps in accessing the character
"""
str = "ashutosh"
ch = str[0]
print(ch)
print(str[3])
we cant change the character value with help of indexing.
"""

# slicing
"""
helps in acessing the part of a string
str="ApnaCollege"
str[1:4] is "pna"
str[:4] is same as str[0:4]
str[1:] is same a s str[1:lens(str)]

python also introduce negative slicing which starts from the backward side and always start with -1
ex- a  p  p  l  e
   -5 -4 -3 -2 -1

str="Apple"
str[-3:-1] is "pl"

"""


# string functions
str = "i am a coder am"
print(str.endswith('er.'))
print(str.capitalize())
print(str.replace('a', 'o'))
print(str.find('am'))
print(str.count("am"))

# string aee very powerful in python as its has so many inbuilyt functions
