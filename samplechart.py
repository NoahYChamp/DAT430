# -*- coding: utf-8 -*-
"""SampleChart.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mOh3uRmqBFdF2Ppy79W8LAe_g5jozevL
"""

import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

Low = 100
High = 100000

# Compute x^2 + y^2 across a 2D grid
x, y = np.meshgrid(range(Low, High, 5000), range(100, 0, -10))
z = x * y

# Convert this grid to columnar data expected by Altair
model = pd.DataFrame({'x': x.ravel(),
                     'y': y.ravel(),
                     'z': z.ravel()})

Chart = alt.Chart(model).mark_rect().encode(
    x='x:O',
    y='y:O',
    color='z:R',
    tooltip='z:Q'
)

st.altair_chart(Chart, use_container_width=True)
