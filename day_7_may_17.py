# for loop and While loop
# for i in range(10):
#     print(i)

# for i in range(5,10):
#     print(i)

# for i in range(5,10,2):
#     print(i)

# lst = [10,20,30,40,50,60,70,80,90]
# print(len(lst))


# for i in range(len(lst)):
#     print(lst[i], end = ' ')   # by default print(i,end="\n") 

# for i in lst:
#     print(i, end = ' ')

# for i in lst:
#     print(i,end="\n")


# company = "jecrc foundation"
# for char in company:
#     print(char)

# company = "jecrc foundation"
# for char in company:
#     if char == 'a':
#         print("a present")

# lst = [12,13,14,18,21,22,24]
# for i in lst:
#     if i%2 == 0:
#         print("even number",i) 
#     else:
#         print("odd number",i)


# for i in range(10):
#     print(i)
#     if i==5:
#         break

# for i in range(10):
#     break
#     print(i)


## continue ignores current iteration only ##

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

# for i in range(10):
#     continue
#     if i == 5:
#         continue
#     print(i)

# count = 0
# for i in range(10):
#     count += 1
#     continue
#     if i == 5:
#         continue
#     print(i)

# print(count)     ## 10

# count = 0
# for i in range(10):
#     count += 1
#     break
#     if i == 5:
#         continue
#     print(i)

# print(count)    ## 1

#### for loop in dictionary ###

d = {'A':0,'B':1,'C':2,'D':3,'E':4}
# for i in d:
#     print(i)

# for i in d.keys():
#     print(i)

# for i in d.values():
#     print(i)

# for i in d.items():
#     print(i)

# for i in d.items():
#     print(i[0])

# for i in d.items():
#     print(i[1])

# for key,value in d.items():
#     print(key  , "-------->" , value)


### tuple unpacking ###

# tpl = ('mohit kumar','cse',101)
# name , branch , roll_no = tpl

# print(name,'\n',branch,'\n',roll_no,'\n')



