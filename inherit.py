class bank:
    def __init__(self):
        self.acct_no = 122334455
        self.fName = "Daniel"
        self.lName = "Fori"
        self.balance = 10000
        self.amount = 0

    def check_balance(self):
        print(self.balance)

    def deposite(self, amount):
        self.amount = amount
        self.balance += self.amount

    def withdraw(self, amount):
        self.amount = amount
        self.balance -= self.amount


class savings(bank):
    def withdraw(self, amount):
        if amount > 5000:
            print("limit exceeded")
        else:
            self.amount = amount
            self.balance -= self.amount


    def deposite(self, amount):
            if amount >= 5000:
                print("limit exceeded")
            else:
                self.amount = amount
                self.balance += self.amount
                print(self.balance)

class current(bank):
    pass


me = savings()
me.deposite(9000)
me.check_balance()

you = current()
you.deposite(8000)
you.check_balance()
print(you.fName)