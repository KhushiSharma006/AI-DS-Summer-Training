import streamlit as st
import pandas as pd
import numpy as np
import time

# ---------------- PAGE ----------------
st.set_page_config(page_title="Student Dashboard", page_icon="🎓", layout="wide")

st.title("🎓 Student Management Dashboard")
st.caption("Created using Streamlit Widgets")

st.markdown("---")

# ---------------- SIDEBAR ----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose Section",
    ["Dashboard", "Registration", "Data", "Charts"]
)

# ---------------- DASHBOARD ----------------
if page == "Dashboard":

    st.header("Dashboard Overview")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Students", 250)

    with c2:
        st.metric("Courses", 8)

    with c3:
        st.metric("Placement", "92%")

    st.divider()

    st.subheader("Announcements")

    st.info("Welcome to the Student Dashboard.")
    st.success("Semester registration is open.")
    st.warning("Assignment submission closes tomorrow.")
    st.error("Server maintenance on Sunday.")

    st.markdown("### Formula Example")
    st.latex(r"Accuracy=\frac{Correct\ Predictions}{Total\ Predictions}")

    st.code("""
def greet(name):
    print("Hello", name)
""", language="python")

# ---------------- REGISTRATION ----------------
elif page == "Registration":

    st.header("Student Registration Form")

    with st.form("student_form"):

        name = st.text_input("Student Name")

        email = st.text_input("Email")

        address = st.text_area("Address")

        age = st.number_input(
            "Age",
            min_value=16,
            max_value=40
        )

        marks = st.slider(
            "Marks",
            0,
            100,
            80
        )

        course = st.selectbox(
            "Course",
            ["Python", "AI", "Data Science", "Machine Learning"]
        )

        skills = st.multiselect(
            "Skills",
            ["Python", "C++", "SQL", "Java", "Pandas", "NumPy"]
        )

        gender = st.radio(
            "Gender",
            ["Male", "Female", "Other"]
        )

        dob = st.date_input("Date of Birth")

        meeting = st.time_input("Preferred Meeting Time")

        color = st.color_picker("Favorite Color")

        agree = st.checkbox("I accept Terms & Conditions")

        submit = st.form_submit_button("Submit")

    if submit:

        if not agree:
            st.warning("Please accept the terms.")
            st.stop()

        with st.spinner("Saving Details..."):
            time.sleep(2)

        st.success("Registration Successful!")

        st.balloons()

        student = {
            "Name": name,
            "Email": email,
            "Age": age,
            "Marks": marks,
            "Course": course,
            "Skills": skills,
            "Gender": gender,
            "DOB": str(dob),
            "Meeting": str(meeting),
            "Color": color
        }

        st.json(student)

        st.download_button(
            "Download Details",
            data=str(student),
            file_name="student.txt"
        )

# ---------------- DATA ----------------
elif page == "Data":

    st.header("Student Data")

    df = pd.DataFrame({
        "Name":["Aman","Khushi","Riya","Raj"],
        "Marks":[82,94,76,88],
        "Attendance":[90,96,85,91]
    })

    st.subheader("Interactive DataFrame")
    st.dataframe(df)

    st.subheader("Static Table")
    st.table(df)

    file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    if file is not None:

        uploaded = pd.read_csv(file)

        st.success("CSV Uploaded Successfully")

        st.dataframe(uploaded)

# ---------------- CHARTS ----------------
elif page == "Charts":

    st.header("Student Analytics")

    chart = pd.DataFrame({
        "Marks":[70,80,85,92,88],
        "Attendance":[75,81,90,93,95]
    })

    tab1, tab2, tab3 = st.tabs(
        ["Line", "Bar", "Area"]
    )

    with tab1:
        st.line_chart(chart)

    with tab2:
        st.bar_chart(chart)

    with tab3:
        st.area_chart(chart)

    with st.expander("More Information"):
        st.write(
            "Charts help visualize student performance."
        )

# ---------------- FOOTER ----------------
st.markdown("---")
st.text("Thank you for using the dashboard.")