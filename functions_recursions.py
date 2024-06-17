# functions are block of statements that perform a specific task, helps in code reusability.
# syntax:
# def func_name(param1, param2):     # function definition
#     #some work
#     return val
# func_name(arg1,arg2)   # function call


""" # sum of two numbers functions
"""
# def sum(a, b):      # a and b are parameters
#     return a+b

# print(sum(2, 3))    # 2 and 3 are arguments


"""# average of three numbers
"""
# def calc_avg(a, b, c):
#     sum = a+b+c
#     avg = sum/3
#     return avg

# print(calc_avg(23, 45, 67))


""" 
Default parameters:  assigning a default value to parameter, which is used when no argument is passed.
"""
# mult

# def prod(a=1, b=1):
#     print(a*b)
#     return a*b
# prod()


""" wap to print length of a list (list is the parameter)"""

# cities = ["delhi", "noida", "chennai", "pune", "mumbai"]
# def print_list(list):
#     print(len(list))
# print_list(cities)


""" wap to print the elements of a list in single line (list is parameter)"""
# cities = ["delhi", "noida", "chennai", "pune", "mumbai"]
# def print_list(list):
#     for item in list:
#         print(item, end=" ")
# print_list(cities)
# print()


""" factorial using function"""

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# factorial(5)

# -----------------------------------------------------------------------------------------------
"""  Recursions : when a function calls itself repeatedly
"""
# 5,4,3,2,1

# def show(n):
#     if (n == 0):            # base case
#         return
#     print(n)
#     show(n-1)
# show(5)


""" factroial uing recursion"""

# def fact(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))


""" recursive function to calculate sum of first n numbers"""

# def sum_nat(n):
#     if (n == 0):
#         return 0
#     return sum_nat(n-1)+n
# sum = sum_nat(5)
# print(sum)
