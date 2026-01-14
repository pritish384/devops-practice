import uuid

class BankAccount:
    def __init__(self, name):
        self.account_number = uuid.uuid4()
        self.name = name
        self.balance = 0

    def display_information(self):
        return f"{self.name} has {self.account_number} with ₹{self.balance}"

    def withdraw(self,amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"₹ {amount} has been withdrawn. New balance is ₹ {self.balance}"
    
    def deposit(self,amount):
        self.balance += amount
        return f"₹ {amount} has been deposited. New balance is ₹ {self.balance}"
    
    def pay(self,amount,receiver_account):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        receiver_account.balance += amount
        return f"₹ {amount} has been paid to {receiver_account.name}. New balance is ₹ {self.balance}"
    


if __name__ == "__main__":
    while True:
        name = input("Enter account holder name: ")
        account = BankAccount(name)
        print(f"Account created for {name} with account number {account.account_number}")
        
        while True:
            action = input("Choose action: 1) Deposit 2) Withdraw 3) Display Info 4) Exit: ")
            if action == '1':
                amount = float(input("Enter amount to deposit: "))
                print(account.deposit(amount))
            elif action == '2':
                amount = float(input("Enter amount to withdraw: "))
                print(account.withdraw(amount))
            elif action == '3':
                print(account.display_information())
            elif action == '4':
                print("Exiting...")
                break
            else:
                print("Invalid action. Please try again.")
        
        another = input("Do you want to create another account? (yes/no): ")

        if another.lower() != 'yes':
            break

       


    print("Thank you for using the banking system.")
