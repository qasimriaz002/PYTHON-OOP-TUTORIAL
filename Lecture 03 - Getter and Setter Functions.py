# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# ===============================
# Lecture 03 - Getter and Setter Functions
# ===============================

# In previous lectures we learned:
# 1. What are classes and objects
# 2. How objects store data in RAM
# 3. How functions inside class use the "self" keyword
# 4. How constructor automatically initializes data

# In this lecture we will learn:
# 1. Why we should not directly access important data of objects
# 2. What are Getter functions
# 3. What are Setter functions
# 4. How getter and setter help in protecting data (Encapsulation)


# In real-world programs some data must be protected.
# Example:
# A student's marks should not be randomly changed by anyone in program.

# BAD PRACTICE:
# s1.s_marks = -100
# s1.s_marks = 1000

# These values are logically wrong.
# To avoid such problems we make variables PRIVATE
# and use Getter and Setter functions to control access.


# ---------------------------------------------------
# Creating Student Class
# ---------------------------------------------------

class Student:

    # Constructor is used to initialize values when object is created
    def __init__(self, name, age, marks):

        # Public variables
        self.s_name = name
        self.s_age = age

        # Private variable
        # "__" double underscore means the variable should not be accessed directly
        self.__s_marks = marks

        # Now marks are protected inside the object packet in RAM


    # ---------------------------------------------------
    # Getter Function
    # ---------------------------------------------------

    # Getter function is used to READ the value of a private variable
    # It safely returns the value stored inside the object

    def get_marks(self):
        return self.__s_marks


    # ---------------------------------------------------
    # Setter Function
    # ---------------------------------------------------

    # Setter function is used to MODIFY the value of a private variable
    # It allows us to apply conditions before changing the value

    def set_marks(self, new_marks):

        # Applying logical condition before changing marks

        if new_marks >= 0 and new_marks <= 100:
            self.__s_marks = new_marks
            print("Marks updated successfully")

        else:
            print("Invalid marks value entered")


    # ---------------------------------------------------
    # Function to introduce student
    # ---------------------------------------------------

    def s_introduce(self):

        print("Name:", self.s_name)
        print("Age:", self.s_age)

        # accessing private variable inside the class is allowed
        print("Marks:", self.__s_marks)


    # ---------------------------------------------------
    # Function to show result
    # ---------------------------------------------------

    def s_result(self):

        if self.__s_marks >= 50:
            print(self.s_name, "has passed")

        else:
            print(self.s_name, "has failed")



# ---------------------------------------------------
# Creating Object of Student Class
# ---------------------------------------------------

# Now an object is created in RAM

s1 = Student("Ali", 20, 75)

# RAM Concept (simplified)

# s1 object packet in RAM will look conceptually like this:

# ---------------------------------
# | s_name = "Ali"                |
# | s_age = 20                    |
# | __s_marks = 75                |
# | functions of Student class    |
# ---------------------------------
#                ↑
#               s1



# ---------------------------------------------------
# Calling Functions Using Object
# ---------------------------------------------------

s1.s_introduce()

s1.s_result()



# ---------------------------------------------------
# Using Getter Function
# ---------------------------------------------------

# Because marks variable is private we should not access it directly

print("Marks using Getter Function:", s1.get_marks())



# ---------------------------------------------------
# Using Setter Function
# ---------------------------------------------------

# Setter will safely update the value

s1.set_marks(85)

print("Updated Marks:", s1.get_marks())



# ---------------------------------------------------
# Testing Invalid Input
# ---------------------------------------------------

# This value should not be accepted logically

s1.set_marks(150)


# Checking marks again

print("Final Marks:", s1.get_marks())



# ---------------------------------------------------
# Important Concept Summary
# ---------------------------------------------------

# Getter Function
# Used to READ the value of a private variable

# Setter Function
# Used to MODIFY the value of a private variable with validation

# Why Getter and Setter are important?

# 1. Protect object data
# 2. Prevent invalid values
# 3. Apply logical conditions
# 4. Support Encapsulation concept in OOP


# In upcoming lectures we will see how encapsulation,
# inheritance and polymorphism build more powerful systems.