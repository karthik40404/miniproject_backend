import random
import os

def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def save_account(account_details):
    file_name = f"miniproject_backend/bank2/{account_details['account_number']}.txt"
    ensure_directory_exists(os.path.dirname(file_name))
    with open(file_name, 'w') as file:
        for key, value in account_details.items():
            file.write(f"{key}: {value}\n")

def load_account(account_number):
    file_name = f"miniproject_backend/bank2/{account_number}.txt"
    if not os.path.exists(file_name):
        return None
    
    account_details = {}
    with open(file_name, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ')
            account_details[key] = value
    
    return account_details

def update_balance(account_number, new_balance):
    account_details = load_account(account_number)
    if account_details:
        account_details['balance'] = str(new_balance)
        save_account(account_details)

def main_menu():
    while True:
        print('\n1. Create account\n2. Login\n3. Exit')
        try:
            ch = int(input('Enter your choice: '))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if ch == 1:
            create_account()
        elif ch == 2:
            login()
        elif ch == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def create_account():
    name = input('Enter your name: ')
    
    while True:
        try:
            ph = int(input('Enter your phone number: '))
            break
        except ValueError:
            print("Invalid phone number. Please enter a valid number.")

    while True:
        try:
            password = int(input('Enter your pin: '))
            break
        except ValueError:
            print("Invalid pin. Please enter a valid number.")

    while True:
        try:
            balance = int(input('Deposit: '))
            break
        except ValueError:
            print("Invalid deposit amount. Please enter a valid number.")

    account_number = random.randint(10000, 99999)
    
    account_details = {
        'name': name,
        'phone': str(ph),
        'password': str(password),  
        'balance': str(balance),
        'account_number': str(account_number)
    }
    
    save_account(account_details)
    
    print(f"Account has been created successfully! Your account number is: {account_number}")

def login():
    acc_num = input('Enter your account number: ')
    password = input('Enter your pin: ')
    
    account_details = load_account(acc_num)
    
    if account_details:
        if account_details['password'] == password:
            print(f"Login successful! Welcome, {account_details['name']}.")
            account_operations(acc_num, account_details)
        else:
            print("Invalid pin.")
    else:
        print("Account not found. Please check the account number.")

def account_operations(acc_num, account_details):
    while True:
        print('\n1. Deposit\n2. Withdraw\n3. Display Balance\n4. Logout')
        try:
            option = int(input('Enter your choice: '))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if option == 1:  
            deposit(acc_num, account_details)
        elif option == 2:  
            withdraw(acc_num, account_details)
        elif option == 3: 
            display_balance(account_details)
        elif option == 4:  
            print("Logging out...")
            break                  
        else:
            print("Invalid option")

def deposit(acc_num, account_details):
    try:
        amount = int(input('Enter amount to deposit: '))
        new_balance = int(account_details['balance']) + amount
        update_balance(acc_num, new_balance)
        account_details['balance'] = str(new_balance) 
        print(f"Amount deposited successfully! New balance is: {new_balance}")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")

def withdraw(acc_num, account_details):
    try:
        amount = int(input('Enter amount to withdraw: '))
        current_balance = int(account_details['balance'])
        if amount <= current_balance:
            new_balance = current_balance - amount
            update_balance(acc_num, new_balance)
            account_details['balance'] = str(new_balance) 
            print(f"Amount withdrawn successfully! New balance is: {new_balance}")
        else:
            print("Insufficient balance.")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")

def display_balance(account_details):
    print(f"Your current balance is: {account_details['balance']}")


main_menu()
