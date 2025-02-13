class CheckingAccount(BankAccount):
    # Attributes
    transfer_limit = 0

    # Constructor
    def __init__(self,name=str,bal=int,minbal=int,limit=int):
        BankAccount.__init__(self,name,bal)
        self.transfer_limit = limit

    # Methods
    def deposit(self,amt):
        if amt > self.transfer_limit:
            self.current_balance += amt
        else:
            print("Transfer exceeds account limit.")
            