import streamlit as st
import string

st.set_page_config(page_title="🔒Password Strength Checker",layout='centered')
st.title("🔒Password Strength Checker")


# Password input field
password = st.text_input("Enter your password", type="password")

def has_upper_and_lower(s):
    return any(c.islower() for c in s) and any(c.isupper() for c in s)


def has_special_char(s):
    special_chars = string.punctuation  # All special characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    return any(c in special_chars for c in s)

def has_digit(s):
    return any(c.isdigit() for c in s)

def password_strength_checker(password):
    if len(password) < 8:
        error="The password must have 8 characters"
        st.error(error)
    
    
    if has_upper_and_lower(password) != True:
        error="The password must have one uppercase and lower case character"
        st.error(error)

    
    if has_special_char(password) != True:
        error="The password must have one special character"
        st.error(error)


    if has_digit(password) != True:
        error="The password must have one digit"
        st.error(error)

def password_score(password):
    score=0
    if len(password) >= 8:
        score=score+2
    if has_upper_and_lower(password) == True:
        score+=1
    if has_special_char(password) == True:
        score+=1
    if has_digit(password) == True:
        score+=1
    return score



    



password_strength_checker(password)
total_password_score=password_score(password)

if total_password_score <= 2:
    st.write("Your password is weak 😔")
if total_password_score > 3 and total_password_score <= 4:
    st.write("Your password is Moderate 😐")
if total_password_score == 5:
    st.write("Your password is Strong 💪")
