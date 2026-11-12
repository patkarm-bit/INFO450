

import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('Lesson_24/Advertising_F.csv')
st.title("Advertising Effectiveness Manas")

st.sidebar.header("Filters")
x_var = st.selectbox("X axis", ["TV", "radio", "newspaper"])
y_var = st.selectbox("Y axis", ["TV", "radio", "newspaper"])

# Show scatterplot
fig = px.scatter(df, x=x_var, y=y_var,
                 labels={'TV': 'TV ad spend', 'radio': 'Radio ad spend'})
st.plotly_chart(fig)

# Show the barplot
sales_per_city = df.groupby('City')['sales'].sum().reset_index()
fig = px.bar(sales_per_city, x='City', y='sales', title="data is fun")
st.plotly_chart(fig)

# Show the dataframe
st.dataframe(df)

