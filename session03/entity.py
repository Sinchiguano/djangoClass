from datetime import datetime


class BankAccountBase:
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


class BankAccountSimple(BankAccountBase):
    
    def __init__(self,account_number, account_type, account_name, account_name_id, currency, balance=0.0,ruc=''):   
        super().__init__(account_number, account_type, account_name,account_name_id, currency, balance=0.0)
        self.ruc=ruc
        print(f'Bank account for {self.account_name} with account_number {self.account_number} created successfully!!!')

    
    
    def add_money(self, amount):
        if amount > 0:
            adding_money=0.01
            self.balance += amount
            print('adding extra money for saving')
            self.balance += adding_money
            self.movements_time
            self.movements.append(f"Deposit: +{amount} {self.currency},Time: {self.movements_time}")
            self.movements.append(f"Adding money for saving money: +{adding_money} {self.currency},Time: {self.movements_time}")
            return True
        return False

    def withdraw_money(self, amount):
        if amount > 0 and self.balance >= amount:

            tmp=0.50
            self.balance -= amount
            self.movements.append(f"Withdrawal: -{amount} {self.currency},Time: {self.movements_time}")
            
            
            print('charging money for withdraw money')
            self.balance -= tmp
            self.movements.append(f"Charging for Withdrawal: -{tmp} {self.currency},Time: {self.movements_time}")
            
            return True
        return False


class BankAccountBusiness(BankAccountBase):
   def add_money(self, amount):
        if amount > 0:
            adding_money=0.02
            self.balance += amount
            print('adding extra money for saving')
            self.balance += adding_money
            self.movements_time
            self.movements.append(f"Deposit: +{amount} {self.currency},Time: {self.movements_time}")
            self.movements.append(f"Adding money for saving money: +{adding_money} {self.currency},Time: {self.movements_time}")
            return True
        return False
   def withdraw_money(self, amount):
        if amount > 0 and self.balance >= amount:
            tmp=0.75
            self.balance -= amount
            self.movements.append(f"Withdrawal: -{amount} {self.currency},Time: {self.movements_time}")
            
            
            print('charging money for withdraw money')
            self.balance -= tmp
            self.movements.append(f"Charging for Withdrawal: -{tmp} {self.currency},Time: {self.movements_time}")
            
            return True
        return False

