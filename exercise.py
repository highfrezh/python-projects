# --------------Project 001-------------
# You are working at a car dealership and store the car data in a dictionary:
# car = {'brand': 'BMW','year': 2018,'color': 'red'}
# Your program needs to take the key as input and output the corresponding value.

# SOLUTION
# car = {
#     'brand':'BMW',
#     'year': 2018,
#     'color': 'red',
#     'mileage': 15000
# }
# key = input()
# print(car[key])

# ---------------Project 002------------------
# You are working on data that represents the economic freedom rank by country.
# Each country name and rank are stored in a dictionary, with the key being the country name.
#
# Complete the program to take the country name as input and output its corresponding economic freedom rank.
# In case the provided country name is not present in the data, output "Not found".

#SOLUTION
# data = {
#     'Singapore': 1,
#     'Ireland': 6,
#     'United Kingdom': 7,
#     'Germany': 27,
#     'Armenia': 34,
#     'United States': 17,
#     'Canada': 9,
#     'Italy': 74
# }
# countryName = input()
# print(data.get(countryName, "Not found"))

# -------------project 003--------------
# You are given a list of contacts, where each contact is represented by a tuple, with the name and age of the contact.
# Complete the program to get a string as input, search for the name in the list of contacts and output the age of the contact in the format presented below:
#
# Sample Input
# John

# Sample Output
# John is 31
# SOLUTION
# contacts = [
#     ('James', 42),
#     ('Amy', 24),
#     ('John', 31),
#     ('Amanda', 63),
#     ('Bob', 18)
# ]
# word = input()
# for i in contacts:
#     if word  in i:
#         print (str(i[0]) + " is " + str(i[1]) )
#         break
#     else :
#         print("Not Found")
#         break

# -------------- Project 004---------------
# Tuples can be used to output multiple values from a function.
# You need to make a function called calc(), that will take the side length of a square as its argument and return the perimeter and area using a tuple.
# The perimeter is the sum of all sides, while the area is the square of the side length.
#
# Sample Input
# 3
#
# Sample Output
# Perimeter: 12
# Area: 9

# SOLUTION

# def calc(x):
#     a = x**2
#     p = x+x+x+x
#     return  p, a
#
# side = int(input())
# p, a = calc(side)
#
# print("Perimeter: " + str(p))
# print("Area: " + str(a))

# -----------Project 005-------------------
# You are working on a recruitment platform, which should match the available jobs and the candidates based on their skills.
# The skills required for the job, and the candidate's skills are stored in sets.
# Complete the program to output the matched skill.
#SOLUTION
# skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
# job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}
# matched = list(skills & job_skills)
# print(matched[0])

# ---------------project 006--------------
# Given a word as input, output a list, containing only the letters of the word that are not vowels.
# The vowels are a, e, i, o, u.
#
# Sample Input
# awesome
#
# Sample Output
# ['w', 's', 'm']

# Solution
# word = input()
# vowels = ["a", "e","i","o","u"];
# nonVowel = [i for i in word if i not in vowels]
# print(nonVowel)

# ---------------------project 007------------------
# Given a string as input, you need to output how many times each letter appears in the string.
# You decide to store the data in a dictionary, with the letters as the keys, and the corresponding counts as the values.
# Create a program to take a string as input and output a dictionary, which represents the letter count.
#
# Sample Input
# hello
#
# Sample Output
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# text = input()
# dict = {}
# counter = 0
# for letter in text:
#     counter = text.count(letter)
#     dict[letter] = counter
# print(dict)

# ---------Project 008----------
# You are given code that should calculate the corresponding percentage of a price.
# Somebody wrote a lambda function to accomplish that, however the lambda is wrong.
# Fix the code to output the given percentage of the price.
#
# Sample Input
# 50
# 10
#
# Sample Output
# 5.0
#SOLUTION

# price = int(input())
# perc = int(input())
#
# res = (lambda x,y:(x*y)/100)(price, perc)
#
# print(res)

# -----------Project 009------------
# You work on a payroll program.
# Given a list of salaries, you need to take the bonus everybody is getting as input and increase all the salaries by that amount.
# Output the resulting list.
# You can use the map() function to increase all the values of the list.

#SOLUTION
# salaries = [2000, 1800, 3100, 4400, 1500]
# bonus = int(input())
# print(list(map(lambda x: x+ bonus, (salaries))))

#filter Example
# nums = [11, 22, 33, 44, 55]
# res = list(filter(lambda x: x%2==0, nums))
# print(res)

# -------- Project 010 -------------
# Finding prime numbers is a common coding interview task.
# The given code defines a function isPrime(x), which returns True if x is prime.
# You need to create a generator function primeGenerator(), that will take two numbers as arguments, and use the isPrime() function to output the prime numbers in the given range (between the two arguments).
#
# Sample Input
# 10
# 20
#
# Sample Output
# [11, 13, 17, 19]

# SOLUTION
# def isPrime(x):
#     if x < 2:
#         return False
#     elif x == 2:
#         return True
#     for n in range(2, x):
#         if x % n == 0:
#             return False
#     return True
#
#
# def primeGenerator(a, b):
#     # your code goes here
#     for i in range(a, b):
#         if isPrime(i):
#             yield i
#
#
# f = int(input())
# t = int(input())
#
# print(list(primeGenerator(f, t)))

# --------project 011-----------
# You are working on an invoicing system.
# The system has an already defined invoice() function, which takes the invoice number as argument and outputs it.
# You need to add a decorator for the invoice() function, that will print the invoice in the following format:
#
# Sample Input
# 42
#
# Sample Output
# ***
# INVOICE #42
# ***
# END OF PAGE

# SOLUTION
# def decor(func):
#     def wrap(num):
#         print("***")
#         func(num)
#         print("***")
#         print("END OF PAGE")
#     return wrap
#
# @decor
# def invoice(num):
#     print("INVOICE #" +num)
#
# invoice(input())

# Calculate factorial of any number
# SOLUTION
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x-1)
#
# num = int(input("Enter any number! "))
#
# print(factorial(num))

# -----------Project 012 ----------
# The given code defines a recursive function convert(), which needs to convert its argument from decimal to binary.
# However, the code has an error.
# Fix the code by adding the base case for the recursion, then take a number from user input and call the convert() function, to output the result.
#
# Sample Input
# 8
#
# Sample Output
# 1000

# SOLUTION
# def convert(num):
#    if num == 0:
#       return 0
#    return (num % 2 + 10 * convert(num // 2))
# num = int(input())
# res = convert(num)
# print(res)

# -------------Project 013-------------
# The given code defined a function called my_min(), which takes two arguments and returns the smaller one.
# You need to improve the function, so that it can take any number of variables, so that the function call works.

# SOLUTION
# def my_min(*y):
#     return min(y)
#
# print(my_min(8, 13, 4, 42, 120, 7))

# What is the result of this code?
# nums = {1, 2, 3, 4, 5, 6}
# nums = {0, 1, 2, 3} & nums
# nums = filter(lambda x: x > 1, nums)
# print(list(nums))
# print(len(list(nums)))

# -----------------Project 014---------------

# Given a string as input, use recursion to output each letter of the strings in reverse order, on a new line.
#
# Sample Input
# HELLO
#
# Sample Output
# O
# L
# L
# E
# H

# SOLUTION
# def spell(txt):
# # your code goes here
#     letters = txt[::-1]
#     for letter in letters:
#         print(letter)
# txt = input()
# spell(txt)

# ___________Product 015---------------
# You are making a video game! The given code declares a Player class, with its attributes and an intro() method.
# Complete the code to take the name and level from user input, create a Player object with the corresponding values and call the intro() method of that object.
#
# Sample Input
# Tony
# 12
#
# Sample Output
# Tony (Level 12)
# SOLUTION
# class Player:
#     def __init__(self, name, level):
#         self.name = name
#         self.level = level
#
#     def intro(self):
#         print(self.name + " (Level " +self.level + ")")
#
# #your code goes here
# name = input()
# level = input()
# info = Player(name, level)
# info.intro()

# -------------Project 015---------------
# Inheritance
#
#
# You are making a drawing application, which has a Shape base class.
# The given code defines a Rectangle class, creates a Rectangle object and calls its area() and perimeter() methods.
#
# Do the following to complete the program:
# 1. Inherit the Rectangle class from Shape.
# 2. Define the perimeter() method in the Rectangle class, printing the perimeter of the rectangle.
# SOLUTION
# class Shape:
#     def __init__(self, w, h):
#         self.width = w
#         self.height = h
#
#     def area(self):
#         print(self.width*self.height)
#
# class Rectangle(Shape):
#     #your code goes here
#     def perimeter(self):
#         print(2*(self.width+self.height))
# w = int(input())
# h = int(input())
#
# r = Rectangle(w, h)
# r.area()
# r.perimeter()

# -------------Project 016----------------
# Data Hiding
#
# We are working on a game. Our Player class has name and private _lives attributes.
# The hit() method should decrease the lives of the player by 1. In case the lives equal to 0, it should output "Game Over".
# Complete the hit() method to make the program work as expected.

# SOLUTION
# class Player:
#     def __init__(self, name, lives):
#         self.name = name
#         self._lives = lives
#
#     def hit(self):
#         # your code goes here
#         self._lives -= 1
#         if self._lives == 0:
#             print("Game Over")
#
#
# p = Player("Cyberpunk77", 3)
# p.hit()
# p.hit()
# p.hit()

# ----------Project 017-------------
# Static Methods
# The given code takes 2 numbers as input and calls the static area() method of the Shape class, to output the area of the shape, which is equal to the height multiplied by the width.
# To make the code work, you need to define the Shape class, and the static area() method, which should return the multiplication of its two arguments.

# SOLUTION
# class Shape:
#     @staticmethod
#     def area(width, height):
#         return width*height
#
# w = int(input())
# h = int(input())
#
# print(Shape.area(w, h))