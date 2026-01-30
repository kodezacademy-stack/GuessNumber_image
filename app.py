import streamlit as st
import random
st.title("🎯 Guess the Number")
secret = random.randint(1, 10)
guess = st.number_input("Guess a number (1–10)", 1, 10)
st.image("image.png")
if st.button("Check"):
    if guess == secret:
        st.success("🎉 Correct!")
    elif guess < secret:
        st.info("🔼 Too low")
    elif guess > secret:
        st.info("🔽 Too high")   
    else:
        st.error("❌ Try again")
