import streamlit as st
import pandas as pd
import altair as alt
import json

# Sample patient data in JSON format
data_json = '''
[
    {"name": "John Doe", "age": 25, "gender": "Male"},
    {"name": "Jane Smith", "age": 34, "gender": "Female"},
    {"name": "Alice Johnson", "age": 29, "gender": "Female"},
    {"name": "Bob Brown", "age": 45, "gender": "Male"}
]
'''

# Convert JSON to DataFrame
data = pd.read_json(data_json)

# Streamlit application title
st.title('Patient Data Visualization')

# Display the data as a table in Streamlit
st.write("### Raw Data", data)

# Creating a histogram of age distribution
chart = alt.Chart(data).mark_bar().encode(
    alt.X("age:Q", bin=True, title="Age"),
    alt.Y('count()', title="Number of Patients"),
    color='gender:N'
).properties(
    width=600,
    height=400
)

# Display the chart in Streamlit
st.write("### Age Distribution by Gender", chart)
