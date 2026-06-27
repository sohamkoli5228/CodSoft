import random
import string
import secrets
import os

# ===============================
#      ELITE PASSWORD GENERATOR
# ===============================

os.system("cls" if os.name == "nt" else "clear")

print("=" * 60)
print("        🔐 ELITE PASSWORD GENERATOR v2.0")
print("=" * 60)

print("""
Choose Password Strength

1. Weak
2. Medium
3. Strong
4. Ultra Secure
""")

strength = input("Select (1-4): ")

if strength == "1":
    default_length = 8
elif strength == "2":
    default_length = 12
elif strength == "3":
    default_length = 16
elif strength == "4":
    default_length = 24
else:
    print("Invalid choice!")
    exit()

length = input(f"Password Length (Press Enter for {default_length}): ")

if length == "":
    length = default_length
else:
    length = int(length)

if length < 6:
    print("Password should be at least 6 characters.")
    exit()

count = int(input("How many passwords to generate? "))

exclude = "O0Il1|`'\""

uppercase = ''.join(c for c in string.ascii_uppercase if c not in exclude)
lowercase = ''.join(c for c in string.ascii_lowercase if c not in exclude)
numbers = ''.join(c for c in string.digits if c not in exclude)
symbols = "!@#$%^&*()-_=+[]{}<>?/"

all_chars = uppercase + lowercase + numbers + symbols

def generate_password(length):

    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(numbers),
        secrets.choice(symbols)
    ]

    while len(password) < length:
        password.append(secrets.choice(all_chars))

    random.shuffle(password)

    return ''.join(password)

def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in symbols for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    elif score == 5:
        return "Strong"
    else:
        return "Ultra Secure"

print("\n" + "=" * 60)
print("Generated Passwords")
print("=" * 60)

with open("passwords.txt", "w") as file:

    for i in range(count):

        pwd = generate_password(length)
        strength = check_strength(pwd)

        print(f"{i+1}. {pwd}")
        print(f"   Strength : {strength}")
        print("-" * 60)

        file.write(f"{i+1}. {pwd} ({strength})\n")

print("\nPasswords saved to passwords.txt")
print("Thank you for using Elite Password Generator!")
print("=" * 60)