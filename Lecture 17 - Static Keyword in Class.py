# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 17 - Static Keyword in Class
# =====================================================

# In previous lectures we learned:
# 1. Classes & Objects
# 2. Inheritance (Single, Multiple, Multilevel)
# 3. Polymorphism (Method-level & Class/Object-level)
# 4. Abstract Classes
# 5. Passing Objects, Lists, Dictionaries of Objects

# In this lecture, we will learn about the STATIC keyword in Python classes.

# -----------------------------------------------------
# What is a Static Variable?
# -----------------------------------------------------
# - A variable that is shared among all instances (objects) of a class
# - Not unique to a single object
# - Changes to a static variable affect all objects of the class

# -----------------------------------------------------
# What is a Static Method?
# -----------------------------------------------------
# - A method that does not require an object (self) to be called
# - Cannot access instance variables (self.variable)
# - Can access only static/class variables

# =====================================================
# Example 1: Static Variable
# =====================================================

class Student:
    # Static variable
    school_name = "GIK Institute"

    def __init__(self, name, marks):
        self.name = name  # instance variable
        self.marks = marks  # instance variable

    def show_info(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"School Name: {Student.school_name}")  # accessing static variable


# Creating objects
s1 = Student("Ali", 85)
s2 = Student("Sara", 90)

# Accessing instance info
print("=== Student Information ===")
s1.show_info()
print("------")
s2.show_info()

# Changing static variable affects all objects
Student.school_name = "Topi University of Engineering"

print("\n=== After Changing Static Variable ===")
s1.show_info()
print("------")
s2.show_info()


# -----------------------------------------------------
# Explanation:
# -----------------------------------------------------
# 1. school_name is shared among all objects
# 2. Changing Student.school_name updates it for all objects
# 3. Instance variables (name, marks) remain unique to each object


# =====================================================
# Example 2: Static Method
# =====================================================

class Circle:
    pi = 3.14159  # static variable

    def __init__(self, radius):
        self.radius = radius  # instance variable

    # Static method
    @staticmethod
    def circle_area(radius):
        return Circle.pi * radius * radius

    # Instance method for comparison
    def instance_area(self):
        return Circle.pi * self.radius * self.radius


# Using static method without creating object
print("\n=== Static Method Example ===")
print("Area of circle with radius 5:", Circle.circle_area(5))

# Using instance method
c1 = Circle(5)
print("Area using instance method:", c1.instance_area())


# -----------------------------------------------------
# Explanation:
# -----------------------------------------------------
# 1. circle_area() can be called without creating an object
# 2. instance_area() requires an object because it uses self.radius
# 3. Static methods are useful for utility functions related to class


# =====================================================
# Example 3: Practical Mechanical Engineering Example
# =====================================================

class Machine:
    total_machines = 0  # static variable

    def __init__(self, name):
        self.name = name
        Machine.total_machines += 1  # increment static variable

    @staticmethod
    def machine_count():
        print("Total machines created:", Machine.total_machines)


# Creating objects
m1 = Machine("Engine")
m2 = Machine("Generator")
m3 = Machine("Conveyor Belt")

# Access static variable using static method
print("\n=== Machines Example with Static Variable/Method ===")
Machine.machine_count()

# -----------------------------------------------------
# Key Takeaways for Students
# -----------------------------------------------------
# 1. Static variables are shared among all objects of a class
# 2. Static methods can be called without creating an object
# 3. Static methods cannot access instance variables (self.var)
# 4. Useful for:
#    - Counters (e.g., total machines, total students)
#    - Constants (e.g., pi)
#    - Utility functions related to class
# 5. Improves memory efficiency as static variables are not duplicated per object
