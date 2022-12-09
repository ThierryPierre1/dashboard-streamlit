import streamlit as st
import pandas as pd
import numpy as np 
import warnings
warnings.filterwarnings('ignore')

# Load data
device = pd.read_csv("DataSets/deviceState.csv")
screentime = pd.read_csv("DataSets/ScreenTime.csv")

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

device.head(50)
device2 = device.head(50)

screentime.head(50)
screentime2 = screentime.head(50)

# Battery Analysis

st.title("Battery Data Analysis")

st.table(device2)

# Displaying the bar chart
st.subheader('Battery Level')
battery = device2['battery_level'].value_counts()
st.bar_chart(battery)

# ScreenTime Analysis

st.title("Screem Time Analysis")

st.table(screentime)

# Displaying the line chart
st.subheader('Elapsed Time')
time = screentime['Elapsed Time In Minutes'].value_counts()
st.line_chart(time)

