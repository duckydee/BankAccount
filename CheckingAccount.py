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
    def deposit(self,amt):
        if amt > self.transfer_limit:
            self.current_balance += amt
        else:
            print("Transfer exceeds account limit.")
            