"""
classification.py

Simple Streamlit demo showing how to load data, cache it, collect user input
from the sidebar, train a small sklearn model, and show predictions.

Concepts demonstrated:
- `@st.cache_data` to cache loaded data across reruns
- `st.sidebar` for inputs
- Model training / prediction and displaying results with `st.write`
"""

import streamlit as st 
import pandas as pd 
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


# Cache loading the dataset so the expensive I/O / construction is not repeated
# on every user interaction. Use @st.cache_data for pure data (no resources).
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    # add a target column with integer labels
    df['species'] = iris.target 
    return df, iris.target_names


# Load (cached) data and target name mapping
df, target_names = load_data()


# Train a tiny model. For a real app you would load a pre-trained model
# from disk (and cache that load) instead of retraining on every start.
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])


# --- Sidebar inputs: use the sidebar to collect feature values from the user
st.sidebar.title("Input features")
sepal_length = st.sidebar.slider(
    "Sepal length",
    float(df['sepal length (cm)'].min()),
    float(df['sepal length (cm)'].max()),
)
sepal_width = st.sidebar.slider(
    "Sepal width",
    float(df['sepal width (cm)'].min()),
    float(df['sepal width (cm)'].max()),
)
petal_length = st.sidebar.slider(
    "Petal length",
    float(df['petal length (cm)'].min()),
    float(df['petal length (cm)'].max()),
)
petal_width = st.sidebar.slider(
    "Petal width",
    float(df['petal width (cm)'].min()),
    float(df['petal width (cm)'].max()),
)


# Prepare input and run prediction. Streamlit reruns the script when inputs change,
# so prediction will update automatically when sliders move.
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# Prediction
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]

st.write("## Prediction")
st.write(f"The predicted species is: {predicted_species}")