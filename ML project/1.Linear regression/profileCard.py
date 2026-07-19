import streamlit as st

st.set_page_config(page_title="Student Profile Card", page_icon="🎓")

st.title("🎓 Student Profile Card")

# Input Section
st.header("Enter Student Details")

photo = st.file_uploader("Upload Student Photo", type=["jpg", "jpeg", "png"])

name = st.text_input("Name")

course = st.selectbox(
    "Course",
    [
        "Data Science",
        "Artificial Intelligence",
        "Machine Learning",
        "Computer Science",
        "Information Technology",
        "Cyber Security",
        "Cloud Computing"
    ]
)
college = st.text_input("College")
email = st.text_input("Email")
phone = st.text_input("Phone")

skills = st.multiselect(
    "Select Skills",
    [
        # Programming Languages
        "Python",
        "C++",
        "JAVA",
        "Javascript",
        "SQL",

        # Data Analysis
        "NumPy",
        "Pandas",
        "SciPy",

        # Visualization
        "Matplotlib",
        "Seaborn",
        "Plotly",

        # Machine Learning
        "Scikit-learn",
        "XGBoost",
        "LightGBM",
        "CatBoost",

        # Deep Learning
        "TensorFlow",
        "Keras",
        "PyTorch",

        # NLP
        "NLTK",
        "spaCy",
        "Transformers",
        "Hugging Face",

        # Computer Vision
        "OpenCV",
        "YOLO",

        # Model Deployment
        "Flask",
        "FastAPI",
        "Streamlit",
       

        # Databases
        "MySQL",
        "MongoDB",
        "PostgreSQL",

        # Cloud Platforms
        "AWS",
        "Google Cloud",
        "Microsoft Azure",

        # Version Control
        "Git",
        "GitHub",

    ]
)

# Button
if st.button("Submit Profile"):

    st.markdown("---")
    st.header("📋 Student Profile")

    col1, col2 = st.columns([1,2])

    with col1:
        if photo:
            st.image(photo, width=180)
        else:
            st.write("No Photo Uploaded")

    with col2:
        st.write(f"**Name:** {name}")
        st.write(f"**Course:** {course}")
        st.write(f"**College:** {college}")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone:** {phone}")

        st.write("**Skills:**")
        if skills:
            for skill in skills:
                st.write(f"✔ {skill}")
        else:
            st.write("No skills selected.")

    st.success("Profile Submitted Successfully!")