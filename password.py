# import modules
import re 
import random
import string

# strong_password()function
def suggest_password(): 
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*"

    all_chars = letters + digits + symbols

    password = ""
    for i in range(10):
        password += random.choice(all_chars)

    return password

# check_password()function
def check_password(password):# check digit, uppercase and lowercase latter or symbol 
    if len(password) < 8:
        return False
    if re.search(r"\d", password) is None:
        return False
    if re.search(r"[A-Z]", password) is None:
        return False
    if re.search(r"[a-z]", password) is None:
        return False
    if re.search(r"[!@#$%^&*]", password) is None:
        return False
    return True

# input from user 
password = input("Enter password: ")

# print password or suggest_
if check_password(password):
    print("strong password ")

else:
    print("Weak password ")
    print("Suggested strong password: ", suggest_password())