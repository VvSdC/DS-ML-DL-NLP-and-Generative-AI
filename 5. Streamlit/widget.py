import streamlit as st 
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name: ")
age = st.slider("Select your age: ",0,100,25)

options = ["Python","C++","GoLang","Java"]
choice = st.selectbox("Choose your favorite programming language: ",options)


if name and age:
    st.write(f"Hello, {name}!! Your age is {age}")

if choice:
    st.write(f"You favorite programming language is {choice}")

uploaded_file = st.file_uploader("Choose a csv file",type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
