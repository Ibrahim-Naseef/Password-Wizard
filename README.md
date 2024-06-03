# Password Wizard 🧙‍♂️

Welcome to Password Wizard, an enhanced password generator tool powered by Streamlit! 🚀

## Overview

Password Wizard allows you to generate strong and customizable passwords for your various accounts with ease. It offers a range of options to tailor your password generation experience, ensuring both security and convenience.

## Features

🔐 Customize password length  
🔡 Include uppercase and lowercase letters  
🔢 Include digits  
🧷 Include special characters  
🔠 Optional custom word (User/website name)inclusion  
📝 Save password details to CSV  

## Usage

1. Adjust your password preferences using the sidebar settings.
2. Click on the "Generate Password" button to create your unique password.
3. Copy the generated password and use it for your accounts.
4. Password details are saved to a CSV file for future reference.



## How to Run Locally

1. Clone this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the app using Streamlit by executing `streamlit run app.py`.

## Code
```
import streamlit as st
import random
import string
import pandas as pd
from datetime import datetime

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special, custom_word):
    characters = ""
    password = ""

    if use_uppercase:
        characters += random.choice(string.ascii_uppercase)
    if use_lowercase:
        characters += random.choice(string.ascii_lowercase)
    if use_digits:
        characters += random.choice(string.digits)
    if use_special:
        characters += random.choice(string.punctuation)

    remaining_length = length - len(custom_word)

    if characters:
        if remaining_length < 0:
            return "Length too short for custom word."

        # Check if at least one character set is selected
        if not (use_uppercase or use_lowercase or use_digits or use_special):
            return "Please select at least one character from each character set."

        # Add one character from each selected character set to the password
        password += random.choice(string.ascii_uppercase) if use_uppercase else ""
        password += random.choice(string.ascii_lowercase) if use_lowercase else ""
        password += random.choice(string.digits) if use_digits else ""
        password += random.choice(string.punctuation) if use_special else ""

        # Fill the remaining password length with random characters
        password += ''.join(random.choice(characters) for _ in range(remaining_length - 4))

        # Convert the password to a list for easy insertion of custom word
        password_list = list(password)

        # Insert the custom word at a random position
        insert_position = random.randint(0, len(password_list))
        password_list.insert(insert_position, custom_word)

        # Shuffle the password characters to ensure randomness
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
use_lowercase = st.sidebar.checkbox("Include lowercase letters", value=True)
use_digits = st.sidebar.checkbox("Include digits", value=True)
use_special = st.sidebar.checkbox("Include special characters", value=True)

if not (use_uppercase or use_lowercase or use_digits or use_special):
    st.error("Please select at least one character set.")
else:
    custom_word = st.sidebar.text_input("Custom word (User/Website name)", value="xyz")

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

```

## Results
![image](https://github.com/Ibrahim-Naseef/Password-Wizard/assets/156147657/bb3e44e9-a132-4b55-b38f-07a40884db65)
![Streamlit-GoogleChrome2024-06-0315-11-49-ezgif com-video-to-gif-converter](https://github.com/Ibrahim-Naseef/Password-Wizard/assets/156147657/156c9462-a081-4cfe-8688-a16ad2b7e1de)



## Try it out!

You can try the Password Wizard app live [Password Wizard](https://password-wizard.streamlit.app/).
