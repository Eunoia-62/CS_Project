import random
import time
from data_storage import accounts, login_attempts, locked_accounts
from validation import validate_date, validate_home_address, validate_phone, validate_password

def generate_account_address():
    """Generate a random 6-digit account address"""
    return str(random.randint(100000, 999999))

def find_matching_account(name, dob, home_address, phone_no, gender):
    """Find if an account with same personal details exists"""
    for acc_addr, account in accounts.items():
        if (account['name'] == name and 
            account['dob'] == dob and 
            account['home_address'] == home_address and 
            account['phone_no'] == phone_no and 
            account['gender'] == gender):
            return acc_addr, account['special_code']
    return None, None

def create_new_account():
    """Handle new account creation with validation and account linking"""
    print("\n" + "="*50)
    print("NEW ACCOUNT CREATION")
    print("="*50)
    
    # Get and validate name
    name = input("\nEnter your name: ").strip()
    name = name.capitalize()
    
    # Get and validate date of birth
    while True:
        dob = input("Enter your date of birth (DD/MM/YYYY): ").strip()
        if validate_date(dob):
            break
        else:
            print("Invalid date format! Please enter in DD/MM/YYYY format.")
    
    # Get and validate home address
    while True:
        home_address = input("Enter your home address: ").strip()
        if validate_home_address(home_address):
            break
        else:
            print("Invalid address!")
    
    # Get country for phone validation
    print("\nEnter your country (for phone validation):")
    country = input("Country: ").strip()
    
    # Get and validate phone number
    while True:
        phone_no = input("Enter your phone number: ").strip()
        if validate_phone(phone_no):
            break
        else:
            print("Invalid phone number!")
    
    # Get and validate gender
    while True:
        print("\nSelect your gender:")
        print("1. Male")
        print("2. Female")
        gender_choice = input("Enter choice (1 or 2): ").strip()
        
        if gender_choice == '1':
            gender = 'Male'
            break
        elif gender_choice == '2':
            gender = 'Female'
            break
        else:
            print("Invalid choice! Please select 1 or 2.")
    
    # Get and validate password
    while True:
        password = input("\nEnter your password (min 8 characters, must contain numbers and alphabets): ").strip()
        if validate_password(password):
            break
        else:
            print("Invalid password! Must be at least 8 characters with both numbers and alphabets.")
    
    # Confirm password
    while True:
        confirm_password = input("Re-enter your password: ").strip()
        if confirm_password == password:
            break
        else:
            print("Passwords don't match! Please re-enter.")
    
    # Check if account with same details exists (for linking)
    existing_acc_addr, existing_special_code = find_matching_account(name, dob, home_address, phone_no, gender)
    
    special_code = None
    
    if existing_acc_addr:
        print("\n" + "-"*50)
        print("An account with matching personal details was found!")
        print("Would you like to link this new account?")
        link_choice = input("Enter 'yes' to link or 'no' to create independent account: ").strip().lower()
        
        if link_choice == 'yes':
            attempts = 3
            linked = False
            
            while attempts > 0:
                entered_code = input("\nEnter your special code to link accounts (" + str(attempts) + " attempts remaining): ").strip()
                
                if entered_code == existing_special_code:
                    special_code = existing_special_code
                    print("\nAccounts linked successfully!")
                    linked = True
                    break
                else:
                    attempts -= 1
                    if attempts > 0:
                        print("Incorrect special code! " + str(attempts) + " attempt(s) remaining.")
            
            if not linked:
                print("\nToo many incorrect attempts!")
                print("Please visit the nearest branch to resolve this issue.")
                input("\nPress Enter to return to main menu...")
                return
    
    # Generate new special code if not linked
    if special_code is None:
        special_code = str(random.randint(100000, 999999))
    
    # Generate unique account address
    acc_address = generate_account_address()
    while acc_address in accounts:
        acc_address = generate_account_address()
    
    # Store account information
    accounts[acc_address] = {
        'name': name,
        'dob': dob,
        'home_address': home_address,
        'phone_no': phone_no,
        'password': password,
        'gender': gender,
        'country': country,
        'special_code': special_code,
        'branch_id': 'BR' + str(random.randint(1000, 9999)),
        'balance': 0.0,
        'loan_state': 'None'
    }
    
    print("\n" + "="*50)
    print("ACCOUNT CREATED SUCCESSFULLY!")
    print("="*50)
    print("Your Special Code: " + special_code)
    print("Your Account Address: " + acc_address)
    print("\nIMPORTANT: Please save these details securely.")
    print("You will need them for future logins.")
    print("="*50)
    
    input("\nPress Enter to return to main menu...")

def check_account_locked(acc_address):
    """Check if account is locked and return lock status"""
    if acc_address in locked_accounts:
        lock_time = locked_accounts[acc_address]
        elapsed = time.time() - lock_time
        
        if elapsed < 60:  # 1 minute = 60 seconds
            remaining = int(60 - elapsed)
            return True, remaining
        else:
            # Unlock account after 1 minute
            del locked_accounts[acc_address]
            if acc_address in login_attempts:
                del login_attempts[acc_address]
    
    return False, 0

def display_lockout_countdown(acc_address):
    """Display dynamic countdown for locked account"""
    print("\n" + "="*50)
    print("TOO MANY WRONG ATTEMPTS!")
    print("="*50)
    
    while True:
        is_locked, remaining = check_account_locked(acc_address)
        
        if not is_locked:
            print("\nAccount unlocked! You may try again.")
            input("Press Enter to continue...")
            break
        
        print("\rUser locked out of system. Time remaining: " + str(remaining) + " seconds  ", end='')
        time.sleep(1)

def login():
    """Handle login process with validation"""
    print("\n" + "="*50)
    print("LOGIN")
    print("="*50)
    
    name = input("\nEnter your name: ").strip().capitalize()
    special_code = input("Enter your special code: ").strip()
    acc_address = input("Enter your account address: ").strip()
    
    # Check if account exists and details match
    account_found = False
    
    if acc_address in accounts:
        account = accounts[acc_address]
        if account['name'] == name and account['special_code'] == special_code:
            account_found = True
    
    if not account_found:
        print("\nAccount not found or details don't exist!")
        input("Press Enter to continue...")
        return None
    
    # Check if account is locked
    is_locked, remaining = check_account_locked(acc_address)
    if is_locked:
        display_lockout_countdown(acc_address)
        return None
    
    # Initialize login attempts counter
    if acc_address not in login_attempts:
        login_attempts[acc_address] = 3
    
    # Password verification with 3 attempts
    account = accounts[acc_address]
    
    while login_attempts[acc_address] > 0:
        password = input("\nEnter your password (" + str(login_attempts[acc_address]) + " attempts remaining): ").strip()
        
        if account['password'] == password:
            # Successful login - reset attempts
            login_attempts[acc_address] = 3
            print("\nLogin successful!")
            return acc_address
        else:
            login_attempts[acc_address] -= 1
            
            if login_attempts[acc_address] > 0:
                print("Incorrect password! " + str(login_attempts[acc_address]) + " attempt(s) remaining.")
            else:
                # Lock account
                locked_accounts[acc_address] = time.time()
                login_attempts[acc_address] = 3  # Reset for next time
                display_lockout_countdown(acc_address)
                return None
    
    return None

def switch_account(current_acc_address):
    """Allow user to switch to another account with same special code"""
    print("\n" + "="*50)
    print("SWITCH ACCOUNT")
    print("="*50)
    
    current_special_code = accounts[current_acc_address]['special_code']
    
    target_acc_address = input("\nEnter the account address to switch to: ").strip()
    
    # Check if target account exists
    if target_acc_address not in accounts:
        print("Account not found!")
        input("Press Enter to continue...")
        return current_acc_address
    
    # Check if target account has same special code
    if accounts[target_acc_address]['special_code'] != current_special_code:
        print("This account does not belong to you!")
        input("Press Enter to continue...")
        return current_acc_address
    
    # Ask for password of target account
    attempts = 3
    while attempts > 0:
        password = input("\nEnter password for account " + target_acc_address + " (" + str(attempts) + " attempts remaining): ").strip()
        
        if accounts[target_acc_address]['password'] == password:
            print("\nSwitched to account " + target_acc_address + " successfully!")
            input("Press Enter to continue...")
            return target_acc_address
        else:
            attempts -= 1
            if attempts > 0:
                print("Incorrect password! " + str(attempts) + " attempt(s) remaining.")
    
    print("\nToo many incorrect attempts! Returning to current account.")
    input("Press Enter to continue...")
    return current_acc_address