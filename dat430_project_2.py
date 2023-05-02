import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/NoahYChamp/DAT430/main/motor_vehicle_data.csv')
data['Year'] = data['Year'].astype(str)

st.title('DAT430 Project 2 Streamlit')
st.write('By Noah Youngren.')
st.write('Fundamental Research Question: Has the amount of motor vehicle crash fatalities increased or decreased over time? Which groups are most affected?')

#st.sidebar.write("Sidebar text goes here. Lorem ipsum and all that.")
#st.sidebar.button('This is a button.')

#column setter
col1, col2 = st.columns(2)

with col1:
  fatal_crashes_over_time = alt.Chart(data).mark_bar().encode(
      x='Year',
      y='Fatal Crashes'
  )
  st.altair_chart(fatal_crashes_over_time)
  
  fatalities_data = data.groupby('Year')[['Driver Fatalities', 'Passenger Fatalities', 'Unknown Occupant Fatalities']].sum().reset_index()
  fatalities_data = pd.melt(fatalities_data, id_vars=['Year'], var_name='Occupant Type', value_name='Fatalities')
  stacked_fatalities_chart = alt.Chart(fatalities_data).mark_bar().encode(
      x='Year',
      y='Fatalities',
      color='Occupant Type'
  )
  st.altair_chart(stacked_fatalities_chart, use_container_width=True)

with col2:
  registered_drivers_per_fatality = alt.Chart(data).mark_bar(color='red').encode(
      x='Year',
      y='Fatalities per 100,000 Licensed Drivers',
      tooltip=['Total Overall Fatalities', 'Fatal Crashes']
  )
  st.altair_chart(registered_drivers_per_fatality)
  
  
  chartnum = st.radio(
  'Select chart:',
      ('Chart1', 'Chart2', 'Chart3'))
  if chartnum == 'Chart1':
      st.write('You selected Chart1.')
  elif chartnum == 'Chart2':
      st.write('You pressed Chart2.\n
               Nothing happened.')
  elif chartnum == 'Chart2':
      st.write("None of these buttons work sadly. I am lowkey malding rn.")
