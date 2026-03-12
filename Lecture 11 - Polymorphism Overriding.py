# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 11 - Polymorphism Overriding (Runtime Polymorphism)
# =====================================================

# In previous lectures we learned:
# 1. Function Overloading
# 2. Inheritance (Single, Multiple, Multilevel)
# 3. super() keyword

# In this lecture we will learn FUNCTION OVERRIDING,
# another type of POLYMORPHISM.

# -----------------------------------------------------
# What is Function Overriding?
# -----------------------------------------------------

# Function overriding means:

# A child class defines a function with the SAME NAME
# as a function in its parent class.

# When we call the function using a child object,
# the CHILD'S version is executed instead of the parent’s.

# This is called RUN-TIME POLYMORPHISM.

# -----------------------------------------------------
# Example 1: Single Inheritance
# -----------------------------------------------------

# Parent Class

class Person:

    def introduce(self):

        print("I am a person")



# Child Class

class Student(Person):

    # Overriding the introduce() method

    def introduce(self):

        print("I am a student")



# Creating objects

p1 = Person()
s1 = Student()

# Calling parent class function

p1.introduce()   # Output → I am a person

# Calling child class function (overrides parent function)

s1.introduce()   # Output → I am a student



# -----------------------------------------------------
# Explanation
# -----------------------------------------------------

# Even though Student inherits from Person,
# its introduce() method replaces the parent’s method
# when called using a Student object.


# =====================================================
# Example 2: Multilevel Inheritance
# -----------------------------------------------------

# Grandparent Class

class Vehicle:

    def fuel_type(self):

        print("Generic fuel type")



# Parent Class

class Car(Vehicle):

    # Overriding fuel_type()

    def fuel_type(self):

        print("Petrol fuel type for Car")



# Child Class

class ElectricCar(Car):

    # Overriding fuel_type() again

    def fuel_type(self):

        print("Electric fuel type for Electric Car")



# Creating objects

v1 = Vehicle()
c1 = Car()
e1 = ElectricCar()

# Calling methods

v1.fuel_type()   # Generic fuel type
c1.fuel_type()   # Petrol fuel type for Car
e1.fuel_type()   # Electric fuel type for Electric Car



# -----------------------------------------------------
# Conceptual RAM Packet
# -----------------------------------------------------

# Each object stores its own copy of methods:

# v1 → Vehicle.fuel_type()
# c1 → Car.fuel_type() (overrides Vehicle)
# e1 → ElectricCar.fuel_type() (overrides Car)


# -----------------------------------------------------
# Example 3: Using super() with Overriding
# -----------------------------------------------------

class Teacher(Person):

    def introduce(self):

        print("I am a teacher")

        # Call parent version using super()

        super().introduce()


t1 = Teacher()

t1.introduce()

# Output:
# I am a teacher
# I am a person


# -----------------------------------------------------
# Concept Summary
# -----------------------------------------------------

# Function Overriding:

# 1. Child class defines a function with the same name as parent
# 2. When called using child object → child’s version executes
# 3. This is RUN-TIME POLYMORPHISM
# 4. super() can be used inside child method to also call parent method

# Advantages:

# 1. Allows specialized behavior in child class
# 2. Makes code flexible and reusable
# 3. Keeps a logical class hierarchy intact


# In upcoming lectures we will learn:

# Combined Exercises of OOP:
# - Using lists / tuples / dictionaries of objects
# - Passing objects as parameters
# - Using loops and conditions inside class functions
# - Applying multiple OOP concepts in scenario-based questions