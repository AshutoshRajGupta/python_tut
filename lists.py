# lists
# a built in data type that stores set of values, it can store elements of different types(integer,float,string etc)
# created using square brackets [],
# string are immutable in python but lists are mutable means we can change the data value

# marks=[87,64,33,96,89]   #marks[0],marks[1].....

marks = [97, 89, 76, 45, 78]
print(marks)
print(type(marks))
print(marks[2])
print(len(marks))

# in cpp or java we are storing the data in array of same time but it is not somehting with list
# in list we can add data of different types

student = ["karan", 85, "Delhi"]
student[1] = 45
print(student)   # output- ["karan",45,"Delhi"]

# slicing
# slicing works in the same way starts with zero indexing in forward slicing and in backward slicing starts with -1
# marks=[76,98,78,445,34]
# print(marks[1:4])  ----> [98,78,445]

# functions /methods used in lists
"""
list = [2, 1, 3]
list.append(4)      # add element at last at the end
print(list)

list.sort()         # sort in ascending order
print(list)

list.sort(reverse=True)    # sorts in descending order
print(list)

list.reverse()       # reverses list
print(list)

list.insert(2, 8)    # insert element at index
print(list)

list.remove(1)   # removes first occurence of element
print(list)

list.pop(idx)   # removes element at index
print(list)
"""


# wap to ask the user to enter names of their 3favourite movie and append them into list
"""
movies = []
mov1 = input("enter 1st movie: ")
mov2 = input("enter 2nd movie: ")
mov3 = input("enter 3rd movie: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
"""

# another way is directly append into movies list
"""
movies.append(input("enter the first movie: "))
movies.append(input("enter the secons movie: "))
movies.append(input("enter the third movie: "))
"""


# wap to check if a list contains a plaindrome of elements
# logic: we make a copy of listy and rverse it if revrse list and original list matches element with same
"""
list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("PALINDROME")
else:
    print("NOT PALINDROME")
"""
