import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Multiple Salary Prediction",
    page_icon="💰",
    layout="centered"
)


df = pd.read_csv("multiple_linear_salary_dataset_50_records.csv")

X = df[["Experience", "Education_Level", "Age"]]
y = df["Salary"]


model = LinearRegression()
model.fit(X, y)

accuracy = model.score(X, y)


st.sidebar.title("Dashboard")

if st.sidebar.checkbox("Show Dataset"):
    st.write(df)


st.title("💰 Multiple Salary Prediction Dashboard")

st.write("Enter employee details and click **Predict Salary**.")


experience = st.slider(
    "Years of Experience",
    int(df["Experience"].min()),
    int(df["Experience"].max()),
    5
)

education = st.slider(
    "Education Level",
    int(df["Education_Level"].min()),
    int(df["Education_Level"].max()),
    15
)

age = st.slider(
    "Age",
    int(df["Age"].min()),
    int(df["Age"].max()),
    25
)


if st.button("Predict Salary"):

    prediction = model.predict([[experience, education, age]])

    st.metric(
        label="Predicted Salary",
        value=f"₹ {prediction[0]:,.2f}"
    )

