class Checkbook:
    def __init__(self):
        """
        Initialize a Checkbook object with a zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the checkbook.

        Parameters:
        - amount (float): The amount of money to deposit.
        """
        try:
            amount = float(amount)  # Convert input to float
            if amount <= 0:
                print("Invalid amount. Please enter a positive number.")
            else:
                self.balance += amount
                print("Deposited ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def withdraw(self, amount):
        """
        Withdraw money from the checkbook.

        Parameters:
        - amount (float): The amount of money to withdraw.
        """
        try:
            amount = float(amount)  # Convert input to float
            if amount <= 0:
                print("Invalid amount. Please enter a positive number.")
            elif amount > self.balance:
                print("Insufficient funds to complete the withdrawal.")
            else:
                self.balance -= amount
                print("Withdrew ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def get_balance(self):
        """
        Print the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            amount = input("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = input("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
