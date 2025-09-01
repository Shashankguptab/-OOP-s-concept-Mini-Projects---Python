"""
ATM Machine Simulation

Class: ATM connected with BankAccount.

Options: Withdraw, Deposit, Balance Inquiry.

Implements encapsulation for balance security.
"""


class BankAccount:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self._balance = balance  # encapsulation

    def deposit(self, amount):
        self._balance += amount
        return f"Deposited {amount} .New Balance is {self._balance}"

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return f"Withdrawn {amount} . Remaining Balance is {self._balance}"
        return "Insufficient Funds"

    def check_balance(self):
        return f"Balance is{self._balance}"


class ATM:
    def __init__(self, account):
        self.account = account

    def menu(self):
        while True:
            print("\n ATM menu")
            print("\n 1.Deposit\n 2.Withdraw\n 3.Balance Inquiry\n 4.Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                amount = float(input("Enter the amount to deposit: "))
                print(self.account.deposit(amount))

            elif choice == "2":
                amount = float(input("Enter the the amount to withdraw: "))
                print(self.account.withdraw(amount))
            elif choice == "3":
                print(self.account.check_balance())
            elif choice == "4":
                print("Thanks for visiting")
                break
            else:
                print("Invalid option!!")


acc = BankAccount("4567", 10000)
atm = ATM(acc)
atm.menu()
