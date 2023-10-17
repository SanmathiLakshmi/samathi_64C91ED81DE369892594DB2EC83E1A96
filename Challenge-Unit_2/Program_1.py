class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        elif amount > self.__account_balance:
            print("Insufficient funds. Withdrawal not allowed.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")

    def display_balance(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Balance: ${self.__account_balance}")

# Test the BankAccount class
if __name__ == "__main__":
    # Create a BankAccount instance
    my_account = BankAccount("123456789", "John Doe", 1000.0)

    # Display initial balance
    my_account.display_balance()

    # Make a deposit
    my_account.deposit(500.0)

    # Make a withdrawal
    my_account.withdraw(200.0)

    # Try an invalid withdrawal
    my_account.withdraw(1500.0)
