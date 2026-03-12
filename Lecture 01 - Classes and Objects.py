# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 01 - Classes & Objects
# =====================================================

# A class representing the characteristics of a real-word student is created below
class Student:
    # creation of variables in class
    s_name = None
    s_age = None
    s_marks = None

    # creation of functions (methods) in the class
    def s_introduce(self):  # self keyword is used to refer own items of class
        print("Name:", self.s_name)  # Here we used the self to call s_name variable of class
        print("Age:", self.s_age)
        print("Marks:", self.s_marks)

    # another function in class
    def s_result(self):
        if self.s_marks >= 50:
            print(self.s_name, "has passed")
        else:
            print(self.s_name, "has failed")


# Here now we are going to create the objects of the above created student class. Consider above class was design
# which tell computer that what a student look like with respect to its data (represented by variables / lists / etc)
# and behaviors (represented by functions). While the objects we are going to create will represent an individual
# student or data of an individual student.

s1 = Student()  # s1 is object of Student class, in ram s1 is complete packet containing all  variables and functions.
s1.s_name = "Ali"  # s_name is a variable stored in packet of s1 created in the ram, here we allocated a value to it.
s1.s_age = 20  # s_age is a variable stored in packet of s1 created in the ram, here we allocated a value to it.
s1.s_marks = 55  # s_marks is a variable stored in packet of s1 created in the ram, here we allocated a value to it.

# Now we can call any function of class Student by using the object s1 because copy of every function is created for s1
# in the packet of the s1 object due to use of self keyword the s1 object will be able to use s_name, s_age, s_marks
# variable of the same packet s1 will be

s1.s_introduce()    # Calling s_introduce() using s1 because s1 is object of student class. Using data of s1 variables.
s1.s_result()   # Calling s_result() using s1 because s1 is object of student class. Using data of s1 variables.

