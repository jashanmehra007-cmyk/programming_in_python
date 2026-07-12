# Task: Simple Bank Account System

# Requirements:

# Create a class BankAccount
# Add:
# account_holder
# balance
# Create methods:
# deposit(amount)
# withdraw(amount)
# display_balance()
# Rules:
# Cannot deposit a negative amount.
# Cannot withdraw more than the available balance.
# Use try and except for invalid input.
# Create one account and show a menu:
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit

class BankAccount:
    def __init__(self, account_holder, balance):
        self.acc = account_holder
        self.bal = balance
     
    def deposit(self,amount):
       if amount <= 0:
            print('Enter a valid amount')
            return
       self.bal += amount
       print(f"{amount} deposited successfully.")

    def withdraw(self,amount):
        if amount <= 0:
            print('Enter a valid amount')
            return

        if amount > self.bal:
            print('Insufficient Balance!!')
            return 
        self.bal -= amount
        print(f"{amount} withdrawn successfully.")

    def display_balance(self):
        print(f"Current Balance: {self.bal}")

# create Account
account = BankAccount('jashan',1000)

while True:
    print('\n ---Bank Menu---')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Check Balance')
    print('4. Exit')

    choice = input('Enter your choice: ')

    if choice == "1":
        try:
            amount = float(input('Enter deposit amount: '))
            account.deposit(amount)
        except ValueError:
            print('Please enter a valid number!!')
    elif choice == "2":
        try:
            amount = float(input("Enter Withdraw amount: "))
            account.withdraw(amount)
        except ValueError:
            print("Please enter a valid number! ")
    elif choice == "3":
        account.display_balance()

    elif choice == "4":
        print("Thank you for using the bank system")
        break
    else:
        print("Invalid choice. Please try again.")
