class BankAccount():
    # Attributes
    bank_name = "Chase"
    
    #Constructors
    def __init__(self,name=str,bal=int,minbal=int):
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
        return str((self.bank_name)+" Bank Records\nCustomer: "+str(self.customer_name)+"\nBalance: "+str(self.current_balance)+"\n")

    def check_bal(self,amt):
        if self.current_balance - amt >= self.minimum_balance: return True
        return False