import re

def validate_date(date_str):
    """Validate date format dd/mm/yyyy with any separator"""
    try:
        # Replace any separator with /
        date_normalized = re.sub(r'[.,-/\s]', '/', date_str)
        parts = date_normalized.split('/')
        
        if len(parts) != 3:
            return False
        
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
        
        # Check valid ranges
        if day < 1 or day > 31:
            return False
        if month < 1 or month > 12:
            return False
        if year < 1900 or year > 2100:
            return False
        
        return True
    except:
        return False

def validate_home_address(address):
    """Check if address contains only valid characters and is more than 5 characters"""
    if len(address) <= 5:
        return False
    
    has_alphabet = False
    
    # Check for valid characters only (letters, numbers, spaces, hyphens, commas)
    for char in address:
        if char.isalpha():
            has_alphabet = True
        elif not (char.isdigit() or char in ' ,-./'):
            return False
    
    return has_alphabet

def validate_phone(phone, min_digits=7, max_digits=15):
    """Check if phone number is valid based on country standards"""
    # Remove spaces and dashes
    phone_clean = phone.replace(' ', '').replace('-', '')
    
    if len(phone_clean) < min_digits or len(phone_clean) > max_digits:
        return False
    
    for char in phone_clean:
        if not char.isdigit():
            return False
    
    return True

def validate_password(password):
    """Check if password has minimum 8 characters, contains numbers and alphabets"""
    if len(password) < 8:
        return False
    
    has_number = False
    has_alphabet = False
    
    for char in password:
        if char.isdigit():
            has_number = True
        if char.isalpha():
            has_alphabet = True
    
    return has_number and has_alphabet