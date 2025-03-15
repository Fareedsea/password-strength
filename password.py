import streamlit as st
import re
import random
import string

def generate_strong_password():
    """Generates a strong password that includes uppercase, lowercase, digit, and special character."""
    characters = (
        random.choice(string.ascii_uppercase) +
        random.choice(string.ascii_lowercase) +
        random.choice(string.digits) +
        random.choice("!@#$%^&*") +
        ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=8))
    )
    password = ''.join(random.sample(characters, len(characters)))
    return password

def check_password_strength(password):
    """Checks the password strength against multiple criteria and returns feedback messages."""
    score = 0
    messages = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        messages.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        messages.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        messages.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        messages.append("✅ Strong Password!")
    elif score == 3:
        messages.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        messages.append("❌ Weak Password - Improve it using the suggestions above.")
        messages.append("🔹 Suggested Strong Password: " + generate_strong_password())
    
    return messages

# Streamlit App Layout
st.title("Password Strength Checker")

# Get user input for password
password = st.text_input("Enter your password:", type="password")

if st.button("Check Password"):
    if password:
        results = check_password_strength(password)
        for result in results:
            st.write(result)
    else:
        st.write("Please enter a password.")
