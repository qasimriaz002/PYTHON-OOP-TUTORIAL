# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 19 - Operator Overloading
# =====================================================

# In previous lectures we learned:
# 1. Polymorphism
# 2. Function Overloading
# 3. Function Overriding
# 4. Abstraction
# 5. Abstract Classes and Methods

# In this lecture we will learn another important
# concept of Object-Oriented Programming called:

# OPERATOR OVERLOADING


# -----------------------------------------------------
# What is Operator Overloading?
# -----------------------------------------------------

# Operator Overloading means:

# Giving special meaning to operators
# when they are used with OBJECTS.

# Example operators:

# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division
# ==  Equality
# >   Greater than

# Normally these operators work with numbers.

# Example:

# print(10 + 20)

# But using Operator Overloading,
# we can make operators work with OBJECTS also.


# -----------------------------------------------------
# Magic Methods / Special Methods
# -----------------------------------------------------

# Python provides special functions called:

# MAGIC METHODS
# or
# DUNDER METHODS

# Dunder means:
# Double Underscore

# Example:

# __add__()
# __sub__()
# __str__()

# These methods allow operators to work with objects.

# # + operator for integers
print(1 + 2)
#
# # + operator for strings (concatenation)
print("Geeks" + "For")
#
# # * operator for numbers
print(3 * 4)
#
# # * operator for strings (repetition)
print("Geeks" * 4)


# When we use an operator on user-defined objects, Python doesn’t know how to handle it. To make operators work with custom classes, Python provides special methods (also called magic methods).
#
# + operator -> calls __add__(self, other)
# - operator -> calls __sub__(self, other)
# == operator -> calls __eq__(self, other)
#
# So, when we write obj1 + obj2, internally Python calls:
#
# obj1.__add__(obj2)
#
# If this method is defined in the class, operator overloading works.


# =====================================================
# Example 1
# Without Operator Overloading
# =====================================================


class Student:

    def __init__(self, marks):
        self.marks = marks


# Creating objects

s1 = Student(80)

s2 = Student(70)


# This will NOT add marks directly

# print(s1 + s2)

# Python does not know how to add
# two Student objects.

# So we use OPERATOR OVERLOADING.


# =====================================================
# Example 2
# Overloading + Operator using __add__()
# =====================================================


class Student:

    def __init__(self, marks):
        self.marks = marks

    # Overloading + operator

    def __add__(self, other):
        total = self.marks + other.marks

        return total


# Creating objects

s1 = Student(85)

s2 = Student(90)

# Now + operator works with objects

result = s1 + s2

print("Total Marks:", result)


# -----------------------------------------------------
# Conceptual Idea
# -----------------------------------------------------

# When Python sees:

# s1 + s2

# Internally Python calls:

# s1.__add__(s2)

# So __add__() controls the behavior
# of + operator for objects.


# =====================================================
# Example 3
# Overloading Comparison Operator
# =====================================================


class Employee:

    def __init__(self, salary):

        self.salary = salary

    # Overloading > operator

    def __gt__(self, other):

        if self.salary > other.salary:

            return True

        else:

            return False


# Creating objects

e1 = Employee(50000)

e2 = Employee(45000)

# Comparing objects

if e1 > e2:

    print("Employee 1 has greater salary")

else:

    print("Employee 2 has greater salary")


# -----------------------------------------------------
# Conceptual Idea
# -----------------------------------------------------

# When Python sees:

# e1 > e2

# Internally Python calls:

# e1.__gt__(e2)

# __gt__() means:
# Greater Than


# =====================================================
# Example 4
# Overloading == Operator
# =====================================================


class Product:

    def __init__(self, price):

        self.price = price

    # Overloading == operator

    def __eq__(self, other):

        if self.price == other.price:

            return True

        else:

            return False


# Creating objects

p1 = Product(1500)

p2 = Product(1500)

# Comparing products

if p1 == p2:

    print("Both products have same price")

else:

    print("Products have different prices")


# -----------------------------------------------------
# Important Operator Overloading Methods
# -----------------------------------------------------

# +   → __add__()

# -   → __sub__()

# *   → __mul__()

# /   → __truediv__()

# ==  → __eq__()

# >   → __gt__()

# <   → __lt__()

# >=  → __ge__()

# <=  → __le__()


# =====================================================
# Example 5
# Overloading String Representation using __str__()
# =====================================================


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Overloading print behavior

    def __str__(self):
        return f"Car Brand: {self.brand}, Model: {self.model}"


# Creating object

c1 = Car("Toyota", "Corolla")

# Printing object

print(c1)

# -----------------------------------------------------
# Conceptual Idea
# -----------------------------------------------------

# When Python sees:

# print(c1)

# Internally Python calls:

# c1.__str__()

# __str__() controls how object data
# is displayed as a string.


# =====================================================
# Real Life Analogy
# =====================================================

# Imagine a Calculator:

# 10 + 20 = 30

# Here + works with numbers.

# Now imagine Student objects:

# Student1 + Student2

# We can define what + means.

# Maybe:
# Add marks
# Add GPA
# Add credits

# This flexibility is called
# Operator Overloading.


# =====================================================
# Concept Summary
# =====================================================

# Operator Overloading allows operators
# to work with OBJECTS.

# Python uses special methods called
# MAGIC METHODS or DUNDER METHODS.

# Examples:

# __add__()
# __sub__()
# __gt__()
# __eq__()
# __str__()

# Advantages:

# 1. Makes code more readable
# 2. Improves flexibility
# 3. Allows operators to work with objects
# 4. Makes classes more powerful


# In upcoming lectures we will learn:

# Method Resolution Order (MRO)
# and
# Advanced Python OOP concepts.
