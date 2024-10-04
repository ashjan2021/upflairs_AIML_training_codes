# while loop

# i = 0
# while i <= 10:
#     print(i)
#     i+=1

# quit = False
# while not quit:
#     user_input = input('Do you want to quit it pree Y/N : ')
#     if user_input == 'Y' or user_input == 'y':
#         print("Hello world")
#     elif user_input == 'N' or user_input == 'n':
#         break
        
#         quit = True




#____ FUNCTIONS ____

# user defined
# built in function

# def addtwo(num1,num2):
#     result = num1+ num2
#     print(result)

# addtwo(num1=10,num2=20)


# ## calling
# def addtwo(num1,num2):
#     result = num1+ num2
#     return result               # it is used as a break , output , variables memory release
#     print("hi i am still alive")    # it will not print this statement as return works as break statement

# addtwo(num1=10,num2=20)
# # output = addtwo(num1=10,num2=20)
# # print(output)

# output=addtwo(10,20)
# print(output)

# lst = [10,50,63,4,78,9,6,82,63,1,5]

# def my_len(lst):
#     count = 0
#     for i in lst:
#         count+=1
#     return count

# output = my_len(lst)
# print(output)


#     size = int(input("Enter the size of list : "))
#     lst = []
#     for i in range(size):
#         element = int(input("enter the element for list : "))
#         lst.append(element)


        
#  Function for count even number

# lst = [10,50,63,4,78,9,6,82,63,1,5]
# def count_even(lst):
#     count = 0
#     for num in lst:
#         if num % 2 == 0:
#             count += 1
#     return count
    

# print(count_even(lst))


# lst = [10,50,63,4,78,9,6,82,63,1,5,54,63,74,14,96,25]

# def GT(lst):
#     count = 0
#     for num in lst:
#         if num > 50:
#             count +=1
#     return count

# print(GT(lst))





