"""
Bank Account System

Create a BankAccount class with attributes like account_number, balance.

Methods: deposit(), withdraw(), check_balance().

Extend it with SavingsAccount and CurrentAccount classes (inheritance).
"""


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self._balance = balance  # Encapsulation private variable

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"${amount} is deposited,New Balance: ${self._balance}")
        else:
            print("Deposit Unsuccessful")

    def withadraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"${amount}is credited, New Balance: ${self._balance}")
        else:
            print("Invalid withdrawl or Insufficient Funds")

    def check_balance(self):
        print(f"Account Balance: ${self._balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.05):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        print(f"interest of: {interest:.2f} added")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0, over_draft_limit=1000):
        super().__init__(account_number, balance)
        self.over_draft_limit = over_draft_limit

    def withadraw(self, amount):
        if 0 < amount <= self._balance + self.over_draft_limit:
            self._balance -= amount
            print(f"Withdraw ${amount},Remaining Balance: ${self._balance}")
        else:
            print("Limit excceds")


# example of the output
if __name__ == "__main__":
    print("--------Savings Account--------")
    s_acc = SavingsAccount("12345", 10000)
    s_acc.deposit(500)
    s_acc.withadraw(1000)
    s_acc.check_balance()

    print("---------Current Account---------")
    c_acc = CurrentAccount("5678", 1000, over_draft_limit=2000)
    c_acc.withadraw(2500)
    c_acc.check_balance()
    c_acc.withadraw(200)  # exceeds overdraft limit
