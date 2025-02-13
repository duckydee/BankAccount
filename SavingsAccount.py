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
    def calculate_interest(days=int):
        BankAccount.current_balance += * (1 + (self.interest_rate/(1+(days/365))))