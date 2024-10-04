# class Student:
#     # class properties
#     # attributes (variables) , methods
#     Student_name = "ashish jangid"
#     Student_branch = "it"
#     Student_roll_no = 31
#     def __init__(self,name,city):      # name of constructor is __init__     #  self is like a pointer . it holds address of object.   ## constructor is used to initialize the variables
#         # instance variable
#         self.college_name = name
#         self.college_city = city
#         print("constructor is executed")

# obj = Student(name="jecrc",city="jaipur")

# print(obj.college_name)

# obj2 = Student(name = "poornima",city = "goner jaipur")
# print(obj2.college_name)





#methods inside class

# class Student:
#     # class properties
#     # attributes (variables) , methods
#     #   class variable or global variable
#     Student_name = "ashish jangid"
#     Student_branch = "it"
#     Student_roll_no = 31
#     def __init__(self,name,city):      # name of constructor is __init__     #  self is like a pointer . it holds address of object.   ## constructor is used to initialize the variables
#         # instance variable
#         self.college_name = name
#         self.college_city = city
#         print("constructor is executed")

#     # instance method
#     def display(self):
#         print(self.college_name)
#         print(self.college_city)
    
# obj = Student(name="jecrc",city="jaipur")
# obj.display()




# methods types

# instance method
# class method
# static method
# abstract method
# concrete method



# class method
# class Student:
#     stu_name = 'mohit sharma'
#     stu_roll_no = 21


#     @classmethod      # deporator
#     def display(cls):
#         print(cls.stu_name)
#         print(cls.stu_roll_no)

# obj = Student()
# obj.display()

# print(Student.stu_name)   # accessing class variable without creating object







# class AB:
#     def __init__(self):
#         self.ls = [21,41,52,63,96,85,74,75,84,96,36,251,452,45,142]

#     # # Sum = 0
#     # def average_finder(self):
#     #     Sum = 0
#     #     for i in self.ls:
#     #         Sum += i
#     #     avg = Sum/len(self.ls)
#     #     return avg
# # obj = AB()
# # obj.average_finder()

#     # def position_finder(self,target):
#     #     for i in range(len(self.ls)):
#     #         if target in self.ls:
#     #             print(i)


#     def position_finder(self,target):
#         for i in range(len(self.ls)):
#             if self.ls[i] == target:
#                 print(i)
                


# obj = AB()
# obj.position_finder(85)



## inheritance

# 1.Single 
# 2.Multiple
# 3.Multilevel
# 4.Hybrid
# 5.Heirarchichal



# class A:
#     var_a = "hii from A"
# class B:
#     var_b = "hii from B"

# obj_a = A()
# obj_b = B()

# obj_b.var_b






# inheritance with constructor
# class Father:
#     def __init__(self,name,age):
#         self.father_name = name
#         self.father_age = age

#     def father_biodata(self):
#         print("My father name is : ",self.father_name)
#         print("Age of my father : ",self.father_age)


# # father_obj = Father("Mahaveer",45)
# # obj.father_biodata()

# class Son(Father):
#     son_name = "ritik"
#     son_age = 21
#     def son_biodata(self):
#         print("My name is : ",self.son_name)
#         print("My age is : ",self.son_age)

#     def full_intro(self):
#         #father details
#         #son details
#         self.father_biodata()
#         print()
#         self.son_biodata()

        
        


# son_obj = Son(name = 'Mahaveer',age=45)
# # son_obj.son_biodata()
# # son_obj.father_biodata()
# son_obj.full_intro()

