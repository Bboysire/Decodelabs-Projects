def check_password_strength(password: str) -> str:
    # Step 1: Length Validation Baseline
    if len(password) < 8:
        return "Weak (Failed Length Policy: Must be 8+ characters)"
    
    # Step 2: Pythonic, Short-Circuit Linear Scans
    has_upper  = any(char.isupper() for char in password)
    has_digit  = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)
    
    # Step 3: Risk Classification Output
    criteria_met = sum([has_upper, has_digit, has_symbol])
    
    if criteria_met == 3:
        return "Strong"
    elif criteria_met == 2:
        return "Medium"
    else:
        return "Weak"

# Test environment driver loop
if __name__ == "__main__":
    user_input = input("Enter a password to evaluate: ")
    result = check_password_strength(user_input)
    print(f"Result: {result}")