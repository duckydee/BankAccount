class SavingsAccount(BankAccount):
    
    def __init__(self,name=str,bal=int,minbal=int,rate=float):
        self.customer_name = name
        self.current_balance = bal
        self.minimum_balance = minbal
        self.interest_rate = rate

    def calculate_interest(days=int):
        self.current_balance += (self.interest_rate*0.01)*days





