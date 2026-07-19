import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("experience_salary_40_records.csv")


X = df[["Experience"]]
y = df["Salary"]

model = LinearRegression()
model.fit(X, y)

st.set_page_config(page_title="Salary Prediction", page_icon="💰")

st.title("💰 Salary Prediction Dashboard")

st.write("Predict salary based on years of experience.")


experience = st.slider(
    "Select Years of Experience",
    min_value=int(df["Experience"].min()),
    max_value=int(df["Experience"].max()),
    value=1
)


if st.button("Predict Salary"):

    salary = model.predict([[experience]])

    st.success(f"Predicted Salary: ₹ {salary[0]:,.2f}")
