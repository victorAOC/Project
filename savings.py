from account import Account


class Savings(Account):
    def __init__(self):
        super().__init__()

    def withdraw(self, amount):
        if amount > 5000:
            return "you don reach your daily limit"
        else:
            return super().withdraw(amount)


savings = Savings()
print(savings.withdraw(2000))
