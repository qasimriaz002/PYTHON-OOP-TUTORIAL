# =====================================================
# Lecture 08 - Inheritance Access Specifiers
# =====================================================

# In previous lectures we learned different types of inheritance:
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance

# In this lecture we will learn how ACCESS SPECIFIERS behave
# when inheritance is used.

# Access specifiers control how variables and functions of a class
# can be accessed in:
#   1. Own class
#   2. Child class
#   3. Grandchild class
#   4. Outside the class


# -----------------------------------------------------
# Types of Access Specifiers in Python
# -----------------------------------------------------

# 1. Public      → variable
# 2. Protected   → _variable
# 3. Private     → __variable


# -----------------------------------------------------
# Parent Class
# -----------------------------------------------------

class Person:

    # PUBLIC VARIABLE
    name = None

    # PROTECTED VARIABLE
    _age = None

    # PRIVATE VARIABLE
    __salary = None


    # Function to assign values
    def set_person_data(self):

        self.name = "Ali"
        self._age = 35
        self.__salary = 50000


    # Function inside same class accessing all variables
    def show_person_data(self):

        print("Name:", self.name)       # Public
        print("Age:", self._age)        # Protected
        print("Salary:", self.__salary) # Private



# -----------------------------------------------------
# Child Class
# -----------------------------------------------------

class Employee(Person):

    department = None

    def show_employee_data(self):

        print("Accessing variables inside CHILD class")

        # Public variable → accessible
        print("Name:", self.name)

        # Protected variable → accessible
        print("Age:", self._age)

        # Private variable → NOT accessible directly
        # print(self.__salary)  # This will cause error

        print("Private variable cannot be accessed directly in child class")



# -----------------------------------------------------
# Grand Child Class
# -----------------------------------------------------

class Manager(Employee):

    level = None

    def show_manager_data(self):

        print("Accessing variables inside GRANDCHILD class")

        # Public variable → accessible
        print("Name:", self.name)

        # Protected variable → accessible
        print("Age:", self._age)

        # Private variable → NOT accessible
        # print(self.__salary)  # This would cause error

        print("Private variable cannot be accessed in grandchild class")



# -----------------------------------------------------
# Creating Object
# -----------------------------------------------------

m1 = Manager()

# Assigning values through parent class function

m1.set_person_data()


# -----------------------------------------------------
# Calling functions
# -----------------------------------------------------

print("Accessing from Parent Class Function")

m1.show_person_data()

print("----------------------------")

print("Accessing from Child Class Function")

m1.show_employee_data()

print("----------------------------")

print("Accessing from Grand Child Class Function")

m1.show_manager_data()

print("----------------------------")


# -----------------------------------------------------
# Accessing Variables Outside Class
# -----------------------------------------------------

print("Accessing variables OUTSIDE class")

# Public variable → accessible

print("Public Name:", m1.name)


# Protected variable → technically accessible but not recommended

print("Protected Age:", m1._age)


# Private variable → NOT accessible

# print(m1.__salary)  # This will cause error

print("Private variable cannot be accessed outside class")



# -----------------------------------------------------
# Concept Summary
# -----------------------------------------------------

# PUBLIC VARIABLES
#   Accessible everywhere
#   Own class
#   Child class
#   Grandchild class
#   Outside class


# PROTECTED VARIABLES
#   Accessible in:
#   Own class
#   Child class
#   Grandchild class

#   But should not be accessed outside class
#   (although Python technically allows it)


# PRIVATE VARIABLES
#   Accessible ONLY inside the class where they are defined

#   Not accessible in:
#   Child class
#   Grandchild class
#   Outside class



# -----------------------------------------------------
# Access Specifier Comparison Table
# -----------------------------------------------------

# Access Location        Public             Protected                   Private

# Own Class               Yes               Yes                         Yes
# Child Class             Yes               Yes                         No
# Grand Child Class       Yes               Yes                         No
# Outside Class           Yes               Possible(Not recommended)   No
#                                           As per the rules of oop
#                                           not possible and even
#                                           not allowed but as per
#                                           rules of python it is
#                                           possible but not recommended
#                                           and not allowed as it is
#                                           actually against the rules
#                                           of oop.



# In upcoming lectures we will learn:

# Polymorphism
# Function Overloading
# Function Overriding