import os
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import plotly.figure_factory as fig
from PIL import Image
df = pd.read_csv ('hotel_booking.csv')

image = Image.open('ezgif.com-gif-maker.jpg')
st.image(image, caption='Booking Hotel')


df3 = df['arrival_date_month'].min()
st.title('The Lowest Arrival Date Month') 
df3
df4 = df['arrival_date_month'].max()
st.title('The Highest Arrival Date Month') 
df4

df5 =df['customer_type'].unique().T
st.title('Customer Type ')
st.write(df5)



df7 = df.groupby('arrival_date_year')['arrival_date_month'].max()
st.title('Highest Month of Year')
df7

df8 = df.groupby('arrival_date_year')['arrival_date_month'].min()
st.title('Lowest Months of Year')
df8

