# -*- coding: utf-8 -*-
"""titanic data streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BOLwhZMsL4qpVeZ-TjGweqPV0ueGFm8Y
"""

import pandas as pd
import altair as alt
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

#data.describe()
st.set_page_config(page_title='Titanic Data', layout='centered', initial_sidebar_state='collapsed')

col1, col2, col3 = st.columns(3)

with col1:
#chart 1
  hist_age = alt.Chart(data).mark_bar().encode(
      alt.X('Age:Q', bin=True),
      y='count()'
  )
  st.altair_chart(hist_age)

with col2:
#chart 2
  scatter = alt.Chart(data).mark_circle().encode(
      x = 'Fare',
      y = 'Age',
      color = 'Survived',
      tooltip = ['Age', 'Fare', 'Survived', 'Name']
  )
  st.altair_chart(scatter)

with col3:
#chart 3
  hist_fare = alt.Chart(data).mark_bar().encode(
      alt.X('Fare:Q', bin=True),
      y='count()'
  ).interactive()
  st.altair_chart(hist_fare)
