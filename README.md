# Password Strength Checker 🔐

This project provides a simple Python script to check the strength of a user-provided password and suggest a strong alternative if the entered password is weak.

---

## Features
- **Password Strength Validation**:
  - Minimum length of 8 characters
  - Must contain at least one digit
  - Must contain at least one uppercase letter
  - Must contain at least one lowercase letter
  - Must contain at least one special symbol (`!@#$%^&*`)
- **Password Suggestion**:
  - Generates a random 10-character password containing letters, digits, and symbols.

---

## How It Works
1. The user is prompted to enter a password.
2. The script checks the password against the defined rules.
3. If the password is strong, it prints:


4. If the password is weak, it prints:



---

## Code Overview
- **`suggest_password()`**  
Generates a random 10-character password using uppercase, lowercase, digits, and symbols.

- **`check_password(password)`**  
Validates the password against strength criteria.

- **Main Program Flow**  
Prompts the user for input, checks the password, and prints the result.

---

## Example Usage
```bash
$ python password_checker.py
Enter password: hello123
Weak password
Suggested strong password: A9@dF!k2Qz

$ python password_checker.py
Enter password: Hello@123
strong password







Would you like me to also add a **step-by-step installation and run guide** (like cloning the repo, running the script, etc.) so it’s beginner-friendly?