# =====================================================
# Lecture 09 - Inheritance Super Keyword
# =====================================================

# In previous lectures we learned different types of inheritance:
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Access Specifiers with Inheritance

# In those examples we directly accessed variables of parent classes.

# In this lecture we will learn a very useful keyword in Python
# called the SUPER KEYWORD.


# -----------------------------------------------------
# What is super() ?
# -----------------------------------------------------

# super() is used inside a child class to call
# variables or functions of the parent class.

# It helps us avoid writing the parent class name again
# and allows us to reuse parent class functionality easily.

# In simple words:

# super() → gives access to parent class members


# =====================================================
# Example 1
# Basic / Single Inheritance using super()
# =====================================================


# Parent Class

class Person:

    name = None
    age = None

    def set_person(self, n, a):

        self.name = n
        self.age = a


    def introduce(self):

        print("Name:", self.name)
        print("Age:", self.age)



# Child Class

class Student(Person):

    marks = None

    def set_student(self, n, a, m):

        # using super() to call parent class function
        super().set_person(n, a)

        self.marks = m


    def show_result(self):

        print("Marks:", self.marks)



# Creating object

s1 = Student()

s1.set_student("Ali", 20, 75)

# calling parent class function

s1.introduce()

# calling child class function

s1.show_result()



# =====================================================
# Example 2
# Multiple Inheritance using super()
# =====================================================

# Parent Class 1

class Writer:

    topic = None

    def set_writing_topic(self, t):

        self.topic = t


    def write_article(self):

        print("Writing article on:", self.topic)



# Parent Class 2

class Speaker:

    speech_topic = None

    def set_speech_topic(self, t):

        self.speech_topic = t


    def give_speech(self):

        print("Giving speech on:", self.speech_topic)



# Child Class inheriting from both classes

class Trainer(Writer, Speaker):

    trainer_name = None

    def set_trainer(self, name, w_topic, s_topic):

        self.trainer_name = name

        # calling parent class functions

        super().set_writing_topic(w_topic)

        Speaker.set_speech_topic(self, s_topic)


    def introduce_trainer(self):

        print("Trainer Name:", self.trainer_name)



# Creating object

t1 = Trainer()

t1.set_trainer("Dr. Ahmed", "Artificial Intelligence", "Machine Learning")

t1.introduce_trainer()

t1.write_article()

t1.give_speech()



# =====================================================
# Example 3
# Multilevel Inheritance using super()
# =====================================================


# Grandparent Class

class Vehicle:

    brand = None

    def set_brand(self, b):

        self.brand = b


    def show_brand(self):

        print("Vehicle Brand:", self.brand)



# Parent Class

class Car(Vehicle):

    model = None

    def set_car(self, b, m):

        # using super() to call grandparent function

        super().set_brand(b)

        self.model = m


    def show_model(self):

        print("Car Model:", self.model)



# Child Class

class ElectricCar(Car):

    battery = None

    def set_electric_car(self, b, m, battery):

        # using super() to call parent class function

        super().set_car(b, m)

        self.battery = battery


    def show_battery(self):

        print("Battery Capacity:", self.battery)



# Creating object

car1 = ElectricCar()

car1.set_electric_car("Tesla", "Model S", "100 kWh")


# calling functions from all levels

car1.show_brand()

car1.show_model()

car1.show_battery()



# -----------------------------------------------------
# Concept Summary
# -----------------------------------------------------

# super() keyword allows a child class to access
# functions and variables of its parent class.

# Advantages of super()

# 1. Avoids rewriting parent class name
# 2. Makes code cleaner
# 3. Helps reuse parent class functionality


# super() can be used in:

# Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance


# In upcoming lectures we will learn:

# Polymorphism
# Function Overloading
# Function Overriding