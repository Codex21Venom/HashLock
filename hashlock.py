import bcrypt
from getpass import getpass
import time
from password_strength_checker import check_password_strength  # your existing file

def hash_pass(passwd):
    """Hash a password securely using bcrypt."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(passwd.encode(), salt)

def verify_pass(plain_pass, hashed_pass):
    """Verify a password against its bcrypt hash."""
    return bcrypt.checkpw(plain_pass.encode(), hashed_pass)

def main():
    print("=== Welcome to HashLock: Secure Password Confirmation Tool ===")
    
    while True:
        passwd = getpass("Enter your password: ")
        strength, tips = check_password_strength(passwd)

        print(f"\nStrength: {strength}")
        if tips:
            print("Suggestions to improve:")
            for t in tips:
                print(f"- {t}")
            print("\nPlease improve your password before continuing.\n")
            continue  # Ask again if password is weak or moderate
        else:
            print("✅ Strong password confirmed.\n")
            break

    hashed = hash_pass(passwd)
    confirm = getpass("Confirm your password: ")

    if verify_pass(confirm, hashed):
        print("\nPassword confirmed successfully!\n")
    else:
        print("\n❌ Passwords do not match. Exiting for security reasons.")
        for i in range(3, 0, -1):
            print(f"Exiting in {i}...", end="\r")
            time.sleep(1)
        print("Exiting now...          ")
        exit(1)

    while True:
        print("\nSelect an option:\n1. Authenticate Password\n2. Show Hashed Password (if authenticated)\n3. Exit\n")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                attempts = 3
                while attempts > 0:
                    entered = getpass("Enter your password for verification: ")
                    if verify_pass(entered, hashed):
                        print("\n🔐 Password verified successfully!")
                        break
                    else:
                        attempts -= 1
                        print(f"❌ Incorrect password. Attempts left: {attempts}")
                else:
                    print("\n🚨 Too many failed attempts! Access locked.")
            
            case "2":
                entered = getpass("Enter password to view stored hash: ")
                if verify_pass(entered, hashed):
                    print("\n🧩 Your stored bcrypt hash value is:")
                    print(hashed.decode())  # decode bytes for clean print
                else:
                    print("\n❌ Authentication failed! Cannot display hash.")
            
            case "3":
                print("\n👋 Exiting HashLock. Stay secure!")
                break
            
            case _:
                print("⚠️ Invalid option. Try again.")


if __name__ == "__main__":
    main()
