class SavingsAccount(BankAccount):
    
    # Constructor
    def __init__(self,name=str,bal=int,minbal=int,rate=float):
        BankAccount.__init__(self,name,bal)
        self.interest_rate = rate

    # Methods
    def calculate_interest(days=int):
        self.current_balance += (self.interest_rate*0.01)*days