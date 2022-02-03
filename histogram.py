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
size = st.sidebar.slider('N', min_value=1000, max_value=10000, value=5000, step=500)

array = np.random.normal(mean, sd, size)
bins = np.arange(array.min(), array.max()+step, step)

fig = plt.figure(figsize=(8, 5))
plt.hist(array, bins)
st.pyplot(fig)
