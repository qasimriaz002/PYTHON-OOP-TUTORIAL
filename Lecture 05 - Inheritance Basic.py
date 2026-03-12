# =====================================================
# Lecture 05 - Inheritance Basic
# =====================================================

# In previous lectures we learned:
# 1. Classes and Objects
# 2. Constructors and Destructors
# 3. Getter and Setter Functions
# 4. Encapsulation and Access Specifiers

# In this lecture we will learn an important concept of
# Object-Oriented Programming called INHERITANCE.


# -----------------------------------------------------
# What is Inheritance?
# -----------------------------------------------------

# Inheritance means creating a new class from an existing class.

# The new class automatically gets the variables and functions
# of the existing class.

# Existing class → Parent Class
# New class → Child Class


# -----------------------------------------------------
# Real-world Example
# -----------------------------------------------------

# Consider a PERSON.

# Every person has some common properties:
#   name
#   age

# But there are different types of persons such as:
#   Student
#   Teacher
#   Admin

# Instead of writing name and age again and again
# in every class we can create a general class called Person
# and other classes can inherit its properties.


# -----------------------------------------------------
# Example 1
# Simple / Single Inheritance
# One Parent Class → One Child Class
# -----------------------------------------------------


# Parent Class

class Person:

    # variables of parent class
    name = None
    age = None


    # function of parent class
    def introduce(self):

        print("Name:", self.name)
        print("Age:", self.age)



# Child Class
# Student class inherits from Person class

class Student(Person):

    # additional variable of student class
    marks = None


    # function of student class
    def show_result(self):

        if self.marks >= 50:
            print(self.name, "has passed")

        else:
            print(self.name, "has failed")



# -----------------------------------------------------
# Creating Object of Student Class
# -----------------------------------------------------

# Object is created in RAM

s1 = Student()

# Assigning values

s1.name = "Ali"
s1.age = 20
s1.marks = 65


# Conceptual RAM packet of s1 object

# -----------------------------------------
# | name = "Ali"       (from parent class) |
# | age = 20           (from parent class) |
# | marks = 65         (from child class)  |
# | introduce()        (from parent class) |
# | show_result()      (from child class)  |
# -----------------------------------------
#                 ↑
#                s1


# Calling functions

s1.introduce()     # inherited function from parent class
s1.show_result()   # function of student class



# -----------------------------------------------------
# Example 2
# One Parent Class → Multiple Child Classes
# -----------------------------------------------------

# Here we create a general Person class
# and multiple specialized classes that inherit from it.


# Parent Class

class Person:

    name = None
    age = None


    def introduce(self):

        print("Name:", self.name)
        print("Age:", self.age)



# -----------------------------------------------------
# Child Class 1
# -----------------------------------------------------

class Student(Person):

    department = None


    def show_student(self):

        print(self.name, "is studying in", self.department, "department")



# -----------------------------------------------------
# Child Class 2
# -----------------------------------------------------

class Teacher(Person):

    subject = None


    def show_teacher(self):

        print(self.name, "teaches", self.subject)



# -----------------------------------------------------
# Child Class 3
# -----------------------------------------------------

class Admin(Person):

    role = None


    def show_admin(self):

        print(self.name, "works as", self.role)



# -----------------------------------------------------
# Creating Objects of Different Child Classes
# -----------------------------------------------------

stu1 = Student()
stu1.name = "Ahmed"
stu1.age = 21
stu1.department = "Mechanical Engineering"


teach1 = Teacher()
teach1.name = "Dr. Khan"
teach1.age = 45
teach1.subject = "Thermodynamics"


admin1 = Admin()
admin1.name = "Mr. Bilal"
admin1.age = 40
admin1.role = "Registrar Office"



# -----------------------------------------------------
# Calling Functions
# -----------------------------------------------------

# Student object

stu1.introduce()
stu1.show_student()

print("----------------------")

# Teacher object

teach1.introduce()
teach1.show_teacher()

print("----------------------")

# Admin object

admin1.introduce()
admin1.show_admin()



# -----------------------------------------------------
# Concept Summary
# -----------------------------------------------------

# Inheritance allows one class to use properties of another class.

# Parent Class
# The class whose properties are inherited.

# Child Class
# The class which inherits properties of another class.


# Advantages of Inheritance:

# 1. Code Reusability
# 2. Less Code Duplication
# 3. Easier Program Maintenance
# 4. Logical Class Relationships


# In upcoming lectures we will learn:

# 1. Constructors in inheritance
# 2. super() keyword
# 3. Multiple inheritance
# 4. Multilevel inheritance
# 5. Diamond problem