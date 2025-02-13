
class BankAccount():

    import random
    # Attributes
    bank_name = "Chase"
    _accountNumber = int(random.random()*100000)+1
    __routingNumber = int(random.random()*100000)+1

    #Constructors
    def __init__(self,name=str,bal=int,minbal=int,):
        self.customer_name = name
        self.current_balance = bal
        self.minimum_balance = minbal

    # Methods
    def deposit(self,amt):
        self.current_balance += amt

    def withdraw(self,amt):
        if self.check_bal(amt): self.current_balance -= amt
        else: print("Balance has been overdrawn.")

    def print_customer_information(self):
        print (f"{self.bank_name} Bank Records\nCustomer: {self.customer_name} \nBalance: {self.current_balance} \nAccount Number: {self._accountNumber}\nRouting Number: {self.__routingNumber}")

    def check_bal(self,amt):
        if self.current_balance - amt >= self.minimum_balance: return True
        return False

class CheckingAccount(BankAccount):
    # Attributes
    transfer_limit = None

    # Constructor
    def __init__(self,name=str,bal=int,minbal=int,limit=int):
        self.customer_name = name
        self.current_balance = bal
        self.minimum_balance = minbal
        self.transfer_limit = limit

    # Methods
    def deposit(self,amt=int):
        if amt <= self.transfer_limit :
            self.current_balance += amt
        else:
            print("Transfer woukd exceed account limit.")

    def withdraw(self,amt):
        if BankAccount.check_bal(amt) and amt <= self.transfer_limit: self.current_balance -= amt
        else: print("Balance has been overdrawn.")
            

class SavingsAccount(BankAccount):
    # Attributes
    interest_rate = None
    
    # Constructor
    def __init__(self,name=str,bal=int,minbal=int,rate=float):
        self.customer_name = name
        self.current_balance = bal
        self.minimum_balance = minbal
        self.interest_rate = rate

    # Methods
    def calculate_interest(self,years=float):
        interest = int(100*(self.current_balance * (1 + (self.interest_rate/(1+(years))))))
        interest = float(interest/100)
        self.current_balance += interest        
        return interest