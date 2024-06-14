# set id the collection of the unordered items
# each element in the set must be unique and immutable .

# nums={1,2,3,4}
# set2={1,2,2,2}   # repeated elements are stored only once , so it resolved to be {1,2}


# null_set=set()  #empty set

# list and dictionary cant be stored in the set as they are mutable and sets are immuatable so bollean, int float, str, tuple can be stored as they are immutabel

# sets will ignore the duplicate the value
collection = {1, 2, 3, 4, 2, 2, "hello"}
print(collection)
print(type(collection))
print(len(collection))

"""
sets are mutable as we can add and remove elements  but the elements of the sets are immutable.
"""


# methods in set
# adds element in the set we can store string also tuple but list cant be add
collection.add(5)
print(collection)

collection.remove(5)   # remove the element
print(collection)

# collection.pop()      # remove random value
# print(collection)

# collection.clear()
# print(collection)

# union method comines both set values and return new set and intersection find the common value in both sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))
print(set1.intersection(set2))
