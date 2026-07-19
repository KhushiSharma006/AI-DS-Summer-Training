import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


st.set_page_config(page_title="Employee Leave Prediction", layout="wide")

st.title("Employee Leave Prediction using Decision Tree")
st.write("This application predicts whether an employee will leave the company.")


df = pd.read_csv("Employee.csv")

st.subheader("Dataset")
st.dataframe(df)


data = df.copy()

# Drop Name column if present
if "Name" in data.columns:
    data.drop("Name", axis=1, inplace=True)

# Encode categorical columns
label_encoders = {}

for col in data.columns:
    if data[col].dtype == "object":
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        label_encoders[col] = le

X = data.drop("LeaveOrNot", axis=1)
y = data["LeaveOrNot"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

st.subheader("Model Performance")

st.success(f"Accuracy : {accuracy * 100:.2f}%")

st.write("### Confusion Matrix")

cm = confusion_matrix(y_test, y_pred)

cm_df = pd.DataFrame(
    cm,
    index=["Actual Stay", "Actual Leave"],
    columns=["Predicted Stay", "Predicted Leave"]
)

st.dataframe(cm_df)

st.write("### Classification Report")

report = classification_report(y_test, y_pred, output_dict=True)
st.dataframe(pd.DataFrame(report).transpose())


st.subheader("Predict Employee Leave")

education = st.selectbox(
    "Education",
    label_encoders["Education"].classes_
)

joining_year = st.number_input(
    "Joining Year",
    min_value=2000,
    max_value=2030,
    value=2016
)

city = st.selectbox(
    "City",
    label_encoders["City"].classes_
)

salary = st.number_input(
    "Salary",
    min_value=10000,
    max_value=5000000,
    value=500000
)

payment_tier = st.selectbox(
    "Payment Tier",
    sorted(df["PaymentTier"].unique())
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=60,
    value=25
)

gender = st.selectbox(
    "Gender",
    label_encoders["Gender"].classes_
)

ever_benched = st.selectbox(
    "Ever Benched",
    label_encoders["EverBenched"].classes_
)

experience = st.number_input(
    "Experience in Current Domain",
    min_value=0,
    max_value=20,
    value=2
)


if st.button("Predict"):

    input_dict = {
        "Education": label_encoders["Education"].transform([education])[0],
        "JoiningYear": joining_year,
        "City": label_encoders["City"].transform([city])[0],
        "Salary": salary,
        "PaymentTier": payment_tier,
        "Age": age,
        "Gender": label_encoders["Gender"].transform([gender])[0],
        "EverBenched": label_encoders["EverBenched"].transform([ever_benched])[0],
        "ExperienceInCurrentDomain": experience
    }

    input_data = pd.DataFrame([input_dict])

    input_data = input_data[X.columns]

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("Employee is likely to Leave.")
    else:
        st.success("Employee is likely to Stay.")

    st.write("### Prediction Probability")
    st.write(f"Stay : **{probability[0]*100:.2f}%**")
    st.write(f"Leave : **{probability[1]*100:.2f}%**")

# ---------------------------------------------------
# Show Training Feature Order (Debug)
# ---------------------------------------------------
with st.expander("Training Feature Order"):
    st.write(X.columns.tolist())