# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 15 - Abstract Classes
# =====================================================

# In previous lectures we learned:
# 1. Classes & Objects
# 2. Inheritance (Single, Multiple, Multilevel)
# 3. Function Overloading & Overriding
# 4. Passing Objects and Lists/Dictionaries of Objects

# In this lecture, we will learn about ABSTRACT CLASSES
# which are used to define a common interface for child classes.

# -----------------------------------------------------
# What is an Abstract Class?
# -----------------------------------------------------

# An abstract class is a class that **cannot be instantiated** directly.
# It is meant to be a blueprint for other classes.
# It may contain one or more **abstract methods** that MUST be implemented
# by any child class.

# Abstract classes in Python are created using the **abc module**.

# =====================================================
# Example 1: Basic Abstract Class
# =====================================================

# Import ABC and abstractmethod from abc module
from abc import ABC, abstractmethod

# Create an abstract class called Machine
class Machine(ABC):

    # Abstract method
    @abstractmethod
    def start(self):
        pass  # No implementation, just a placeholder

    # Another abstract method
    @abstractmethod
    def stop(self):
        pass


# -----------------------------------------------------
# Trying to create an object of Machine
# -----------------------------------------------------

# Uncommenting the following line will give an error
# because abstract class cannot be instantiated directly
# m1 = Machine()   # TypeError: Can't instantiate abstract class Machine with abstract methods start, stop

# -----------------------------------------------------
# Child Class Must Implement Abstract Methods
# -----------------------------------------------------

class Engine(Machine):
    # Implementing abstract methods

    def start(self):
        print("Engine has started")

    def stop(self):
        print("Engine has stopped")


# Now we can create an object of Engine
e1 = Engine()
e1.start()   # Output: Engine has started
e1.stop()    # Output: Engine has stopped

# -----------------------------------------------------
# Explanation
# -----------------------------------------------------

# 1. Machine is an abstract class → cannot create Machine objects
# 2. Engine is a concrete child class → must implement all abstract methods
# 3. Abstract methods define a contract/interface → ensures uniform behavior
# 4. If Engine did NOT implement start or stop, Python would raise an error

# =====================================================
# Example 2: Abstract Classes with Multiple Child Classes
# =====================================================

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Child Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Child Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Creating objects of child classes
c1 = Circle(5)
r1 = Rectangle(4, 6)

print("\nCircle Area:", c1.area())
print("Circle Perimeter:", c1.perimeter())
print("\nRectangle Area:", r1.area())
print("Rectangle Perimeter:", r1.perimeter())

# -----------------------------------------------------
# Key Learning Points
# -----------------------------------------------------

# 1. Abstract class cannot be instantiated
# 2. Abstract methods must be implemented in child classes
# 3. Helps in designing **common interface** for multiple classes
# 4. Ensures **polymorphism** → we can store different child objects
#    and call the same method safely

# Example: Polymorphism with Abstract Classes
shapes_list = [c1, r1]  # list of different Shape objects

for shape in shapes_list:
    print("\nArea:", shape.area())
    print("Perimeter:", shape.perimeter())

# All objects respond to area() and perimeter(), even though
# they are different types (Circle, Rectangle)
# This is runtime polymorphism using abstract classes