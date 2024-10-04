##  MODULE  ##

# accessing functionalities from any other file. 
# eg - from hello.py access lst into test.py

import hello

print(hello.lst)

print(hello.employee_name)
print(hello.employee_id)

print(hello.employee_password)  # we cant access it from hello.py


print(hello.manager_name)