"""
streamlit.py

Minimal Streamlit example showing basic display primitives: title, text,
dataframe display, and a simple line chart.

Concepts:
- `st.title`, `st.write` for text and markdown
- Displaying DataFrames directly with `st.write` or specialized chart helpers
"""

import streamlit as st
import pandas as pd 
import numpy as np 

# Title of the application shown at the top
st.title("This is a basic Streamlit application")

# Display a simple text message; `st.write` is flexible and can render
# strings, dataframes, matplotlib/plotly objects, and more.
st.write("This is a simple text")

# Creating and displaying a simple dataframe. Streamlit will render it nicely.
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write("Here is the simple dataframe")
st.write(df)


# Creating a line chart from random data. Streamlit provides quick charting
# helpers like `st.line_chart`, `st.area_chart`, and `st.bar_chart`.
chart_data = pd.DataFrame(
    np.random.randn(20, 4), columns=['a', 'b', 'c', 'd']
)
st.line_chart(chart_data)