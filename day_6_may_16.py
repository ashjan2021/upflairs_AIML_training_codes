#nested if-else
# ATM SIMULATION PROGRAM

name = input("Please enter yout name : \n")
print("Welcome",name,'\n')

print("""
plz choose your task :
Type --> 1 for check balance
Type --> 2 for deposit amount
Type --> 3 for withdraw amount
""")

task = int(input("Enter your task : "))
current_available_balance =  5000

pin = 2021
entered_pin = int(input("enter your pin : "))
if entered_pin == 2021:

    if task >= 1 and task <= 3:

        if task == 1:
            print("your available balance is : ",current_available_balance)

        elif task == 2:
            deposit_amount = int(input("How much amount you want to deposit : "))

            if deposit_amount > 500 :
                current_available_balance += deposit_amount
                print("you have successfully deposited your amount : ",deposit_amount,'\n',"your available balance is : ",current_available_balance)
            
            else: 
                print("please deposit more than 500 Ruppess")
            
        
        else:
            withdrawal_amount = int(input("how much amount you want to withdraw : "))

            if withdrawal_amount < current_available_balance and withdrawal_amount<0 and withdrawal_amount <500 :
                current_available_balance -= withdrawal_amount
                print("you have successfully withdrawal your amount : ",withdrawal_amount,'\n',"your available balance is : ",current_available_balance)
            
            else:
                print("you are trying to withdraw amount that is not withdrawable ")


    else:
        print("Invalid task")

else:
    print("Invalid pin")

























