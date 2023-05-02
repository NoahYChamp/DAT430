import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
from streamlit import caching

# Set up caching so the app doesn't run unnecessarily
@st.cache(allow_output_mutation=True)
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/NoahYChamp/DAT430/main/motor_vehicle_data.csv')
    return data

data = load_data()

# Initialize session state
if 'selection' not in st.session_state:
    st.session_state.selection = 'Fatalities by Year'

def navigation_menu():
    options = ['Fatalities by Year', 'Total Fatalities by Year', 'Your Next Chart', 'Another Chart']
    selection = st.sidebar.radio('Select a chart:', options, key='radio')

    if selection != st.session_state.selection:
        st.session_state.selection = selection
        caching.clear_cache()

    return selection

def main():
    st.sidebar.title('Navigation')
    selection = navigation_menu()

    if selection == 'Fatalities by Year':
        chart = fatalities_by_year_chart()
        st.altair_chart(chart, use_container_width=True)

    elif selection == 'Total Fatalities by Year':
        chart = total_fatalities_by_year_chart()
        st.altair_chart(chart, use_container_width=True)

    elif selection == 'Your Next Chart':
        # call function to display your next chart here

    elif selection == 'Another Chart':
        # call function to display another chart here

def fatalities_by_year_chart():
    fatalities_data = data.groupby('Year')[['Driver Fatalities', 'Passenger Fatalities', 'Unknown Occupant Fatalities']].sum().reset_index().melt(id_vars=['Year'], var_name='Type of Occupant', value_name='Number of Fatalities')

    chart = alt.Chart(fatalities_data).mark_bar().encode(
        x='Year',
        y='Number of Fatalities',
        color='Type of Occupant'
    ).properties(
        width=600,
        height=400,
        title='Fatalities by Year'
    )

    return chart

def total_fatalities_by_year_chart():
    total_fatalities_data = data.groupby('Year')[['Total Fatalities']].sum().reset_index()

    chart = alt.Chart(total_fatalities_data).mark_line().encode(
        x='Year',
        y='Total Fatalities'
    ).properties(
        width=600,
        height=400,
        title='Total Fatalities by Year'
    )

    return chart

if __name__ == '__main__':
    main()
