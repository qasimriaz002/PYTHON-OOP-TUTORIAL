# =====================================================
# Lecture 18 - Inner Classes (Nested Classes in Python)
# =====================================================
# Prepared by Muhammad Qasim Riaz

# =====================================================
# In previous lectures we learned:
# =====================================================

# 1. Abstract Classes and their importance
# 2. Method-level and Object-level Polymorphism
# 3. Working with objects, lists, and dictionaries
# 4. Interaction between different classes

# In this lecture, we will learn:
# → INNER CLASSES (also called Nested Classes)

# =====================================================
# Concept Introduction
# =====================================================

# An Inner Class is a class defined INSIDE another class.

# Syntax:
# class Outer:
#     class Inner:
#         pass

# Key Ideas:
# - Inner classes help logically group related classes
# - Improve code organization and readability
# - Indicate that a class is ONLY useful inside another class

# IMPORTANT NOTE:
# - Inner classes DO NOT automatically access outer class data
# - We must pass outer object explicitly if needed

# =====================================================
# When to Use Inner Classes
# =====================================================

# 1. When a class is only meaningful inside another class
# 2. When you want better code organization
# 3. To avoid polluting global namespace
# 4. For helper/support classes
# 5. For "has-a" relationships

# =====================================================
# Example 1: University and Department
# =====================================================

class University:

    class Department:
        def __init__(self, dept_name):
            self.dept_name = dept_name

        def display(self):
            print("Department:", self.dept_name)

    def __init__(self, uni_name):
        self.uni_name = uni_name

    def show(self):
        print("University:", self.uni_name)


# Demonstration
print("Example 1: University and Department")

u1 = University("ABC University")
u1.show()

d1 = University.Department("Computer Science")
d1.display()

# Explanation:
# - Department is part of University
# - It is grouped inside University for better design

# =====================================================
# Example 2: Car and Engine (Real-Life Model)
# =====================================================

class Car:

    class Engine:
        def __init__(self, horsepower):
            self.hp = horsepower

        def start(self):
            print(f"Engine with {self.hp} HP is starting")

        def stop(self):
            print("Engine stopped")

    def __init__(self, brand):
        self.brand = brand

    def car_info(self):
        print("Car brand:", self.brand)


# Demonstration
print("\nExample 2: Car and Engine")

c1 = Car("Toyota")
c1.car_info()

engine1 = Car.Engine(150)
engine1.start()
engine1.stop()

# Explanation:
# - Engine belongs to Car
# - Inner class improves clarity of relationship

# =====================================================
# Example 3: Interaction Between Outer and Inner Class
# =====================================================

class Company:

    def __init__(self, name):
        self.name = name

    class Employee:
        def __init__(self, emp_name, outer_obj):
            self.emp_name = emp_name
            self.company = outer_obj

        def show(self):
            print("Employee:", self.emp_name)
            print("Company:", self.company.name)


# Demonstration
print("\nExample 3: Company and Employee Interaction")

comp = Company("TechCorp")

emp1 = Company.Employee("Ali", comp)
emp1.show()

# Explanation:
# - Inner class does NOT automatically access outer class
# - We pass outer object manually
# - This enables controlled interaction

# =====================================================
# Advantages of Inner Classes
# =====================================================

# 1. Better organization of related classes
# 2. Improves readability
# 3. Logical encapsulation
# 4. Reduces global namespace pollution
# 5. Good for real-world modeling

# =====================================================
# Limitations of Inner Classes
# =====================================================

# 1. No automatic access to outer class attributes
# 2. Can increase complexity if overused
# 3. Not always necessary

# =====================================================
# When NOT to Use Inner Classes
# =====================================================

# Avoid if:
# - Class is reusable independently
# - Needs heavy interaction with outer class
# - Makes code harder to understand

# =====================================================
# Key Takeaways
# =====================================================

# 1. Inner class = class inside another class
# 2. Used for logical grouping and clean design
# 3. Does NOT automatically access outer class data
# 4. Useful in modeling relationships like Car-Engine
# 5. Helps write organized object-oriented programs

# =====================================================
# End of Lecture 18
# =====================================================