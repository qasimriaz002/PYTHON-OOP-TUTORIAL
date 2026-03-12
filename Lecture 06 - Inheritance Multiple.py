# =====================================================
# Lecture 06 - Inheritance Multiple
# =====================================================

# In previous lecture we learned about basic inheritance
# where one child class inherits from one parent class.

# Parent Class  →  Child Class

# In this lecture we will learn about another important
# type of inheritance called MULTIPLE INHERITANCE.


# -----------------------------------------------------
# What is Multiple Inheritance?
# -----------------------------------------------------

# Multiple inheritance means that a single child class
# inherits properties from more than one parent class.

# Structure:

# Parent Class A        Parent Class B
#           \            /
#            \         /
#            Child Class


# This means the child class can use variables and
# functions from BOTH parent classes.


# -----------------------------------------------------
# Real World Example
# -----------------------------------------------------

# Consider a Smart Device.

# A smart device may behave like:

# 1. A Camera
# 2. A Music Player

# If we create a SmartPhone class,
# it may inherit features from both:

# Camera class
# MusicPlayer class


# -----------------------------------------------------
# Parent Class 1
# -----------------------------------------------------

class Camera:
    camera_resolution = None

    def take_picture(self):
        print("Picture captured with resolution:", self.camera_resolution)


# -----------------------------------------------------
# Parent Class 2
# -----------------------------------------------------

class MusicPlayer:
    song_name = None

    def play_music(self):
        print("Playing song:", self.song_name)


# -----------------------------------------------------
# Child Class
# -----------------------------------------------------

# SmartPhone inherits from both Camera and MusicPlayer

class SmartPhone(Camera, MusicPlayer):
    brand = None

    def phone_info(self):
        print("Smart Phone Brand:", self.brand)


# -----------------------------------------------------
# Creating Object of Child Class
# -----------------------------------------------------

phone1 = SmartPhone()

# Assigning values

phone1.brand = "Samsung"
phone1.camera_resolution = "48 MP"
phone1.song_name = "Favorite Song"

# -----------------------------------------------------
# Conceptual RAM Packet of phone1
# -----------------------------------------------------

# ---------------------------------------------
# | brand = "Samsung"         (child class)    |
# | camera_resolution = 48MP  (Camera class)   |
# | song_name = "Favorite"    (MusicPlayer)    |
# | phone_info()              (child class)    |
# | take_picture()            (Camera class)   |
# | play_music()              (MusicPlayer)    |
# ---------------------------------------------
#                    ↑
#                  phone1


# -----------------------------------------------------
# Calling Functions
# -----------------------------------------------------

phone1.phone_info()

phone1.take_picture()

phone1.play_music()


# -----------------------------------------------------
# Another Simple Example
# -----------------------------------------------------

# Parent Class 1

class Writer:
    writing_topic = None

    def write_article(self):
        print("Writing article on:", self.writing_topic)


# Parent Class 2

class Speaker:
    speaking_topic = None

    def give_speech(self):
        print("Giving speech on:", self.speaking_topic)


# Child Class inheriting from both parents

class Trainer(Writer, Speaker):
    trainer_name = None

    def introduce_trainer(self):
        print("Trainer Name:", self.trainer_name)


# -----------------------------------------------------
# Creating Object
# -----------------------------------------------------

t1 = Trainer()

t1.trainer_name = "Dr. Ahmed"
t1.writing_topic = "Artificial Intelligence"
t1.speaking_topic = "Machine Learning"

# Calling functions

t1.introduce_trainer()

t1.write_article()

t1.give_speech()

# -----------------------------------------------------
# Concept Summary
# -----------------------------------------------------

# Multiple Inheritance means:

# One child class inherits properties
# from more than one parent class.

# Example Structure

# Parent Class A
# Parent Class B
#        ↓
#     Child Class


# Advantages

# 1. Code reuse from multiple classes
# 2. Combination of different functionalities
# 3. More flexible class design


# In upcoming lectures we will learn:

# 1. Multilevel Inheritance
# 2. Diamond Problem in Multiple Inheritance
# 3. Method Resolution Order (MRO)
