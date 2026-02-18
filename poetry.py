import streamlit as st
import pandas as pd 
import time
from google import genai

def write_poem(prompt):
    if prompt:
        msg = st.toast("Analyzing...")
        time.sleep(2)
        msg = st.toast("Writing for you!")
        time.sleep(2)
        msg = st.toast("Ready!", icon="🥞")
        time.sleep(2)
        st.write(f"So you want to write {prompt} today.")
        time.sleep(1)
        st.write("Let's see how it will look.")
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=f"Write poem on {prompt}")
        st.write(response.text)

# a function to pull up images goes here
# I will write this function later 

if __name__=="__main__":
    API_KEY = "AIzaSyDJy1zxO7kmg-RWOFRiM8cQo_8vKz2cnL8"   # YOUR API
    # initialize the client
    client = genai.Client(api_key=API_KEY)
    # title 
    st.title("Poetry Generator")
    prompt = st.chat_input("What's idea?")
    write_poem(prompt)