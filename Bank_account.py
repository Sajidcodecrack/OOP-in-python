class account:
    def __init__(self, acc, bal):
        self.account_no = acc
        self.balance = bal
        # debit method

    def debit(self, amount):
        self.balance -= amount
        print("$ ", amount, " is debited from your account no ", self.account_no)
        print("Total balance is now : $", self.get_balance())
        # credit method

    def credit(self, amount):
        self.balance += amount
        print("$", amount, " is credited to your account no ", self.account_no)
        print("Total balance is now :$", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = account("1413259741", 25000)
print("Your account number : ", acc1.account_no)
print("Your account balance is : ", acc1.balance)
acc1.debit(535.75)
acc1.credit(30000.25)
