# Code 3: Basic Banking System

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. Remaining balance: ${self.balance}"
        return "Insufficient funds or invalid amount."

    def check_balance(self):
        return f"Account holder: {self.owner}. Current balance: ${self.balance}"
if __name__ == "__main__":
    account = BankAccount("Alice", 1000)
    print(account.deposit(500))
    print(account.withdraw(300))
    print(account.check_balance())