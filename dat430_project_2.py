import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/NoahYChamp/DAT430/main/motor_vehicle_data.csv')
data['Year'] = data['Year'].astype(str).str.replace(',', '')

st.title('DAT430 Project 2 Streamlit')
st.write('By Noah Youngren.')

st.write('This is a description of your fundamental research question and its context.')

st.header('Header')

st.sidebar.write("Sidebar text goes here. Lorem ipsum and all that.")
st.sidebar.button('This is a button.')

#column setter
col1, col2 = st.columns(2)

#sample data
Low = 100
High = 100000

# Compute x^2 + y^2 across a 2D grid
x, y = np.meshgrid(range(Low, High, 5000), range(100, 0, -10))
z = x * y

# Convert this grid to columnar data expected by Altair
model = pd.DataFrame({'x': x.ravel(),
                     'y': y.ravel(),
                     'z': z.ravel()})

with col1:
   fatal_crashes_over_time = alt.Chart(data).mark_bar().encode(
      x='Year',
      y='Fatal Crashes'
  )
  st.altair_chart(fatal_crashes_over_time)
