import re

def check_password_strength(password):
    # Initialize lists to store missing criteria
    missing_criteria = []

    # Minimum length requirement
    if len(password) < 8:
        missing_criteria.append("Password is too short (at least 8 characters required).")
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        missing_criteria.append("Password should contain at least one lowercase letter.")
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        missing_criteria.append("Password should contain at least one uppercase letter.")
    
    # Check for at least one digit
    if not re.search(r'[0-9]', password):
        missing_criteria.append("Password should contain at least one digit.")
    
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\]', password):
        missing_criteria.append("Password should contain at least one special character.")
    
    if not missing_criteria:
        return "Strong: Password meets all criteria."
    else:
        return "Weak: " + ", ".join(missing_criteria)

# Keep running the script in a loop
while True:
    password = input("Enter a password (or 'exit' to quit): ")
    
    if password.lower() == 'exit':
        break  # Exit the loop if the user enters 'exit'
    
    result = check_password_strength(password)
    print(result)

