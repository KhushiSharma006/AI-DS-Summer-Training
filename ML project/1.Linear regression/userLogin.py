import streamlit as st

st.title("User Login Page")
uid  = st.text_input("User ID: ")
pswd = st.text_input("Password", type="password")

st.subheader("per")

st.button("Login")
st.button("Reset")

