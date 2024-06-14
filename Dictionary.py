"""
dictionaries are used to store data values in key:value pairs.
they are unordered, mutable(changable) and dont allow duplicate keys

"key":value

dict={
    "name":"ashu",
    "cgpa":9.6,
    "marks":[98.87,95],
}

dict["name"],dict["cgpa"],dict["marks"]
"""


info = {
    "name": "ashu",
    "learning": "coding",
    "age": 35,
    "marks": 94.4,
    "subjects": ["python", "java", "cpp"],
    "topics": ("dictionary", "sets"),
    "is_adult": True
}
print(info)
print(type(info))

# there is no any indexing in dictionary in python

# if i want to access values i will use key for that
print(info["age"])
print(info["marks"])
print(info["subjects"])

info["name"] = "ashuuu"
print(info["name"])
# in the same manner we can add a new key value pair
info["surname"] = "gupta"
print(info)


# creating an empty dictionary
null_dict = {}


# Nested Dictionary
info1 = {
    "name": "ashu",
    "subjects": {
        "phy": 97,
        "chem": 88,
        "maths": 99
    }
}

print(info1)
print(info1["subjects"]["chem"])


# methods in dictionary
# here we use keys function to print out total keys then converted into list from dicyionary and then count total no of keys
print(len(list(info1.keys())))

print(info1.values())      # return all the values

print(info1.items())       # return all (key,val) pairs as tuples

print(info1.get("name"))   # return the value according to specify key

info1.update({"city": "pune"})
print(info1)


# if we want to store more than one value for a key we can use list and tuple
dictionary = {
    "cat": "s amall animal",
    "table": ["abc", "xyz"]
}
