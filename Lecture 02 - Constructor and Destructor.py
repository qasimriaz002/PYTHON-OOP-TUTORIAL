# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 02 - Constructors & Destructors
# =====================================================


# In this lecture we will understand the concept of constructor & destructor.
# CONSTRUCTOR - it is a kind of function that is called directly when object of class is created.
# DESTRUCTOR - it is a kind of function that called directly when object of class is removed from memory.

class Student:

    # Creation of constructor. We use constructors when we want to do some task at time of creation of object.
    # It is a type of function which is always created with __init__() keyword.
    # Constructor functions are mostly used to initialize class level variable.
    # Following constructor functions take 3 parameters name, age, marks and 4th one "self" keyword.
    # Self is compulsory to be added as parameter so that all variables / functions of class level can be called in it.
    # You can see we have created three variable self.s_name, self.s_age, self.s_marks in constructor.
    # Self is used with s_name, s_age, s_marks so that these three variables can be used even outside the constructor.
    # s_name = name, s_age = age, s_marks = marks ---> because values received by parameters will be allocated to them.
    def __init__(self, name, age, marks):
        self.s_name = name
        self.s_age = age
        self.s_marks = marks

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

    # Creation of destructor, We use destructors when we want to do some task at time of deletion of object from RAM.
    # Destructors mostly don't have parameters other than self.
    # Destructors can also be called using the "del" keyword with object means to delete object from memory.
    # Because when "del" keyword is used then object is removed from memory and destructor is triggered and run
    # If delete is not used by developer in any program then all objects are deleted from memory automatically.
    # When all objects are deleted from memory then destructors called automatically.
    # Destructors of all objects are called before the program is completely executed and removed from RAM.
    def __del__(self):
        print("The object of student " + str(self.s_name) + " is deleted from memory")


# Here when we will create the first object of Student class you will see how constructor is being called.
# Now s1 is created with values "Ali", 20, 55 because all of them are send to s1 object.
# You can see Student(Ali, 20, 55) all values of parameters will be sent to parametric variables of __init__().
# Means name variable of __init__() will be allocated "Ali" similarly age and marks variables will be allocated 20, 55.
# Once values are allocated to name, age, marks variables then all these will be allocated to s_name, s_age, s_marks.
# Then the s1 objects packet in memory will contain 3 variables s_name, s_age, s_marks and two functions as in class.
s1 = Student("Ali", 20, 55)
s1.s_introduce()
s1.s_result()
print("------------------------")

# Similarly we can even create the other objects which will also have their own packets in memory.
s2 = Student("Usman", 19, 48)
s2.s_introduce()
s2.s_result()
print("------------------------")
s3 = Student("Ayesha", 18, 52)
s3.s_introduce()
s3.s_result()
print("------------------------")
# All variables of s1,s2 and s3 will have separate memory for all variables and functions
# For example we can see s1.s_introduce() and s2.s_introduce() shows separate introduction because of separate memory.
s1.s_introduce()
print("------------------------")
s2.s_introduce()
print("------------------------")

# Now I am using the "del" keyword to delete the object s2 from memory manually
print("Destructor of s1 is called here using del keyword")
del s2
print("------------------------")
# As the "del" keyword with the other objects s1 and s3 is not used the destructor for both will be called automatic.
print("Other Destructors being called automatically because execution of program is completed and removed from RAM")

