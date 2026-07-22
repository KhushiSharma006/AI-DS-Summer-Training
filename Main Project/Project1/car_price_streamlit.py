
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import os

st.set_page_config(page_title="Car Selling Price Prediction", page_icon="🚗")

base_dir = os.path.dirname(os.path.abspath(__file__))

@st.cache_resource
def train_model():
    cars_data = pd.read_csv(os.path.join(base_dir, "Cardetails.csv"))
    cars_data = cars_data.drop(columns=["torque"])
    cars_data = cars_data.dropna()

    cars_data["name"] = cars_data["name"].apply(lambda x: x.split()[0])
    cars_data["mileage"] = cars_data["mileage"].apply(lambda x: float(x.split()[0]))
    cars_data["engine"] = cars_data["engine"].apply(lambda x: float(x.split()[0]))
    cars_data["max_power"] = pd.to_numeric(
        cars_data["max_power"].apply(lambda x: x.split()[0]), errors="coerce"
    )
    cars_data = cars_data.dropna()

    encoders = {}
    for col in ["name","fuel","seller_type","transmission","owner"]:
        le = LabelEncoder()
        cars_data[col] = le.fit_transform(cars_data[col])
        encoders[col] = le

    X = cars_data.drop(columns=["selling_price"])
    y = cars_data["selling_price"]

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
    model = LinearRegression()
    model.fit(X_train,y_train)
    return model,encoders

model, encoders = train_model()

st.title("🚗 Car Selling Price Predictor")

brand = st.selectbox("Car Brand", encoders["name"].classes_)
year = st.number_input("Year", 1990, 2035, 2018)
km = st.number_input("Kilometers Driven", 0, 1000000, 50000)
fuel = st.selectbox("Fuel", encoders["fuel"].classes_)
seller = st.selectbox("Seller Type", encoders["seller_type"].classes_)
trans = st.selectbox("Transmission", encoders["transmission"].classes_)
owner = st.selectbox("Owner", encoders["owner"].classes_)
mileage = st.number_input("Mileage (kmpl)", 5.0, 50.0, 20.0)
engine = st.number_input("Engine (CC)", 500.0, 5000.0, 1200.0)
power = st.number_input("Max Power (bhp)", 20.0, 500.0, 80.0)
seats = st.number_input("Seats", 2, 10, 5)

if st.button("Predict Selling Price"):
    row = pd.DataFrame([{
        "name": encoders["name"].transform([brand])[0],
        "year": year,
        "km_driven": km,
        "fuel": encoders["fuel"].transform([fuel])[0],
        "seller_type": encoders["seller_type"].transform([seller])[0],
        "transmission": encoders["transmission"].transform([trans])[0],
        "owner": encoders["owner"].transform([owner])[0],
        "mileage": mileage,
        "engine": engine,
        "max_power": power,
        "seats": seats
    }])

    prediction = model.predict(row)[0]
    st.success(f"Estimated Selling Price: ₹{prediction:,.0f}")
