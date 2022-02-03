"""To provide a variable input for users to develop parameters for a
visualized histogram
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.write('Change the inputs in the sidebar to change the output of the plot')

step = st.sidebar.slider('Step', min_value=1, max_value=10, value=5, step=1)
mean = st.sidebar.slider('Mean of Distribution', min_value=100, max_value=200, value=100, step=5)
sd = st.sidebar.slider('sd of Distribution', min_value=1, max_value=5, value=2, step=1)
