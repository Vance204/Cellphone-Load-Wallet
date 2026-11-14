
class LoadWallet:
    def __init__(self, owner_name, mobile_number, balance):
        self.owner_name = owner_name
        self.mobile_number = mobile_number
        self.__balance = balance

    def top_up(self, amount):
        if amount <= 0:
            print("Invalid top-up amount.")
        else:
            self.__balance += amount
            print(f"New balance: P{self.__balance:.2f}")

    def send_load(self, recipient_number, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif recipient_number[:4] != self.mobile_number[:4]:
            print("Recipient must be on the same network.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Successfully sent P{amount:.2f} to {recipient_number}.")
            print(f"Remaining balance: P{self.__balance:.2f}")

    def send_with_fee(self, recipient_number, amount, fee):
        if amount <= 0 or fee < 0:
            print("Invalid amount or service fee.")
        elif recipient_number[:4] == self.mobile_number[:4]:
            print("Recipient is on the same network.")
        elif amount + fee > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount + fee
            print(f"Successfully sent P{amount:.2f} to {recipient_number}.")
            print(f"Service fee: P{fee:.2f}")
            print(f"Remaining balance: P{self.__balance:.2f}")

    def show_balance(self):
        print(f"Owner         : {self.owner_name}")
        print(f"Mobile Number : {self.mobile_number}")
        print(f"Balance       : P{self.__balance:.2f}")
