import streamlit as st
st.title("mahes1316")
st.sidebar.title("Give us your valid Info")
s=st.sidebar.text_input("Enter your name ","Type here ...")
st.sidebar.text_input("Enter your Email ","Type here ...")
st.sidebar.date_input("Enter your DOB ","Type here ...")
st.sidebar.number_input("Enter your Mobile Number","Type here ...")
st.sidebar.radio("Select your Gender",["Male","Female","Others"])
if st.button("Submit"):
    name=s.title()
    st.subheader("Hello, "name" !")
    st.success("Your details submited successfully")
