# =====================================================
# Lecture 10 - Polymorphism Overloading
# =====================================================

# In previous lectures we learned:
# 1. Classes and Objects
# 2. Encapsulation
# 3. Different types of Inheritance
# 4. super() keyword in inheritance

# In this lecture we will learn a new concept of OOP
# called POLYMORPHISM.


# -----------------------------------------------------
# What is Polymorphism?
# -----------------------------------------------------

# The word Polymorphism means:

# "Poly"  → Many
# "Morphism" → Forms

# So Polymorphism means:
# One function name can behave in multiple ways.


# -----------------------------------------------------
# Types of Polymorphism
# -----------------------------------------------------

# 1. Function Overloading  (Compile-time concept)
# 2. Function Overriding   (Run-time concept)

# In this lecture we will focus on FUNCTION OVERLOADING.


# -----------------------------------------------------
# What is Function Overloading?
# -----------------------------------------------------

# Function overloading means creating functions
# with the SAME NAME but DIFFERENT PARAMETERS.

# Python does not support traditional function overloading
# like some other languages.

# However, we can simulate overloading using
# default arguments.


# =====================================================
# Example 1
# Function Overloading in a Single Class
# =====================================================


class Calculator:

    # This function can behave differently depending on arguments

    def add(self, a=None, b=None, c=None):

        # Case 1 → two numbers

        if a is not None and b is not None and c is None:

            result = a + b
            print("Addition of two numbers:", result)

        # Case 2 → three numbers

        elif a is not None and b is not None and c is not None:

            result = a + b + c
            print("Addition of three numbers:", result)

        else:

            print("Invalid input")


# Creating object

calc1 = Calculator()

# Calling function with different number of arguments

calc1.add(10, 20)

calc1.add(10, 20, 30)



# -----------------------------------------------------
# Conceptual Idea
# -----------------------------------------------------

# Same function name → add()

# But it works for:
# add(a,b)
# add(a,b,c)

# This demonstrates FUNCTION OVERLOADING behavior.


# =====================================================
# Example 2
# Function Overloading using Inheritance
# =====================================================


# Parent Class

class Shape:

    def area(self, a=None, b=None):

        if a is not None and b is None:

            # area of square

            print("Area of square:", a * a)

        elif a is not None and b is not None:

            # area of rectangle

            print("Area of rectangle:", a * b)

        else:

            print("Invalid input")



# Child Class

class AdvancedShape(Shape):

    def area(self, a=None, b=None, c=None):

        # Calling parent class version if two values are given

        if c is None:

            super().area(a, b)

        else:

            # area of triangle

            print("Area of triangle:", 0.5 * a * c)



# Creating object

shape1 = AdvancedShape()

# Square

shape1.area(5)

# Rectangle

shape1.area(5, 10)

# Triangle

shape1.area(5, 10, 8)



# -----------------------------------------------------
# Concept Summary
# -----------------------------------------------------

# Function Overloading allows a function
# to perform different tasks depending on
# the number or type of arguments.


# Example:

# add(a,b)
# add(a,b,c)


# Advantages:

# 1. Improves code readability
# 2. Reduces need for multiple function names
# 3. Provides flexibility in function usage


# In upcoming lectures we will learn:

# Function Overriding
# Another important type of polymorphism.