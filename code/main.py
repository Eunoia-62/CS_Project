from data_storage import accounts
from account_management import create_new_account, login, switch_account
from account_operations import account_options_menu
import loan_operations

def show_account_info(acc_address):
    """Display account information"""
    account = accounts[acc_address]
    print("\n" + "="*50)
    print("ACCOUNT INFORMATION")
    print("="*50)
    print("Name: " + account['name'])
    print("Branch ID: " + account['branch_id'])
    print("Account Address: " + acc_address)
    print("Balance: $" + str(account['balance']))
    print("Loan State: " + account['loan_state'])
    print("="*50)

def main_menu_after_login(acc_address):
    """Main menu after successful login"""
    while True:
        show_account_info(acc_address)
        print("\n" + "-"*50)
        print("MAIN MENU")
        print("-"*50)
        print("1. Account Options")
        print("2. Loan Options")
        print("3. Switch Account")
        print("4. Logout")
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == '1':
            account_options_menu(acc_address)
        elif choice == '2':
            loan_operations.loan_options_menu(acc_address)
        elif choice == '3':
            acc_address = switch_account(acc_address)
        elif choice == '4':
            print("\nLogging out... Thank you for using our banking system!")
            input("Press Enter to continue...")
            break
        else:
            print("Invalid choice!")

def main():
    """Main program loop"""
    print("="*50)
    print("WELCOME TO THE BANKING SYSTEM")
    print("="*50)
    
    while True:
        print("\n" + "-"*50)
        print("MAIN SCREEN")
        print("-"*50)
        print("1. Login")
        print("2. Create New Account")
        print("3. Exit")
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == '1':
            acc_address = login()
            if acc_address:
                main_menu_after_login(acc_address)
        
        elif choice == '2':
            create_new_account()
        
        elif choice == '3':
            print("\nThank you for using our banking system. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()