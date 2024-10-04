import os

# pwd

# os.getcwd()

# os.listdir()   ## ls,dir

# pwd

# os.listdir("A:\Photos")  # return current working directory

# os.chdir()       # change directory

# mkdir testing
# os.mkdir('testing')
# os.makedirs('testing',exist_ok=True)

# pwd

# cd testing

# cd..

# os.chdir('testing')

# file = open('demo.txt','x')
# file.close()

# if os.path.exists('demo.txt'):
#     print("already present")
# else:
#     file = open('demo.txt','x')
#     file.close()












# OOP

# two parts:
# 1.core part
# 2.oop part


# class is a blueprint , template
# object or instance

class Student:
    # class properties
    # attributes (variables) , methods
    student_name = "ashish jangid"
    student_branch = "it"
    student_roll_no = 31


# obj = Student()   # object creation

# print(obj.student_name)



## constructor 

    def __init__(self):      # name of constructor is __init__     #  self is like a pointer . it holds address of object.
        # instance variable
        self.college_name = "jecrc"
        self.college_city = "jaipur"
        print("constructor is executed")

obj = Student()

print(obj.student_name)

print(obj.college_name)

obj2 = Student()
obj2.college_name = "poornima"
print(obj2.college_name)