
import time 
from datetime import datetime



class BankAccount:
    def __init__(self, account_number, account_type, account_name,account_name_id, currency, balance=0.0):
        
        self.account_number = account_number
        self.account_type = account_type
        self.account_name = account_name
        self.account_name_id = account_name_id
        self.currency = currency
        self.balance = balance
        self.movements = []
        self.movements_time = datetime.now()
        print(f'Bank account for {self.account_name} with account_number {self.account_number} created successfully!!!')

    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            self.movements_time
            self.movements.append(f"Deposit: +{amount} {self.currency},Time: {self.movements_time}")
            return True
        return False

    def withdraw_money(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.movements.append(f"Withdrawal: -{amount} {self.currency},Time: {self.movements_time}")
            return True
        return False

    def show_movements(self):
        print(f"\nAccount Movements for {self.account_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance} {self.currency}")
        print("\nTransaction History:")
        for movement in self.movements:
            print(movement)



# Create bank account instance with the provided information
cesar_sinchiguano = BankAccount(account_number=1,
                                account_type='saving',
                                account_name='Cesar Sinchiguano',
                                account_name_id='1111',
                                currency='dollars',
                                balance=0.00)

# Create bank account instance with the provided information
juan_chiriboga  = BankAccount(account_number=2,
                                account_type='saving',
                                account_name='Juan Chiriboga',
                                account_name_id='2222',
                                currency='dollars',
                                balance=0.00)

print('--------------------------------')
# TRANSACTIONS

cesar_sinchiguano.add_money(120)
juan_chiriboga.add_money(350)

# MOVEMENTS 

# print(cesar_sinchiguano.movements)
print(juan_chiriboga.show_movements())


print('--------------------------------')

# TRANSACTIONS

cesar_sinchiguano.add_money(10)
juan_chiriboga.add_money(30)

# MOVEMENTS 

# print(cesar_sinchiguano.movements)
print(cesar_sinchiguano.show_movements())


print('--------------------------------')
# TRANSACTIONS

cesar_sinchiguano.add_money(18)
juan_chiriboga.add_money(35)

# MOVEMENTS 

# print(cesar_sinchiguano.movements)
print(juan_chiriboga.show_movements())

print('--------------------------------')
# TRANSACTIONS

cesar_sinchiguano.withdraw_money(36)
# juan_chiriboga.add_money(35)

# MOVEMENTS 

# print(cesar_sinchiguano.movements)
cesar_sinchiguano.show_movements()
