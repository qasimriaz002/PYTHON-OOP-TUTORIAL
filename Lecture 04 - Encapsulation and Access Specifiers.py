# ===============================================
# Lecture 04 - Encapsulation and Access Specifiers
# ===============================================

# In previous lectures we learned:
# 1. Classes and Objects
# 2. Constructors and Destructors
# 3. Getter and Setter Functions

# In this lecture we will learn an important concept of Object-Oriented Programming
# called ENCAPSULATION.


# -------------------------------------------------------
# What is Encapsulation?
# -------------------------------------------------------

# Encapsulation means combining DATA and FUNCTIONS together inside a class
# and restricting direct access to some of the object's internal data.

# In simple words:

# Encapsulation =
# Putting variables and functions together in a single unit (class)
# and protecting sensitive data from direct access.

# Real-world example:

# Think of a MACHINE.

# A machine has:
#   Internal parts (hidden from user)
#   Control buttons (user interacts through them)

# User does not directly touch internal gears of machine.
# Instead user presses buttons to operate it.

# In programming:

# Variables = Internal machine parts
# Functions = Control buttons


# -------------------------------------------------------
# Access Specifiers
# -------------------------------------------------------

# Access specifiers define how variables of a class can be accessed.

# Python uses naming conventions to represent access levels.

# 1. Public variable
#    Accessible from anywhere

# 2. Protected variable
#    Should only be accessed inside class and child classes

# 3. Private variable
#    Cannot be accessed directly outside the class


# -------------------------------------------------------
# Creating Student Class
# -------------------------------------------------------

class Student:

    # Constructor to initialize data when object is created
    def __init__(self, name, age, marks):

        # PUBLIC VARIABLE
        # Can be accessed anywhere

        self.s_name = name


        # PROTECTED VARIABLE
        # Single underscore "_" indicates protected variable
        # It should only be used inside class or subclasses

        self._s_age = age


        # PRIVATE VARIABLE
        # Double underscore "__" indicates private variable
        # It should not be accessed directly outside class

        self.__s_marks = marks



    # -------------------------------------------------------
    # Function to display student information
    # -------------------------------------------------------

    def display_student(self):

        print("Student Name:", self.s_name)
        print("Student Age:", self._s_age)
        print("Student Marks:", self.__s_marks)



    # -------------------------------------------------------
    # Getter Function
    # -------------------------------------------------------

    # Used to safely read private variable

    def get_marks(self):
        return self.__s_marks



    # -------------------------------------------------------
    # Setter Function
    # -------------------------------------------------------

    # Used to safely modify private variable

    def set_marks(self, new_marks):

        if new_marks >= 0 and new_marks <= 100:

            self.__s_marks = new_marks
            print("Marks updated successfully")

        else:

            print("Invalid marks entered")



# -------------------------------------------------------
# Creating Object of Student Class
# -------------------------------------------------------

# When object is created, memory is allocated in RAM

s1 = Student("Ali", 20, 75)

# Conceptual RAM view:

# -----------------------------------------
# | s_name = "Ali"  (public variable)      |
# | _s_age = 20     (protected variable)   |
# | __s_marks = 75  (private variable)     |
# | functions of class Student             |
# -----------------------------------------
#                   ↑
#                  s1


# -------------------------------------------------------
# Accessing Public Variable
# -------------------------------------------------------

# Public variables can be accessed directly

print("Student Name:", s1.s_name)



# -------------------------------------------------------
# Accessing Protected Variable
# -------------------------------------------------------

# Protected variables can technically be accessed,
# but it is not recommended outside the class.

print("Student Age:", s1._s_age)



# -------------------------------------------------------
# Accessing Private Variable
# -------------------------------------------------------

# The following line will cause an error if we try:

# print(s1.__s_marks)

# Because private variables cannot be accessed directly outside class


# -------------------------------------------------------
# Accessing Private Variable using Getter
# -------------------------------------------------------

print("Student Marks:", s1.get_marks())



# -------------------------------------------------------
# Modifying Private Variable using Setter
# -------------------------------------------------------

s1.set_marks(85)

print("Updated Marks:", s1.get_marks())



# -------------------------------------------------------
# Testing Invalid Input
# -------------------------------------------------------

s1.set_marks(150)



# -------------------------------------------------------
# Calling Class Function
# -------------------------------------------------------

s1.display_student()



# -------------------------------------------------------
# Concept Summary
# -------------------------------------------------------

# Encapsulation means:
# Combining variables and functions inside a class
# and protecting internal data.

# Types of access specifiers in Python:

# Public
#   variable_name

# Protected
#   _variable_name

# Private
#   __variable_name


# Why Encapsulation is important?

# 1. Protect sensitive data
# 2. Prevent invalid changes to variables
# 3. Improve program security
# 4. Control how data is accessed


# In upcoming lectures we will learn:

# Inheritance
# Where one class can use properties of another class
# which helps in code reuse and building large systems.