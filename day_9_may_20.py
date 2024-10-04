## FILE HANDLING

## open(file_name , mode)

# file = open('hello.txt' , 'r')   ### to open a file in read mode

# file = open('hello.txt' , 'w')   ### to open a file in write mode

# file = open('test.txt' , 'x')    ### to create a file

# file = open('test.txt' , 'w')
# message = """
# we are from jecrc foundation, and we are learning
# about python file handling.
# """
# file.write(message)
# file.close()


# file = open('test.txt','r')
# message = file.read()
# print(message)

## FileExistsError
## FileNotFoundError

# file = open('test.txt')       ### by default read mode
# message = file.read()
# print(message)


# file = open('demo.txt' , 'w')   ### if file do not exist then it will create a demo.txt file and copy the message in it.
# message = """
# we are from jecrc foundation, and we are learning
# about python file handling.
# """
# file.write(message)
# file.close()


#######    write mode clear the old data and then write the new data in it.    #######


# file = open('demo.txt' , 'a')   ### ---> append mode if file do not exist then it will create a demo.txt file and copy the message in it without clearing the old data.
# message = """
# we are from jecrc foundation, and we are learning
# about python file handling.
# """
# file.write(message)
# file.close()      ### save and close the file.

# with open('demo.txt') as file:           ## no  need of writing file.close()
#     data = file.read()
#     print(data)

# with open('demo.txt') as file:           ## we are from jecrc founda   (read upto 25 characters)
#     data = file.read(25)
#     print(data)


## file = open('demo.txt','r')
## data = file.read(25)
## print(data)
##
## message = file.read(25)
## print(message)


# with open('demo.txt','r') as file:
#     data = file.readlines()
#     print(data)
#     print(len(data))



# with open('hello.txt','w') as file:       #### UnicodeEncodeError
#     message = """
#     we are from jecrc foundation, and we are learning
#     about python file handling. 😊😊😊😊
#     """
#     file.write(message)
#     print(message)


# with open('hello.txt','w',encoding = 'utf-8') as file:       
#     message = """
#     we are from jecrc foundation, and we are learning
#     about python file handling. 😊😊😊😊
#     """
#     file.write(message)
#     print(message)


# with open('hello.txt','r',encoding = 'utf-8') as file:       
#     message = """
#     we are from jecrc foundation, and we are learning
#     about python file handling. 😊😊😊😊
#     """
#     file.read(message)
#     print(message)



#### EXCEPTION HANDLING ####

##  try, except, else, finally ##

# name = input("Please write your name : ")
# print('welcome : ',name)

# age = int(input("Enter Your Age : "))
# print('you are ',age,'year old')


# try:
#     age = int(input("Enter Your Age : "))      ### it gives a value error when you enter any other datatype other than integer.
#     print('you are ',age,'year old')

# except:
#     print("please enter a valid input")

# else:                                          ### if error encountered except block runs and if no error else block will run.
#     print("hi from else")

# finally:
#     print('i am from finally and i will runs always.')   ### it will always run whether error encountered or nor.

# print("still i am alive")                      ### it will continue to run the remaining part of the code even if there  is a error above it.


# try:
#     num1 = int(input("enter the first number : "))
#     num2 = int(input("enter the second number : "))
#     result = num1/num2
#     print(result)
# except ZeroDivisionError:
#     print("number cant be divided by zero")

# except ValueError:
#     print("please enter valid input")


