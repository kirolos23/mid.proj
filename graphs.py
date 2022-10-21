import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import plotly.figure_factory as fig

df = pd.read_csv ('hotel_booking.csv')

st.write('Relation between adults count and their country')
df1 =px.histogram(df , x= 'country', y='adults')
df1


st.write('the counts cancelation and Month')
df2 =px.histogram(df , x= 'arrival_date_month', y='is_canceled')
df2


df6 = px.histogram(df , x= 'reservation_status', y='stays_in_week_nights')
df6


df9 = px.histogram(df , x= 'customer_type', y='total_of_special_requests' )
df9

df10 = px.scatter(df, x = 'total_of_special_requests' ,y =  'adults')
df10
