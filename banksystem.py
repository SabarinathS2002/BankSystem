# Define a class named BankAccount to represent a bank account
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  # Store the owner's name
        self.balance = balance  # Initialize the balance with the provided value

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # Add the amount to the balance
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount  # Subtract the amount from the balance
                print(f"Withdrawn: ${amount}")
            else:
                print("Insufficient funds!")  # Error message for insufficient balance
        else:
            print("Withdrawal amount must be positive!")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")


# Main function to simulate the bank operations
def main():
    print("Welcome to Bank Operation System")

    # Creating an account with the owner's name and an optional initial balance
    name = input("Enter your name to create an account: ")
    account = BankAccount(owner=name)

    # Menu loop to perform operations
    while True:
        print("\nChoose an operation:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)  # Call the deposit method
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)  # Call the withdraw method
        elif choice == '3':
            account.check_balance()  # Call the check_balance method
        elif choice == '4':
            print("Thank you for using the Bank Operation System.")
            break  # Exit the loop
        else:
            print("Invalid choice, please try again.")

# Execute the main function
if __name__ == "__main__":
    main()
