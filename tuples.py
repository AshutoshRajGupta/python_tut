# a built in dtata type that let us create immutable sequences of values
# created using paranthesis ()
# tup=(87,64,89,98,56)   #tup[o],tup[1]....

tup = (2, 1, 3, 1)
print(type(tup))
print(tup[0])
# tup[0] = 5    # tuple' object does not support item assignment
# creating an empty tuple
tup1 = ()
print(type(tup1))
print(tup1)    # --->()

# to createa single value tuple put comma , after value
tup2 = (1,)
print(tup2)

# slicing works in the same way as they work in the list

#methods/functions in tuples
tupp = (2, 1, 3, 1)
print(tupp.index(1))        # returns index of first occurence

print(tupp.count(1))        # return total count or occurences


# wap to count the number of students with the "A" ggrade in following tuple
"""
grade = ("a", "a", "c", "b", "a", "f")
print(grade.count("a"))
"""
# store the above values in a list and sort them form "A to D"
"""
grade = ["a", "a", "c", "b", "a", "f"]
grade.sort()
print(grade)
"""
