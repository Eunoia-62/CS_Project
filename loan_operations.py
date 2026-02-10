import time
from data_storage import accounts

INTEREST_RATE = 0.05  # 5%

LOAN_TYPES = {
    '1': 'Home Loan',
    '2': 'Car Loan',
    '3': 'Education Loan',
    '4': 'Personal Loan',
    '5': 'Gold Loan'
}

PAYMENT_PLANS = {
    '1': ('Weekly', 0.25),
    '2': ('Monthly', 1),
    '3': ('Quarterly', 3),
    '4': ('Half Yearly', 6),
    '5': ('Yearly', 12)
}


def apply_loan(acc_address):
    """Handle loan application"""
    account = accounts[acc_address]
    
    print("\n" + "="*50)
    print("APPLY FOR LOAN")
    print("="*50)

    # Get loan amount
    try:
        amount = float(input("\nEnter loan amount: $"))
        if amount <= 0:
            print("Invalid amount! Amount must be greater than zero.")
            input("Press Enter to continue...")
            return
    except ValueError:
        print("Invalid amount! Please enter a valid number.")
        input("Press Enter to continue...")
        return

    # Select loan type
    print("\nSelect Loan Type:")
    for key, value in LOAN_TYPES.items():
        print(key + ". " + value)

    loan_choice = input("\nEnter your choice: ").strip()
    if loan_choice not in LOAN_TYPES:
        print("Invalid loan type!")
        input("Press Enter to continue...")
        return

    loan_type = LOAN_TYPES[loan_choice]

    # Select payment plan
    print("\nSelect Payment Plan:")
    for key, (name, months) in PAYMENT_PLANS.items():
        print(key + ". " + name)

    plan_choice = input("\nEnter your choice: ").strip()
    if plan_choice not in PAYMENT_PLANS:
        print("Invalid payment plan!")
        input("Press Enter to continue...")
        return

    plan_name, interval_months = PAYMENT_PLANS[plan_choice]

    # Validation with special code and password
    print("\n" + "-"*50)
    print("VERIFICATION")
    print("-"*50)
    special_code = input("Enter your special code: ").strip()
    password = input("Enter your password: ").strip()

    if special_code != account['special_code']:
        print("\nIncorrect special code! Authentication failed.")
        input("Press Enter to continue...")
        return
    
    if password != account['password']:
        print("\nIncorrect password! Authentication failed.")
        input("Press Enter to continue...")
        return

    # Calculate loan details
    interest_amount = amount * INTEREST_RATE
    total_payable = amount + interest_amount
    
    # Calculate installment amount based on payment plan
    if interval_months == 0.25:  # Weekly
        total_installments = 52  # 1 year in weeks
    elif interval_months == 1:  # Monthly
        total_installments = 12  # 1 year
    elif interval_months == 3:  # Quarterly
        total_installments = 4
    elif interval_months == 6:  # Half Yearly
        total_installments = 2
    else:  # Yearly
        total_installments = 1
    
    installment_amount = total_payable / total_installments

    # Create loan record
    loan = {
        'principal': amount,
        'interest_rate': INTEREST_RATE,
        'interest_amount': interest_amount,
        'total_payable': total_payable,
        'paid_amount': 0.0,
        'remaining_amount': total_payable,
        'payment_plan': plan_name,
        'installment_interval_months': interval_months,
        'suggested_installment': installment_amount,
        'total_installments': total_installments,
        'installments_paid': 0,
        'start_date': time.strftime("%d/%m/%Y", time.localtime()),
        'last_payment_date': None
    }

    # Add loan to account
    if 'loans' not in account:
        account['loans'] = {}
    
    if loan_type not in account['loans']:
        account['loans'][loan_type] = []
    
    account['loans'][loan_type].append(loan)

    # Display loan details
    print("\n" + "="*50)
    print("LOAN APPROVED!")
    print("="*50)
    print("Customer Name: " + account['name'])
    print("Loan Type: " + loan_type)
    print("Loan Amount (Principal): $" + str(amount))
    print("Interest Rate: 5%")
    print("Interest Amount: $" + str(round(interest_amount, 2)))
    print("Total Payable: $" + str(round(total_payable, 2)))
    print("Payment Plan: " + plan_name)
    print("Suggested Installment: $" + str(round(installment_amount, 2)))
    print("Total Installments: " + str(total_installments))
    print("Installments Paid: 0")
    print("Amount Paid: $0.00")
    print("Amount Remaining: $" + str(round(total_payable, 2)))
    print("Loan Start Date: " + loan['start_date'])
    print("="*50)
    
    input("\nPress Enter to continue...")


def check_loans(acc_address):
    """Display all loans categorized by type"""
    account = accounts[acc_address]
    loans = account.get('loans', {})

    print("\n" + "="*50)
    print("LOAN STATUS")
    print("="*50)
    print("Account Holder: " + account['name'])
    print("Account Address: " + acc_address)
    print("="*50)

    # Show all loan types
    for loan_type_key, loan_type_name in LOAN_TYPES.items():
        print("\n" + loan_type_name + ":")
        
        if loan_type_name not in loans or not loans[loan_type_name]:
            print("  No loan pending")
        else:
            loan_list = loans[loan_type_name]
            for i, loan in enumerate(loan_list, start=1):
                print("\n  Loan #" + str(i) + ":")
                print("    Principal Amount: $" + str(loan['principal']))
                print("    Interest Rate: " + str(int(loan['interest_rate'] * 100)) + "%")
                print("    Total Payable: $" + str(round(loan['total_payable'], 2)))
                print("    Amount Paid: $" + str(round(loan['paid_amount'], 2)))
                print("    Amount Remaining: $" + str(round(loan['remaining_amount'], 2)))
                print("    Payment Plan: " + loan['payment_plan'])
                print("    Suggested Installment: $" + str(round(loan['suggested_installment'], 2)))
                print("    Installments Paid: " + str(loan['installments_paid']) + "/" + str(loan['total_installments']))
                print("    Start Date: " + loan['start_date'])
                
                if loan['last_payment_date']:
                    print("    Last Payment: " + loan['last_payment_date'])
                else:
                    print("    Last Payment: No payments yet")
                
                if loan['remaining_amount'] <= 0:
                    print("    Status: FULLY PAID")
                else:
                    completion = (loan['paid_amount'] / loan['total_payable']) * 100
                    print("    Completion: " + str(round(completion, 1)) + "%")

    print("\n" + "="*50)
    input("\nPress Enter to continue...")


def repay_loan(acc_address):
    """Handle loan repayment"""
    account = accounts[acc_address]

    if 'loans' not in account or not account['loans']:
        print("\nNo loans to repay.")
        input("Press Enter to continue...")
        return

    # Show current loans
    check_loans(acc_address)

    print("\n" + "="*50)
    print("LOAN REPAYMENT")
    print("="*50)

    # Show available loan types
    print("\nAvailable Loan Categories:")
    available_types = []
    for loan_type, loan_list in account['loans'].items():
        if loan_list and any(loan['remaining_amount'] > 0 for loan in loan_list):
            available_types.append(loan_type)
            print("- " + loan_type)
    
    if not available_types:
        print("\nNo active loans to repay!")
        input("Press Enter to continue...")
        return

    loan_type = input("\nEnter loan category name (exactly as shown): ").strip()
    
    if loan_type not in account['loans']:
        print("Invalid loan category!")
        input("Press Enter to continue...")
        return

    loans = account['loans'][loan_type]
    
    # Filter out fully paid loans
    active_loans = [loan for loan in loans if loan['remaining_amount'] > 0]
    
    if not active_loans:
        print("No active loans under this category.")
        input("Press Enter to continue...")
        return

    if len(active_loans) == 1:
        loan_index = 0
        loan = active_loans[0]
    else:
        print("\nMultiple loans found. Select loan number:")
        for i, loan in enumerate(active_loans, start=1):
            print(str(i) + ". Loan of $" + str(loan['principal']) + " (Remaining: $" + str(round(loan['remaining_amount'], 2)) + ")")
        
        try:
            loan_index = int(input("\nEnter loan number: ")) - 1
            if loan_index < 0 or loan_index >= len(active_loans):
                print("Invalid selection!")
                input("Press Enter to continue...")
                return
            loan = active_loans[loan_index]
        except ValueError:
            print("Invalid input!")
            input("Press Enter to continue...")
            return

    # Display selected loan details
    print("\n" + "-"*50)
    print("Selected Loan Details:")
    print("-"*50)
    print("Principal: $" + str(loan['principal']))
    print("Total Payable: $" + str(round(loan['total_payable'], 2)))
    print("Amount Paid: $" + str(round(loan['paid_amount'], 2)))
    print("Amount Remaining: $" + str(round(loan['remaining_amount'], 2)))
    print("Suggested Installment: $" + str(round(loan['suggested_installment'], 2)))
    print("-"*50)
    print("Your Account Balance: $" + str(account['balance']))
    print("-"*50)

    # Get repayment amount
    try:
        amount = float(input("\nEnter repayment amount: $"))
        if amount <= 0:
            print("Invalid amount! Amount must be greater than zero.")
            input("Press Enter to continue...")
            return
    except ValueError:
        print("Invalid amount! Please enter a valid number.")
        input("Press Enter to continue...")
        return

    # Check if user has sufficient balance
    if account['balance'] < amount:
        print("\nInsufficient balance!")
        print("Your balance: $" + str(account['balance']))
        print("Required amount: $" + str(amount))
        input("Press Enter to continue...")
        return

    # Prevent overpayment
    if amount > loan['remaining_amount']:
        print("\nAmount exceeds remaining loan balance!")
        print("Maximum you can pay: $" + str(round(loan['remaining_amount'], 2)))
        
        overpay_choice = input("Pay the exact remaining amount instead? (yes/no): ").strip().lower()
        if overpay_choice == 'yes':
            amount = loan['remaining_amount']
        else:
            input("Press Enter to continue...")
            return

    # Process payment
    account['balance'] -= amount
    loan['paid_amount'] += amount
    loan['remaining_amount'] -= amount
    loan['installments_paid'] += 1
    loan['last_payment_date'] = time.strftime("%d/%m/%Y", time.localtime())

    # Display payment confirmation
    print("\n" + "="*50)
    print("PAYMENT SUCCESSFUL!")
    print("="*50)
    print("Amount Paid: $" + str(round(amount, 2)))
    print("New Account Balance: $" + str(round(account['balance'], 2)))
    print("\nUpdated Loan Details:")
    print("Amount Paid So Far: $" + str(round(loan['paid_amount'], 2)))
    print("Amount Remaining: $" + str(round(loan['remaining_amount'], 2)))
    print("Installments Paid: " + str(loan['installments_paid']) + "/" + str(loan['total_installments']))
    
    if loan['remaining_amount'] <= 0:
        print("\n*** CONGRATULATIONS! LOAN FULLY REPAID! ***")
        # Remove fully paid loan from list
        original_loans = account['loans'][loan_type]
        for i, l in enumerate(original_loans):
            if l is loan:
                original_loans.pop(i)
                break
    else:
        completion = (loan['paid_amount'] / loan['total_payable']) * 100
        print("Loan Completion: " + str(round(completion, 1)) + "%")
    
    print("="*50)
    input("\nPress Enter to continue...")


def loan_options_menu(acc_address):
    """Display and handle loan options"""
    while True:
        print("\n" + "-"*50)
        print("LOAN OPTIONS")
        print("-"*50)
        print("1. Apply for Loan")
        print("2. Check Loan Status")
        print("3. Repay Loan")
        print("4. Back to Menu")
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == '1':
            apply_loan(acc_address)
        elif choice == '2':
            check_loans(acc_address)
        elif choice == '3':
            repay_loan(acc_address)
        elif choice == '4':
            break
        else:
            print("Invalid choice!")