import re

def check_password_strength(password):
    strength_points = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        strength_points += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Uppercase Check
    if re.search(r'[A-Z]', password):
        strength_points += 1
    else:
        feedback.append("❌ Include at least one uppercase letter.")

    # Lowercase Check
    if re.search(r'[a-z]', password):
        strength_points += 1
    else:
        feedback.append("❌ Include at least one lowercase letter.")

    # Digit Check
    if re.search(r'[0-9]', password):
        strength_points += 1
    else:
        feedback.append("❌ Include at least one number.")

    # Special Character Check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_points += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$, etc).")

    # Final Assessment
    if strength_points == 5:
        return "✅ Strong password!", []
    elif 3 <= strength_points < 5:
        return "⚠️ Moderate password", feedback
    else:
        return "❌ Weak password", feedback


if __name__ == "__main__":
    print("🔐 Password Strength Checker")
    print("Type 'exit' anytime to quit.\n")

    while True:
        user_input = input("Enter your password: ")

        if user_input.lower() in ['exit', 'quit']:
            print("👋 Exiting... Stay safe out there!")
            break

        strength, tips = check_password_strength(user_input)
        print(f"\nAssessment: {strength}")
        
        if tips:
            print("Suggestions to improve:")
            for tip in tips:
                print(f"- {tip}")
        else:
            print("You're good to go! 🔒")
            break

        print("\nTry again or type 'exit' to quit.\n")