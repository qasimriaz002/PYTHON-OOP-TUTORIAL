# =====================================================
# Lecture 07 - Inheritance Multilevel
# =====================================================

# In previous lectures we learned about:

# 1. Basic / Simple Inheritance
#    (One Parent → One Child)

# 2. Multiple Inheritance
#    (Multiple Parents → One Child)

# In this lecture we will learn another type of inheritance
# called MULTILEVEL INHERITANCE.


# -----------------------------------------------------
# What is Multilevel Inheritance?
# -----------------------------------------------------

# Multilevel inheritance means that a class inherits
# from another class, and then another class inherits
# from that child class.

# Structure:

# Grandparent Class
#        ↓
#    Parent Class
#        ↓
#     Child Class

# Each new class automatically gets properties
# of all previous classes.


# -----------------------------------------------------
# Real-world Example
# -----------------------------------------------------

# Consider the following hierarchy:

# Person → Student → GraduateStudent

# Person class contains general information.

# Student class inherits from Person
# and adds student related data.

# GraduateStudent class inherits from Student
# and adds further information.


# -----------------------------------------------------
# Grandparent Class
# -----------------------------------------------------

class Person:
    name = None
    age = None

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)


# -----------------------------------------------------
# Parent Class
# -----------------------------------------------------

# Student class inherits from Person

class Student(Person):
    department = None

    def show_student(self):
        print(self.name, "is studying in", self.department, "department")


# -----------------------------------------------------
# Child Class
# -----------------------------------------------------

# GraduateStudent inherits from Student

class GraduateStudent(Student):
    research_topic = None

    def show_research(self):
        print(self.name, "is doing research on", self.research_topic)


# -----------------------------------------------------
# Creating Object of Child Class
# -----------------------------------------------------

# Object of GraduateStudent is created

g1 = GraduateStudent()

# Assigning values

g1.name = "Ali"
g1.age = 24
g1.department = "Mechanical Engineering"
g1.research_topic = "Renewable Energy Systems"

# -----------------------------------------------------
# Conceptual RAM Packet
# -----------------------------------------------------

# ---------------------------------------------
# | name = "Ali"             (Person class)    |
# | age = 24                 (Person class)    |
# | department = Mechanical  (Student class)   |
# | research_topic = Energy  (GraduateStudent) |
# | introduce()              (Person class)    |
# | show_student()           (Student class)   |
# | show_research()          (GraduateStudent) |
# ---------------------------------------------
#                    ↑
#                   g1


# -----------------------------------------------------
# Calling Functions
# -----------------------------------------------------

# Function from Person class

g1.introduce()

print("----------------------")

# Function from Student class

g1.show_student()

print("----------------------")

# Function from GraduateStudent class

g1.show_research()


# -----------------------------------------------------
# Another Simple Example
# -----------------------------------------------------

# Machine hierarchy example


# Base Class

class Machine:
    machine_name = None

    def machine_info(self):
        print("Machine Name:", self.machine_name)


# Second Level Class

class Vehicle(Machine):
    fuel_type = None

    def vehicle_info(self):
        print("Fuel Type:", self.fuel_type)


# Third Level Class

class Car(Vehicle):
    brand = None

    def car_info(self):
        print("Car Brand:", self.brand)


# -----------------------------------------------------
# Creating Object
# -----------------------------------------------------

c1 = Car()

c1.machine_name = "Transport Machine"
c1.fuel_type = "Petrol"
c1.brand = "Toyota"

# Calling functions from all levels

c1.machine_info()

c1.vehicle_info()

c1.car_info()

# -----------------------------------------------------
# Concept Summary
# -----------------------------------------------------

# Multilevel Inheritance means:

# A class inherits from another class,
# and then another class inherits from it.

# Structure

# Class A
#   ↓
# Class B
#   ↓
# Class C


# Class C automatically gets properties
# of both Class A and Class B.


# Advantages

# 1. Code reuse across multiple levels
# 2. Logical hierarchy of classes
# 3. Easier program organization


# In upcoming lectures we will learn:

# 1. Diamond Problem in Multiple Inheritance
# 2. Method Resolution Order (MRO)
# 3. Function Overriding
# 4. Polymorphism
