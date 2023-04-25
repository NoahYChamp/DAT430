import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/NoahYChamp/DAT430/main/motor_vehicle_data.csv')

st.title('Project 2')
st.header('This is the Streamlit for DAT430 Project 2')

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
  Chart1 = alt.Chart(model).mark_rect().encode(
      x='x:O',
      y='y:O',
      color='y:Q',
      tooltip='z:Q'
  ).properties(
      title='Chart 1'
  )

  st.altair_chart(Chart1, use_container_width=True)
  
  Chart2 = alt.Chart(model).mark_rect().encode(
      x='x:O',
      y='y:O',
      color='y:Q',
      tooltip='z:Q'
  )

  st.altair_chart(Chart2, use_container_width=True)

with col2:
  Chart3 = alt.Chart(model).mark_rect().encode(
      x='x:O',
      y='y:O',
      color='y:Q',
      tooltip='z:Q'
  )

  st.altair_chart(Chart3, use_container_width=True)

  Chart4 = alt.Chart(model).mark_rect().encode(
      x='x:O',
      y='y:O',
      color='y:Q',
      tooltip='z:Q'
  )

  st.altair_chart(Chart4, use_container_width=True)