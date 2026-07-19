import streamlit as st
import pandas as pd
import numpy as np
#Page Layout
st.set_page_config(
    page_title="Student Performance System",
    page_icon="@",
    layout="wide"
    )
#Header
st.title("Student Performance System")
st.write("###Machine Learning Dashboard")
st.divider()
st.sidebar.header("Students Details")
name=st.sidebar.text_input("Student Name")
age=st.sidebar.number_input(
    "Age",min_value=15,max_value=30,value=20
)
gender=st.sidebar.selectbox(
    "Gender",["male","female"])
sHour=st.sidebar.slider(
    "Study Hours",0,12,5)
att=st.sidebar.slider("Attendence",0,100,75)
ass=st.sidebar.slider("Assignment Completed",0,10,6)
predict=st.sidebar.button("Predict")
# Main Layout
c1,c2=st.columns([2,1])
with c1:
    st.subheader("Student Information")
    st.write("**Name:**",name)
    st.write("**Age:**",age)
    st.write("**Gender:**",gender)
    st.write("**Attendence:**",att)
    st.write("**Study Hours:**",sHour)
    st.write("**Assignments:**",ass)
with c2:
    st.subheader("Performance")
    st.metric("Attendence",f"{att}%")
    st.metric("Study Hours",sHour)
    st.metric("Assignment",ass)
st.divider()
if predict==True:
    prediction=np.random.randint(60,95)
    st.success("Prediction completed successfully")

    st.metric(
        label="Predicted Marks",
        value=f"{prediction}%"
    )
    st.balloons()
t1,t2,t3=st.tabs(
    ["Charts","Data","About"]
)
with t1:
    d=pd.DataFrame({"Subjects":["Maths","Science","English","Python"],"Marks":[78,82,90,88]})
    st.bar_chart(d.set_index("Subjects"))
with t2:
     d=pd.DataFrame({"Subjects":["Maths","Science","English","Python"],"Marks":[78,82,90,88]})
     st.dataframe(d)
with t3:
    st.info("""This application predicts student performance.
    Technologies Used:
    -Python
    -Streamlit
    -numpy
    -pandas
    -machineLearning""")