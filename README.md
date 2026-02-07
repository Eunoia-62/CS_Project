# Banking System - Python Project

A comprehensive banking system application built with Python that handles account creation, login, transactions, and loan operations.

---

## Table of Contents
- [Features](#features)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)

---

## Features

✅ **Account Management**
- Create new accounts with validation
- Link multiple accounts under same user
- Secure login with 3-attempt password verification
- Account lockout system (1-minute timeout)
- Switch between linked accounts

✅ **Account Operations**
- Deposit money
- Withdraw money
- Check balance
- Transfer funds (coming soon)

✅ **Loan Operations**
- Apply for loans (coming soon)
- Check loan status
- Repay loans (coming soon)

✅ **Security Features**
- Password validation (minimum 8 characters, must contain numbers and alphabets)
- Special code generation for account identification
- Account linking with verification
- Failed login attempt tracking

---

## File Structure
```
CS Project/
│
├── main.py                      # Main program entry point
├── account_management.py        # Account creation, login, and switching
├── account_operations.py        # Deposit, withdraw, balance operations
├── loan_operations.py           # Loan-related operations
├── validation.py                # Input validation functions
├── data_storage.py              # Global data storage
└── README.md                    # Project documentation
```

---

## Installation

1. **Prerequisites**
   - Python 3.6 or higher installed on your system

2. **Clone or Download**
   - Download all project files to a single folder
---

## Usage

### Creating a New Account
1. Select "Create New Account" from main menu
2. Enter personal details:
   - Name (automatically capitalizes first letter)
   - Date of birth (DD/MM/YYYY format, accepts various separators)
   - Home address (must be >5 characters with alphabets)
   - Country
   - Phone number (7-15 digits based on country)
   - Gender (Male/Female)
   - Password (min 8 chars, must have numbers + alphabets)
3. If matching personal details found, option to link accounts
4. Save your Special Code and Account Address!

### Logging In
1. Select "Login" from main menu
2. Enter:
   - Name
   - Special Code
   - Account Address
3. Enter password (3 attempts)
4. Access your account dashboard

### Switching Accounts
1. From main menu after login, select "Switch Account"
2. Enter target account address
3. Enter password for that account
4. Switch successful!

---

## File Descriptions

### **main.py**
**Purpose:** Main program entry point and flow control

**Key Functions:**
- `main()` - Main program loop, displays main screen menu
- `main_menu_after_login(acc_address)` - Dashboard menu after successful login
- `show_account_info(acc_address)` - Displays account information (name, branch ID, balance, loan state)

**What it does:**
- Handles the main program flow
- Displays main screen with Login/Create Account/Exit options
- After login, shows account dashboard with Account Options, Loan Options, Switch Account, and Logout
- Imports and coordinates all other modules

---

### **account_management.py**
**Purpose:** Handles all account-related operations including creation, login, and switching

**Key Functions:**
- `create_new_account()` - Creates new account with full validation
  - Validates all user inputs
  - Checks for existing accounts with matching details
  - Handles account linking with special code verification (3 attempts)
  - Generates unique 6-digit account address
  - Generates or reuses 6-digit special code
  
- `login()` - Handles user login
  - Verifies name, special code, and account address
  - Checks if account is locked
  - Password verification with 3 attempts
  - Locks account for 1 minute after failed attempts
  
- `switch_account(current_acc_address)` - Allows switching between linked accounts
  - Verifies target account has same special code
  - Requires password authentication
  - Returns new account address on success
  
- `find_matching_account(name, dob, home_address, phone_no, gender)` - Searches for accounts with matching personal details
- `generate_account_address()` - Generates unique 6-digit account number
- `check_account_locked(acc_address)` - Checks if account is in lockout period
- `display_lockout_countdown(acc_address)` - Shows dynamic countdown timer during lockout

**What it does:**
- Manages the entire account lifecycle
- Implements security features (password attempts, lockouts)
- Handles account linking for users with multiple accounts
- Ensures data integrity through validation

---

### **account_operations.py**
**Purpose:** Handles all banking transaction operations

**Key Functions:**
- `deposit(acc_address)` - Handles money deposits
  - Validates amount (must be positive)
  - Updates account balance
  - Shows new balance
  
- `withdraw(acc_address)` - Handles money withdrawals
  - Validates amount
  - Checks sufficient balance
  - Updates account balance
  - Shows new balance
  
- `check_balance(acc_address)` - Displays current account balance

- `transfer(acc_address)` - Transfer funds (coming soon)

- `account_options_menu(acc_address)` - Displays account operations menu
  - Lists all available account operations
  - Handles user choice
  - Includes "Back to Menu" option

**What it does:**
- Manages all financial transactions
- Ensures balance accuracy
- Validates transaction amounts
- Provides user-friendly transaction interface

---

### **loan_operations.py**
**Purpose:** Handles all loan-related operations

**Key Functions:**
- `apply_for_loan(acc_address)` - Loan application (coming soon)
- `check_loan_status(acc_address)` - Displays current loan status
- `repay_loan(acc_address)` - Loan repayment (coming soon)
- `loan_options_menu(acc_address)` - Displays loan operations menu

**What it does:**
- Provides loan management interface
- Currently displays loan status
- Placeholder for future loan features

---

### **validation.py**
**Purpose:** Contains all input validation functions

**Key Functions:**
- `validate_date(date_str)` - Validates date format
  - Accepts DD/MM/YYYY with various separators (/, ., -, etc.)
  - Accepts single-digit day/month (7/2 or 07/02)
  - Checks valid day (1-31), month (1-12), year (1900-2100)
  
- `validate_home_address(address)` - Validates home address
  - Must be >5 characters
  - Must contain alphabets
  - Allows letters, numbers, spaces, hyphens, commas, periods, slashes
  - Rejects special characters like @, #, $, etc.
  
- `validate_phone(phone, min_digits=7, max_digits=15)` - Validates phone number
  - Removes spaces and hyphens
  - Checks digit count (7-15 digits)
  - Ensures only numeric characters
  
- `validate_password(password)` - Validates password strength
  - Minimum 8 characters
  - Must contain at least one number
  - Must contain at least one alphabet

**What it does:**
- Centralizes all validation logic
- Ensures data integrity across the application
- Provides consistent validation rules
- Returns True/False for easy checking

---

### **data_storage.py**
**Purpose:** Global data storage for the application

**Data Structures:**
- `accounts = {}` - Stores all account information
  - Key: Account address (6-digit string)
  - Value: Dictionary containing:
    - `name` - User's name (capitalized)
    - `dob` - Date of birth
    - `home_address` - Home address
    - `phone_no` - Phone number
    - `password` - Account password
    - `gender` - Male/Female
    - `country` - Country name
    - `special_code` - 6-digit special code (shared among linked accounts)
    - `branch_id` - Branch identifier (format: BR####)
    - `balance` - Account balance (float)
    - `loan_state` - Current loan status

- `login_attempts = {}` - Tracks remaining login attempts per account
  - Key: Account address
  - Value: Number of attempts remaining (max 3)

- `locked_accounts = {}` - Tracks locked accounts with timestamp
  - Key: Account address
  - Value: Timestamp when account was locked

**What it does:**
- Provides centralized data storage
- Allows all modules to access and modify account data
- Maintains login security state
- Stores account lockout information

---

## Input Validation Rules

### Name
- Any text input
- Automatically capitalizes first letter

### Date of Birth
- Format: DD/MM/YYYY
- Accepts any separator: `/`, `.`, `-`, `,`
- Single-digit dates accepted (7/2/2000 = 07/02/2000)
- Valid ranges: Day (1-31), Month (1-12), Year (1900-2100)

### Home Address
- Minimum 6 characters
- Must contain at least one alphabet
- Allowed: letters, numbers, spaces, hyphens, commas, periods, slashes
- Not allowed: Special characters (@, #, $, %, etc.)

### Phone Number
- 7-15 digits (based on international standards)
- Spaces and hyphens are automatically removed
- Must contain only numbers

### Gender
- Option 1: Male
- Option 2: Female

### Password
- Minimum 8 characters
- Must contain at least one number
- Must contain at least one alphabet
- Must be re-entered to confirm (both entries must match)

---

## Security Features

1. **Password Protection**
   - Minimum 8 characters with numbers and alphabets
   - Confirmation required during account creation
   - Masked during entry

2. **Login Attempt Limit**
   - Maximum 3 password attempts
   - Account locks for 1 minute after 3 failed attempts
   - Dynamic countdown display during lockout

3. **Account Linking Security**
   - Requires special code verification
   - 3 attempts to enter correct special code
   - Branch visit required after failed attempts

4. **Account Switching**
   - Only allows switching to accounts with same special code
   - Password required for target account
   - 3 attempts for password entry

---

## Future Enhancements

- [ ] Transfer funds between accounts
- [ ] Loan application system
- [ ] Loan repayment functionality
- [ ] Transaction history
- [ ] Account statement generation
- [ ] Data persistence (save to file/database)
- [ ] Interest calculation
- [ ] Multiple currency support
- [ ] Email/SMS notifications

---

## Technical Details

**Language:** Python 3.x

**External Dependencies:** None (uses only Python standard library)

**Modules Used:**
- `random` - For generating account addresses and special codes
- `time` - For account lockout timing
- `re` - For regular expressions in date validation

---

## Notes

- All account data is stored in memory and will be lost when the program exits
- Account addresses are unique 6-digit numbers
- Special codes are 6-digit numbers shared among linked accounts
- Branch IDs are 4-digit numbers with "BR" prefix
- The `__pycache__` folder is auto-generated by Python and can be ignored

---

## Developer

**Project Type:** CS Final Project

**Date:** February 2026

---

## License

This project is created for educational purposes.

---

**Happy Banking! 💰**
