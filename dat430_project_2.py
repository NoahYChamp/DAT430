import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/NoahYChamp/DAT430/main/motor_vehicle_data.csv')
data['Year'] = data['Year'].astype(str).str.replace(',', '')

st.title('DAT430 Project 2 Streamlit')
st.write('By Noah Youngren.')
st.write('Fundamental Research Question: Has the amount of motor vehicle crash fatalities increased or decreased over time? Which groups are most affected?')


def navigation_menu():
    options = ['Total Fatalities by Year', 'Fatalities by Year Breakdown', 'Another Chart']
    selection = st.sidebar.radio('Select a chart:', options)

    return selection

def main():
    st.sidebar.title('Navigation')
    selection = navigation_menu()

    if selection == 'Fatalities over Time':
        chart = fatalities_over_time()
        st.altair_chart(chart, use_container_width=True)

    elif selection == 'Fatalities by Position':
        chart = fatalities_by_position()
        st.altair_chart(chart, use_container_width=True)

    elif selection == 'Another Chart':
        pass

def fatalities_over_time():
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


main()
