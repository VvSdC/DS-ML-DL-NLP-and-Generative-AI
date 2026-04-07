import streamlit as st
import pandas as pd 
import numpy as np 

# Title of the applicatiom
st.title("This is a basic streamlit application")

# Display a simple text
st.write("This is a simple text")

# Creating and displaying a simple dataframe
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})
st.write("Here is the simple dataframe")
st.write(df)


# Creating a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,4),columns=['a','b','c','d']
)
st.line_chart(chart_data)