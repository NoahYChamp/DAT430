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
  'Select chart findings:',
      ('Fatal Crashes Findings', 'Occupant Fatalities Findings', 'Per Registered Driver Findings'))
  if chartnum == 'Fatal Crashes Findings':
      st.write('The number of fatal crashes remains relatively the same, but beginning at 2007 takes a notable downturn for about 5 years. This coincides with the Great Recession.')
  elif chartnum == 'Occupant Fatalities Findings':
      st.write('Drivers make up the majority of vehicular occupant fatalities, but this chart also notes a drop in deaths, beginning close to 2007 as well. However, the drop in passenger fatalities is not proportionate to the drop in driver deaths. This may suggest more people drove alone in this time, or were alone when engaging in risky behavior behind the wheel. ')
  elif chartnum == 'Per Registered Driver Findings':
      st.write("The 2007 drop is noticeable in this graph as well. Considering that new, teenage drivers are some of the most accident-prone, this could suggest that less teenagers were behind the wheel during the recession.")
