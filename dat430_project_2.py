import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

ata = pd.read_csv('https://raw.githubusercontent.com/NoahYChamp/DAT430/main/motor_vehicle_data.csv')
data['Year'] = data['Year'].astype(str).str.replace(',', '')

st.title('DAT430 Project 2 Streamlit')
st.write('By Noah Youngren.')
st.write('Fundamental Research Question: Has the amount of motor vehicle crash fatalities increased or decreased over time? Which groups are most affected?')

def fatalities_over_time():
    st.header('Total Fatalities by Year')
    chart = alt.Chart(data).mark_line().encode(
        x='Year',
        y='Total Fatalities'
    )
    return chart

def fatalities_by_position():
  fatalities_data = data.groupby('Year')[['Driver Fatalities', 'Passenger Fatalities', 'Unknown Occupant Fatalities']].sum().reset_index()
  fatalities_data = pd.melt(fatalities_data, id_vars=['Year'], var_name='Occupant Type', value_name='Fatalities')

  chart = alt.Chart(fatalities_data).mark_bar().encode(
      x='Year',
      y='Fatalities',
      color='Occupant Type'
    )
  return chart

chartnum = st.radio(
    'Select chart:',
    ('Chart1', 'Chart2', 'Chart3'))
if chartnum == 'Chart1':
    chart = fatalities_over_time()
    st.altair_chart(chart, use_container_width=True)
elif chartnum == 'Chart2:
    chart = fatalities_by_position()
    st.altair_chart(chart, use_container_width=True)
