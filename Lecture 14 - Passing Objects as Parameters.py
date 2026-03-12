# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 14 - Passing Objects as Parameters & Using Lists/Dictionaries of Objects
# =====================================================

# In previous lectures we learned:
# 1. Classes & Objects
# 2. Lists of Objects in Classes
# 3. Inheritance
# 4. Polymorphism (Overloading & Overriding)

# In this lecture, we will learn:
# - How to pass objects as function parameters
# - How to work with lists and dictionaries of objects


# =====================================================
# Example 1: Passing a Single Object as a Parameter
# =====================================================

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(f"Student: {self.name}, Marks: {self.marks}")


# Function to check if student has passed
def check_result(student_obj):
    print("Checking pass/fail for student:", student_obj.name)
    if student_obj.marks >= 50:
        print("Result: Passed")
    else:
        print("Result: Failed")
    print("------")


# Creating a Student object
s1 = Student("Ali", 85)

# Passing object to function
check_result(s1)


# =====================================================
# Example 2: Passing List of Objects as Parameter
# =====================================================

# Creating more students
s2 = Student("Sara", 45)
s3 = Student("Ahmed", 78)
s4 = Student("Zoya", 92)

# List of students
students_list = [s1, s2, s3, s4]

# Function to display all students and results
def show_all_students(student_list):
    for student in student_list:
        student.show()
        if student.marks >= 50:
            print("Result: Passed")
        else:
            print("Result: Failed")
        print("------")


# Passing list of objects
show_all_students(students_list)


# =====================================================
# Example 3: Passing Dictionary of Objects as Parameter
# =====================================================

# Dictionary with course codes as keys and Student objects as values
students_dict = {
    "ME101": s1,
    "EE102": s2,
    "ME103": s3,
    "CS104": s4
}

# Function to display students from dictionary
def show_students_from_dict(student_dict):
    for course_code, student_obj in student_dict.items():
        print("Course Code:", course_code)
        student_obj.show()
        if student_obj.marks >= 50:
            print("Result: Passed")
        else:
            print("Result: Failed")
        print("------")


# Passing dictionary of objects
show_students_from_dict(students_dict)


# =====================================================
# Example 4: Nested Example - Courses Containing Lists of Students
# =====================================================

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []  # list of Student objects

    def add_student(self, student_obj):
        self.students.append(student_obj)

    def show_course_students(self):
        print("Course:", self.course_name)
        for student in self.students:
            student.show()
        print("------")


# Creating Courses
course1 = Course("Mechanical Engineering")
course1.add_student(s1)
course1.add_student(s3)

course2 = Course("Electrical Engineering")
course2.add_student(s2)
course2.add_student(s4)

# Function to display all courses and their students
def show_all_courses(course_list):
    for course in course_list:
        course.show_course_students()


# List of courses
courses = [course1, course2]

# Passing list of course objects
show_all_courses(courses)


# =====================================================
# Concept Explanation
# =====================================================

# 1. Single Object as Parameter
#    - Pass one object and access its attributes/functions inside the function

# 2. List of Objects
#    - Pass a list of objects
#    - Use loops to access each object
#    - Useful for batch processing, e.g., all students in a course

# 3. Dictionary of Objects
#    - Allows mapping keys (e.g., course codes) to objects
#    - Useful for structured access

# 4. Nested Objects
#    - A Course object can have a list of Student objects
#    - Functions can take lists of Course objects
#    - Shows hierarchy and real-world OOP modeling

# 5. Practical Tip
#    - Always ensure the function knows which object it is handling
#    - Use clear loops and print statements for clarity
#    - This technique is widely used in data management, simulation, and engineering applications