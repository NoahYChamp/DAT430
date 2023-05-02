import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/NoahYChamp/DAT430/main/motor_vehicle_data.csv')
data['Year'] = data['Year'].astype(str).str.replace(',', '')

st.title('DAT430 Project 2 Streamlit')
st.write('By Noah Youngren.')

'''
st.write('This is a description of your fundamental research question and its context.')

st.header('Header')
'''
#st.sidebar.write("Sidebar text goes here. Lorem ipsum and all that.")
#st.sidebar.button('This is a button.')

'''
#column setter
col1, col2 = st.columns(2)

with col1:
  fatal_crashes_over_time = alt.Chart(data).mark_bar().encode(
      x='Year',
      y='Fatal Crashes'
  )
  st.altair_chart(fatal_crashes_over_time)
  
with col2:
  fatalities_data = data.groupby('Year')[['Driver Fatalities', 'Passenger Fatalities', 'Unknown Occupant Fatalities']].sum().reset_index()
  fatalities_data = pd.melt(fatalities_data, id_vars=['Year'], var_name='Occupant Type', value_name='Fatalities')
  stacked_fatalities_chart = alt.Chart(fatalities_data).mark_bar().encode(
      x='Year',
      y='Fatalities',
      color='Occupant Type'
  )

  st.altair_chart(stacked_fatalities_chart, use_container_width=True)
'''
def navigation_menu():
    options = ['Fatalities by Year', 'Your Next Chart', 'Another Chart']
    selection = st.sidebar.radio('Select a chart:', options)

    return selection

def fatalities_by_position_chart():
  fatalities_data = data.groupby('Year')[['Driver Fatalities', 'Passenger Fatalities', 'Unknown Occupant Fatalities']].sum().reset_index()
  fatalities_data = pd.melt(fatalities_data, id_vars=['Year'], var_name='Occupant Type', value_name='Fatalities')

  chart = alt.Chart(fatalities_data).mark_bar().encode(
      x='Year',
      y='Fatalities',
      color='Occupant Type'
    )
  return chart

def main():
    st.sidebar.title('Navigation')
    selection = navigation_menu()

    if selection == 'Fatalities by Year':
        chart = fatalities_by_year_chart()
        st.altair_chart(chart, use_container_width=True)

    elif selection == 'Your Next Chart':
        pass

    elif selection == 'Another Chart':
        pass

main()
