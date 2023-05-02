import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/NoahYChamp/DAT430/main/motor_vehicle_data.csv')

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
      y='Fatalities'
  )
  st.altair_chart(stacked_fatalities_chart, use_container_width=True)

with col2:
  non_occupant_data = data[['Year', 'Motorcyclists', 'Pedestrian Fatalities', 'Pedacyclist Fatalities', 'Other / Unknown Fatalities']]
  non_occupant_data = non_occupant_data.groupby('Year').sum().reset_index()
  non_occupant_data = pd.melt(non_occupant_data, id_vars=['Year'], var_name='Fatalities Type', value_name='Fatalities')
  line_chart = alt.Chart(non_occupant_data).mark_line().encode(
      x='Year',
      y='Fatalities',
      color='Fatalities Type'
  )
  st.altair_chart(line_chart, use_container_width=True)
