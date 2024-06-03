import streamlit as st
import random
import string
import pandas as pd
from datetime import datetime

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special, custom_word):
    characters = ""
    password = ""
    ch = 0

    if use_uppercase:
        characters += random.choice(string.ascii_uppercase)
        ch+=1
    if use_lowercase:
        characters += random.choice(string.ascii_lowercase)
        ch+=1
    if use_digits:
        characters += random.choice(string.digits)
        ch+=1
    if use_special:
        characters += random.choice(string.punctuation)
        ch+=1

    remaining_length = length - len(custom_word) - ch

    if characters:
        if remaining_length < 0:
            return "Length too short for custom word."

        if not (use_uppercase or use_lowercase or use_digits or use_special):
            return "Please select at least one character from each character set."

        password += random.choice(string.ascii_uppercase) if use_uppercase else ""
        password += random.choice(string.ascii_lowercase) if use_lowercase else ""
        password += random.choice(string.digits) if use_digits else ""
        password += random.choice(string.punctuation) if use_special else ""

        password += ''.join(random.choice(characters) for _ in range(remaining_length - 4))

        password_list = list(password)

        insert_position = random.randint(0, len(password_list))
        password_list.insert(insert_position, custom_word)

        random.shuffle(password_list)
        return ''.join(password_list)
    else:
        return "Please select at least one character set."

def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('generated_passwords.csv', mode='a', index=False, header=not pd.io.common.file_exists('generated_passwords.csv'))

st.title("PASSWORD WIZARD")

st.sidebar.header("Settings")
password_length = st.sidebar.slider("Password length", min_value=6, max_value=24, value=12)
use_uppercase = st.sidebar.checkbox("Include uppercase letters", value=True)
use_lowercase = st.sidebar.checkbox("Include lowercase letters", )
use_digits = st.sidebar.checkbox("Include digits", )
use_special = st.sidebar.checkbox("Include special characters", )

if not (use_uppercase or use_lowercase or use_digits or use_special):
    st.error("Please select at least one character set.")
else:
    custom_word = st.sidebar.text_input("Custom word (User/Website name)", value="Google")

    if st.sidebar.button("Generate Password"):
        password = generate_password(password_length, use_uppercase, use_lowercase, use_digits, use_special, custom_word)
        st.text("Generated Password:")
        st.code(password)
        
        data = {
            'Date & Time': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            'Password Length': [password_length],
            'Uppercase': [use_uppercase],
            'Lowercase': [use_lowercase],
            'Digits': [use_digits],
            'Special Characters': [use_special],
            'Custom Word': [custom_word],
            'Generated Password': [password]
        }
        save_to_csv(data)
        st.success("Password is Generated")
    else:
        st.text("Click the button to generate a password")
