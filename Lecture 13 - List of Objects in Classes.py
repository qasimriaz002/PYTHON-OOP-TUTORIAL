# =====================================================
# Lecture 13 - List of Objects in Class
# =====================================================

# In previous lectures we learned:
# 1. Classes & Objects
# 2. Inheritance (Single, Multiple, Multilevel)
# 3. Polymorphism (Overloading & Overriding)
# 4. super() keyword

# In this lecture, we will learn how to use **lists of objects**
# inside another class. This is very useful in real-life scenarios,
# e.g., University having many Courses, Courses having many Students.


# =====================================================
# Example 1: University has list of Courses, Courses have Students
# =====================================================

# Class representing a Student

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def show_student(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)



# Class representing a Course
# Each course contains a list of Student objects

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students_list = []   # List to store Student objects

    # Add a student object to the course
    def add_student(self, student_obj):
        self.students_list.append(student_obj)

    # Show all students in the course
    def show_students(self):
        print("Course:", self.course_name)
        print("Enrolled Students:")
        for student in self.students_list:
            student.show_student()
            print("------")



# Class representing a University
# University contains a list of Course objects

class University:
    def __init__(self, uni_name):
        self.uni_name = uni_name
        self.courses_list = []   # List to store Course objects

    # Add a course object to the university
    def add_course(self, course_obj):
        self.courses_list.append(course_obj)

    # Show all courses and their students
    def show_courses(self):
        print("University:", self.uni_name)
        print("======================")
        for course in self.courses_list:
            course.show_students()
            print("*******************")


# =====================================================
# Creating Student Objects
# =====================================================

s1 = Student("Ali", 20, 85)
s2 = Student("Sara", 21, 90)
s3 = Student("Ahmed", 19, 78)
s4 = Student("Zoya", 22, 88)


# =====================================================
# Creating Course Objects and adding Students
# =====================================================

course1 = Course("Mechanical Engineering")
course1.add_student(s1)
course1.add_student(s2)

course2 = Course("Electrical Engineering")
course2.add_student(s3)
course2.add_student(s4)


# =====================================================
# Creating University Object and adding Courses
# =====================================================

uni = University("GIK Institute")
uni.add_course(course1)
uni.add_course(course2)


# =====================================================
# Display all Courses and Students
# =====================================================

uni.show_courses()


# =====================================================
# Concept Explanation
# =====================================================

# 1. We created a list inside Course class to store Student objects.
#    This allows a Course to keep track of all enrolled students.

# 2. Similarly, University class has a list of Course objects.
#    This allows a University to manage multiple courses.

# 3. Using this approach, we can organize data hierarchically:
#    University → Courses → Students

# 4. Accessing objects:
#    - We can access individual student objects from courses_list
#    - We can access courses from university object
#    - Using loops, we can iterate over lists to perform actions
#      for each object (e.g., display, modify, compute)


# =====================================================
# Additional Notes for Students
# =====================================================

# - You can add methods to remove students or courses.
# - You can also pass lists of objects directly when creating objects.
# - This technique is widely used in real-life applications,
#   e.g., managing inventory, employees, machines, etc.

# Example: Accessing individual students directly

print("\nAccessing Individual Student Directly:")
first_course = uni.courses_list[0]
first_student = first_course.students_list[0]
print("First Student in first course:")
first_student.show_student()