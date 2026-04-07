"""
widget.py

Examples of common Streamlit input widgets: `st.text_input`, `st.slider`,
`st.selectbox`, and `st.file_uploader`. Shows how to read values and display
results conditionally.
"""

import streamlit as st 
import pandas as pd

st.title("Streamlit Text Input and Widgets")

# Text input returns a string; empty string when nothing entered
name = st.text_input("Enter your name:")

# Slider returns a number; arguments are (label, min, max, default)
age = st.slider("Select your age:", 0, 100, 25)

# Selectbox shows a dropdown and returns the selected option
options = ["Python", "C++", "GoLang", "Java"]
choice = st.selectbox("Choose your favorite programming language:", options)


# Display results only when inputs are present. Because Streamlit reruns
# the script on each interaction, outputs update automatically.
if name and age is not None:
    st.write(f"Hello, {name}! Your age is {age}.")

if choice:
    st.write(f"Your favorite programming language is {choice}.")


# File uploader returns a file-like object (or None). You can read it directly
# with pandas if it's a CSV. This is useful for interactive demos.
uploaded_file = st.file_uploader("Choose a csv file", type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

# Note: For more complex apps, consider using `st.session_state` to persist
# small pieces of information across reruns (e.g., counters, form values).
