import BankAccount
import random

# Testing the Checking Account

#1.A: User opens a checking account, and makes a deposit successfully
print("---------------------")
jane = BankAccount.CheckingAccount("Jane",50,50,25) 
jane.print_customer_information()
print("---------------------")
jane.deposit(20)
jane.print_customer_information()


#1.B: User opens a checking account, and makes a deposit unsuccessfully
print("---------------------")
mark = BankAccount.CheckingAccount("Mark",50,50,25)
mark.print_customer_information()
print("---------------------")
mark.deposit(30)
mark.print_customer_information()


#Testing the Savings Account
#2.A: User opens a savings account, and lets interest accrue for 2 years at 1.05 interest
print("---------------------")
alex = BankAccount.SavingsAccount("Alex",50,50,1.05)
alex.print_customer_information()
print("---------------------")
print(f"${alex.calculate_interest(2)} Interest Accrued")
alex.print_customer_information()


#2.B: User opens a savings account, and lets interest accrue for 3.5 years at 1.07 interest
print("---------------------")
jack = BankAccount.SavingsAccount("Jack",50,50,1.07)
jack.print_customer_information()
print("---------------------")
print(f"${jack.calculate_interest(3.5)} Interest Accrued")
jack.print_customer_information()