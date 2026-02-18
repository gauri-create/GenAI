import streamlit as st

st.header("Gimsee")
st.text_area("write something")
st.text_input("Your Name")

st.radio("Your branch", ["CSE", "AIML", "ECE"])
img_upload=st.file_uploader("Image", type=["jpg","png","jpeg"])
if st.button("Click"):
    st.success("welcome")

API_KEY="AIzaSyDJy1zxO7kmg-RWOFRiM8cQo_8vKz2cnL8"

