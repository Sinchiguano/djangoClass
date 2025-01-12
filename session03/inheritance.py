from entity import BankAccountSimple, BankAccountBusiness, BankAccountBase


# Create bank account instance with the provided information
mario_velez  = BankAccountSimple(account_number=3,
                                account_type='saving',
                                account_name='Mario Velez',
                                account_name_id='3333',
                                currency='dollars',
                                balance=10.00)


# Create bank account instance with the provided information
pepe_zambrano  = BankAccountBusiness(account_number=4,
                                account_type='saving',
                                account_name='Pepe Zambrano',
                                account_name_id='3333',
                                currency='dollars',
                                balance=20.00)


# Create bank account instance with the provided information
sandra_garcia  = BankAccountSimple(account_number=4,
                                account_type='saving',
                                account_name='Pepe Zambrano',
                                account_name_id='3333',
                                currency='dollars',
                                balance=20.00,
                                ruc=99999)


mario_velez.add_money(10)
mario_velez.show_movements()
print(f'the ruc of sandra garcia {sandra_garcia.ruc}')