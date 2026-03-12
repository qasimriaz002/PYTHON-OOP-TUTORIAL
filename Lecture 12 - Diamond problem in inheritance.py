# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 12 - Diamond Problem in Inheritance
# =====================================================

# In previous lectures we learned:
# 1. Single, Multiple, Multilevel Inheritance
# 2. super() keyword
# 3. Function Overloading
# 4. Function Overriding (Runtime Polymorphism)

# In this lecture we will learn about the DIAMOND PROBLEM
# in inheritance and how Python solves it using MRO.

# -----------------------------------------------------
# What is the Diamond Problem?
# -----------------------------------------------------

# Diamond problem occurs in MULTIPLE INHERITANCE when:

# - A class inherits from TWO parent classes
# - Both parent classes inherit from the SAME grandparent class
# - The child class calls a method present in the grandparent

# This creates ambiguity:
# Which path should Python follow to call the method?

# Structure:

#          Grandparent
#           /       \
#     Parent1       Parent2
#           \       /
#             Child

# Without rules, the program cannot decide which parent's
# version of the grandparent method to call.

# Python solves this using **Method Resolution Order (MRO)**


# =====================================================
# Example: Diamond Problem
# =====================================================

# Grandparent Class

class Person:

    def introduce(self):
        print("I am a person")



# Parent Classes

class Student(Person):

    def introduce(self):
        print("I am a student")



class Teacher(Person):

    def introduce(self):
        print("I am a teacher")



# Child Class inherits from BOTH Student and Teacher

class TeachingAssistant(Student, Teacher):
    pass



# Creating object

ta1 = TeachingAssistant()

# Calling introduce() method

ta1.introduce()

# -----------------------------------------------------
# Explanation
# -----------------------------------------------------

# Output: I am a student

# Why? → Python follows **Method Resolution Order (MRO)**

# MRO is the order Python searches classes for a method:

# Child → Left Parent → Right Parent → Grandparent

# Here:
# TeachingAssistant → Student → Teacher → Person

# So Student's introduce() is called first


# -----------------------------------------------------
# Checking Method Resolution Order
# -----------------------------------------------------

print("MRO of TeachingAssistant class:")

for cls in TeachingAssistant.__mro__:
    print(cls.__name__)

# Output:
# TeachingAssistant
# Student
# Teacher
# Person
# object


# -----------------------------------------------------
# How to Call Grandparent Method Explicitly
# -----------------------------------------------------

# Using super() along with MRO

class TeachingAssistant2(Student, Teacher):

    def introduce(self):
        print("Teaching Assistant introduces:")

        # Call first parent (Student) using super()
        super().introduce()


ta2 = TeachingAssistant2()
ta2.introduce()

# Output:
# Teaching Assistant introduces:
# I am a student

# Using super() ensures Python follows MRO properly


# -----------------------------------------------------
# Key Points
# -----------------------------------------------------

# 1. Diamond problem occurs when multiple inheritance
#    leads to ambiguous paths to a grandparent method

# 2. Python solves it using **Method Resolution Order (MRO)**

# 3. Use `ClassName.__mro__` to check the search order

# 4. Use **super()** to safely call methods
#    following the MRO without ambiguity


# -----------------------------------------------------
# Concept Summary Table
# -----------------------------------------------------

# Scenario                    | Result
# -------------------------------------------------
# Child calls method           | Leftmost parent in MRO is executed
# MRO of class                 | Checked via ClassName.__mro__
# Explicit call using super()  | Calls next class in MRO

# -----------------------------------------------------
# In upcoming lectures we will:
# - Practice combined OOP exercises
# - Use objects in lists/dictionaries
# - Pass objects as arguments
# - Apply multiple OOP concepts in Mechanical Engineering examples