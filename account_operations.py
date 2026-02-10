from data_storage import accounts

def deposit(acc_address):
    """Handle deposit operation"""
    try:
        amount = float(input("\nEnter deposit amount: $"))
        if amount <= 0:
            print("Amount must be greater than zero!")
            return
        
        accounts[acc_address]['balance'] += amount
        print("\nDeposited $" + str(amount))
        print("New balance: $" + str(accounts[acc_address]['balance']))
    except ValueError:
        print("Invalid amount!")

def withdraw(acc_address):
    """Handle withdrawal operation"""
    try:
        amount = float(input("\nEnter withdrawal amount: $"))
        if amount <= 0:
            print("Amount must be greater than zero!")
            return
        
        if accounts[acc_address]['balance'] >= amount:
            accounts[acc_address]['balance'] -= amount
            print("\nWithdrew $" + str(amount))
            print("New balance: $" + str(accounts[acc_address]['balance']))
        else:
            print("\nInsufficient balance!")
    except ValueError:
        print("Invalid amount!")

def check_balance(acc_address):
    """Display current balance"""
    print("\nCurrent balance: $" + str(accounts[acc_address]['balance']))

def transfer(acc_address):
    """Handle transfer operation"""
    print("\nTransfer feature coming soon!")

def account_options_menu(acc_address):
    """Display and handle account options"""
    while True:
        print("\n" + "-"*50)
        print("ACCOUNT OPTIONS")
        print("-"*50)
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transfer")
        print("5. Back to Menu")
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == '1':
            deposit(acc_address)
        elif choice == '2':
            withdraw(acc_address)
        elif choice == '3':
            check_balance(acc_address)
        elif choice == '4':
            transfer(acc_address)
        elif choice == '5':
            break
        else:
            print("Invalid choice!")