class User:
    def __init__(self, user_id, pin, balance=1000):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid amount. Please enter a positive number."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Invalid amount. Please enter a positive number."

    def transfer(self, recipient, amount):
        if recipient and amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to user {recipient.user_id}")
            recipient.transaction_history.append(f"Received ${amount} from user {self.user_id}")
            return f"Transferred ${amount} to user {recipient.user_id}. New balance: ${self.balance}"
        elif not recipient:
            return "Invalid recipient."
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Invalid amount. Please enter a positive number."

class ATMSystem:
    def __init__(self):
        self.users = {}  # A dictionary to store users (user_id as keys, User objects as values)
        self.current_user = None

    def create_user(self, user_id, pin):
        if user_id not in self.users:
            new_user = User(user_id, pin)
            self.users[user_id] = new_user
            return f"User {user_id} created successfully."
        else:
            return f"User {user_id} already exists."

    def login(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            self.current_user = self.users[user_id]
            return f"Welcome, user {user_id}."
        else:
            return "Invalid user ID or PIN. Please try again."

    def logout(self):
        self.current_user = None
        return "Logged out successfully."

    def display_transaction_history(self):
        if self.current_user:
            return self.current_user.transaction_history
        else:
            return "Please log in to view transaction history."


def main():
    atm_system = ATMSystem()

    while True:
        print("Welcome to the ATM System")
        print("1. Create User")
        print("2. Login")
        print("3. Logout")
        print("4. Check Balance")
        print("5. Deposit")
        print("6. Withdraw")
        print("7. Transfer")
        print("8. Transaction History")
        print("9. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")

        if choice == '1':
            user_id = input("Enter user ID: ")
            pin = input("Enter PIN: ")
            print(atm_system.create_user(user_id, pin))
        elif choice == '2':
            user_id = input("Enter user ID: ")
            pin = input("Enter PIN: ")
            print(atm_system.login(user_id, pin))
        elif choice == '3':
            print(atm_system.logout())
        elif choice == '4':
            if atm_system.current_user:
                print(f"Your balance is: ${atm_system.current_user.check_balance()}")
            else:
                print("Please log in to check your balance.")
        elif choice == '5':
            if atm_system.current_user:
                amount = float(input("Enter the deposit amount: $"))
                print(atm_system.current_user.deposit(amount))
            else:
                print("Please log in to make a deposit.")
        elif choice == '6':
            if atm_system.current_user:
                amount = float(input("Enter the withdrawal amount: $"))
                print(atm_system.current_user.withdraw(amount))
            else:
                print("Please log in to make a withdrawal.")
        elif choice == '7':
            if atm_system.current_user:
                recipient_id = input("Enter recipient's user ID: ")
                amount = float(input("Enter the transfer amount: $"))
                recipient = atm_system.users.get(recipient_id)
                print(atm_system.current_user.transfer(recipient, amount))
            else:
                print("Please log in to make a transfer.")
        elif choice == '8':
            if atm_system.current_user:
                transactions = atm_system.display_transaction_history()
                for transaction in transactions:
                    print(transaction)
            else:
                print("Please log in to view transaction history.")
        elif choice == '9':
            print("Thank you for using the ATM System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
