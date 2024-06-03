import streamlit as st
import random
import string
import pandas as pd
from datetime import datetime

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special, custom_word):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if characters:
        remaining_length = length - len(custom_word) 
        if remaining_length < 0:
            return "Length too short for custom word and app name."
        
        password = ''.join(random.choice(characters) for _ in range(remaining_length))
        
        password_list = list(password)
        insert_positions = random.sample(range(len(password_list) + 1), 2)  # Get two random positions
        password_list.insert(insert_positions[0], custom_word)
        
        # Shuffle the password characters to ensure randomness
        random.shuffle(password_list)
        return ''.join(password_list)
    else:
        return "Please select at least one character set."

def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('generated_passwords.csv', mode='a', index=False, header=not pd.io.common.file_exists('generated_passwords.csv'))

st.title("Enhanced Password Generator")

st.sidebar.header("Settings")
password_length = st.sidebar.slider("Password length", min_value=6, max_value=24, value=12)
use_uppercase = st.sidebar.checkbox("Include uppercase letters", value=True)
use_lowercase = st.sidebar.checkbox("Include lowercase letters", value=True)
use_digits = st.sidebar.checkbox("Include digits", value=True)
use_special = st.sidebar.checkbox("Include special characters", value=True)

if not (use_uppercase or use_lowercase or use_digits or use_special):
    st.error("Please select at least one character set.")
else:
    custom_word = st.sidebar.text_input("Custom word (User/Website name)", value="Secret")

    if st.sidebar.button("Generate Password"):
        password = generate_password(password_length, use_uppercase, use_lowercase, use_digits, use_special, custom_word, app_name)
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
