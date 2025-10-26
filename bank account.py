class BankAccount:
    def __init__(self, acc_number, customer_name, balance, date_of_opening):
        self.acc_number = acc_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening

    
    def deposit(self, amount):
        self.balance += amount
        print(f"deposit: {amount}")
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient balance!")
        else:
            self.balance -= amount
            print(f"withdraw: {amount}")
        return self.balance
    
    def check_balance(self):
        print(f"current amount: {self.balance}")
        return self.balance
    
    def customer_details(self):
        print("Customer_details:")
        print(f"Name: {self.customer_name}")
        print(f"Acc_number: {self.acc_number}")
        print(f"Date of opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")


acc = BankAccount("123456789", "Elsy Mwangi", 5000, "24-10-2025")

acc.customer_details()
acc.deposit(1500)
acc.withdraw(2000)
acc.check_balance()
