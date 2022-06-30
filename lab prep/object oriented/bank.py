class BankAcc:
    def __init__(self):
        self.balance=0

    def deposit(self,amount):
        self.balance+=amount
        return self.balance

    def withdraw(self,amount):
        self.balance-=amount
        return self.balance

a=BankAcc()
b=BankAcc()
print(a.deposit(100))
print(b.deposit(50))

