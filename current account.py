class Account:
    accountName = "victorAOC"
    accountBalance = 40000
    accountNumber = 8039886850
    def __init__(self):
        self.accountBalance
        self.accountName
        self.accountNumber  
    def deposit(self, amount):
        self.accountBalance = self.accountBalance + amount
        return f"Your new ammount is {self.accountBalance}"
    def withdraw(self, amount):
        self.accountBalance = self.accountBalance - amount
        return f"Your current account balance is now {self.accountBalance}"