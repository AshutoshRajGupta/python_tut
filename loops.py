# loops are used to repeat instructions
# while loops
# for loops
"""
while condition:
    #some statement
"""

""" to print hello world multiple times"""
# count = 1
# while (count <= 5):
#     print("Hello",i)
#     count += 1

""" to print numbers from 1 to 100"""
# i = 1
# while i < 100:
#     print(i)
#     i += 1

""" mutiplication table"""
# n=int(input("enter numbers: "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1


""" prunt the eleemnst from list using a loop"""
# lis = [1, 4, 9, 16, 25]
# idx = 0
# while idx < len(lis):
#     print(lis[idx])
#     idx += 1

""" searc a number xin the tuple using loop"""
# tup = (1, 2, 3, 4, 5, 6)
# x = 5
# idx = 0
# while idx < len(tup):
#     if (tup[idx] == x):
#         print("FOUND at index", idx)
#     idx += 1


# Break: used to terminate the loop when encountered
# continue: terminates execution in the urrent iteration and cintinues exceution of the loop with the next iteration

# i = 1
# while i <= 5:
#     print(i)
#     if (i == 3):
#         break
#     i += 1
# print("end of loop")

# i = 0
# while i <= 5:
#     if (i == 3):
#         i += 1    # for skipping that particular element
#         continue
#     print(i)
#     i += 1


""" for loops are used for sequential traversal. for traversing list,string, tuples etc. """
lis = [1, 2, 3]
for el in lis:
    print(el)

beggies = ["potato", "brinjal"]
for val in beggies:
    print(val)

""" number found using for loop"""
# this is we called linear search
# tup = (1, 2, 3, 4,)
# x = 3
# idx = 0
# for el in tup:
#     if (el == x):
#         print("number found", idx)
#     idx += 1


""" range function"""
# range function returns a sewunce of numbers. starting from 0 by default, and increments by 1(by default) and stops before a specific number
# syntax range(start?,stop,step?)

# for el in range(5):
#     print(el)

# for el in range(1, 5):   # 1,2,3,4
#     print(el)

# for el in range(1, 5, 2):  # 1,3
#     print(el)


""" pass statement: is a null statement that does nothing. It is used as a placeholder for future code."""
# for el in range(5):
#     pass
# print("some useful work")


""" sum of first n numbers"""
# sum = 0
# n = int(input("enter numbers: "))
# for i in range(1, n+1):
#     sum = sum+i
# print("total sum is:", sum)

""" factorial"""
# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print("factorial of number is ", fact)
