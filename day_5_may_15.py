## __Dictionary{}__
#mutable
#key:value pairs

# dt = {'a':10,'b':20,'c':30,'d':[1,2,3,4,5]}

# print(dt['d'])
# dt['a'] = 50
# print(dt)
# print(dt.keys())
# print(dt.values())

#__Set__
#unordered, unchangeable, heterogenous, unique (no duplicacy of data)
#no indexing or slicing allowed

# S = {20,'Jessa',35.75}
# print(S)
# print(type(S))

# S = {1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8}      #{1, 2, 3, 4, 5, 6, 7, 8}
# print(S)
# print(type(S))


#__TYPE CASTING__
# casting one datatype into other datatype
# set(),int(),float(),bool(),list(),tuple()

# ls = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
# print(set(ls))

# st = {1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8}      #{1, 2, 3, 4, 5, 6, 7, 8}
# print(st)

# st.add(100)
# print(st)
# st.remove(1)
# print("after removal",st)
# st.remove(101)
# print("after removal",st)    ## it will give error if element is not present in set
# st.discard(100)
# print("after removal",st)
# st.discard(101)
# print("after removal",st)   ## it will not give error even if element is not present in set




## ARITHMETIC OPERATORS(+,-,#,/,%,**,//)
# Addition +
# Subtraction -
# Division /
# Modulus %
# Exponential **
# Floor Division //

# num1 = 10
# num2 = 20
# result = num1 + num2
# print(result)

# num1 = int(input("please enter first number : "))
# num2 = int(input("please enter second number : "))
# result = num1 + num2
# print(result)


## Comparision Operators(<,>,<=,>=,==,!=)

#if elif else
# num1 = int(input("please enter first number : "))
# num2 = int(input("please enter second number : "))

# if num1 > num2:
#     print("num1 is greater than num2")

# elif num1 == num2:
#     print("Both are equal")

# else:
#     print("num2 is greater than num1")


## Logical Operators(and,or,not)

# age = int(input('plz enter age'))

# if age>24 and age<100;
#     print("eligible for vote")

# else:
#     print("Not eligible for vote")


## ASSIGNMENT OPERATOTRS (=,+=,-=,*=)

# num = 10
# num += 1   # num = num + 1

## MEMBERSHIP OPERATORS (in (true if exists), not in (true if not exists))

# fruits = ['mango','banana','apple','grapes']
# if 'mango' in fruits:
#     print('available')
# else:
#     print('not available')

## FOR LOOP
# for i in range(10)
#     print(i)
