import re
import streamlit as st
import random

# Constants
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numerics = '1234567890'
symbols = '!@#$%^&*'
all_chars = alphabet + numerics + symbols

# Password Generator
def generate_password(length=12):
    password = [
        random.choice(alphabet.lower()),
        random.choice(alphabet.upper()),
        random.choice(numerics),
        random.choice(symbols)
    ]
    while len(password) < length:
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return ''.join(password)

# Password Strength Checker
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0–9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    if score == 4:
        return score, "✅ Strong Password!"
    elif score == 3:
        return score, "⚠️ Moderate Password - Consider improving it."
    else:
        return score, "\n".join(feedback)

# Streamlit App
st.set_page_config(page_title="Password Checker", page_icon="🔒", layout="centered")
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

col1, col2 = st.columns(2)

with col1:
    if st.button("Check Password Strength"):
        score, result = check_password_strength(password)
        if score == 4:
            st.success(result)
        elif score == 3:
            st.warning(result)
        else:
            st.error(result)

with col2:
    if st.button("Generate Strong Password"):
        gen_pass = generate_password()
        st.code(gen_pass)


