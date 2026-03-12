# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 16 - Polymorphism with Abstract Classes
# =====================================================

# In previous lectures we learned:
# 1. Method/Function Level Polymorphism:
#    - Function Overloading (compile-time polymorphism)
#    - Function Overriding (runtime polymorphism)
# 2. Abstract Classes
# 3. Passing objects, lists, dictionaries of objects
# 4. Lists of objects and nested objects

# In this lecture, we will learn CLASS / OBJECT LEVEL POLYMORPHISM

# -----------------------------------------------------
# Concept Introduction
# -----------------------------------------------------

# Method-level polymorphism: we already saw
# - Function Overloading → same method name, different parameters
# - Function Overriding → child class method replaces parent method

# Object-level polymorphism (Class-level polymorphism):
# - The same function call can behave differently depending on
#   the type of the OBJECT calling it
# - We want a **generic object** that behaves differently depending on its type
# - Abstract Classes + Overriding provide exactly this solution
#   because they enforce a common interface for different object types

# =====================================================
# Example 1: Human Life Cycle
# =====================================================

from abc import ABC, abstractmethod


# Abstract Class representing a Human
class Human(ABC):
    @abstractmethod
    def role(self):
        pass


# Child Class - Student
class Student(Human):
    def role(self):
        print("I am a student, learning new skills.")


# Child Class - Engineer
class Engineer(Human):
    def role(self):
        print("I am an engineer, building and designing things.")


# Child Class - President
class President(Human):
    def role(self):
        print("I am the president, leading the country.")


# -----------------------------------------------------
# Polymorphism Demonstration
# -----------------------------------------------------

# A single variable (generic human object) can refer to different
# types of Human objects (Student, Engineer, President)
# This is object-level polymorphism in action
human_life = [Student(), Engineer(), President()]

print("Human Life Cycle Polymorphism Example:")
for stage in human_life:
    stage.role()  # Same method call, behaves differently based on object type


# -----------------------------------------------------
# Explanation for Students
# -----------------------------------------------------

# 1. We cannot create a plain Human object: Human() → TypeError
#    because Human is abstract. Abstract classes enforce that child classes
#    implement the required methods (here, role()).
# 2. Using a list of different Human child objects lets us call the same
#    method on all objects → CLASS/OBJECT LEVEL POLYMORPHISM
# 3. A “generic human variable” can point to a Student object, then
#    to an Engineer object, then to a President object:
#       human_var = Student()
#       human_var.role()
#       human_var = Engineer()
#       human_var.role()
# 4. Without abstract classes, we cannot ensure that every child class
#    implements role(), and calling human_var.role() may fail or
#    lead to inconsistent behavior.

# =====================================================
# Example 2: Machines
# =====================================================

# Abstract Class representing a Machine
class Machine(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Child Class - Engine
class Engine(Machine):
    def start(self):
        print("Engine starting with fuel ignition")

    def stop(self):
        print("Engine stopping and fuel cut-off")


# Child Class - Generator
class Generator(Machine):
    def start(self):
        print("Generator starting with electric supply")

    def stop(self):
        print("Generator shutting down safely")


# Child Class - ConveyorBelt
class ConveyorBelt(Machine):
    def start(self):
        print("Conveyor Belt starts moving")

    def stop(self):
        print("Conveyor Belt stops")


# List of different machine objects
machines = [Engine(), Generator(), ConveyorBelt()]

print("\nMachines Polymorphism Example:")
print("Starting all machines using polymorphism:")
for machine in machines:
    machine.start()  # Same method call, behaves differently based on object type

print("\nStopping all machines using polymorphism:")
for machine in machines:
    machine.stop()


# =====================================================
# Example 3: Shapes
# =====================================================

# Abstract Class representing a Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Child Class - Circle
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def perimeter(self):
        return 2 * 3.14 * self.r


# Child Class - Rectangle
class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def perimeter(self):
        return 2 * (self.l + self.w)


# List of shapes (different child classes)
shapes = [Circle(5), Rectangle(4, 6)]

print("\nShapes Polymorphism Example:")
for shape in shapes:
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
    print("------")

# =====================================================
# Key Takeaways
# =====================================================

# 1. Class/Object level polymorphism allows the same code to work
#    with different types of objects.
# 2. Abstract classes enforce a common interface → ensures
#    all child classes implement required methods.
# 3. Using lists of different child objects, we can call the same
#    method on all of them without knowing their specific type.
# 4. Human Life Cycle example shows a real-life intuitive example
#    of polymorphism.
# 5. Machines and Shapes examples show practical engineering applications.
