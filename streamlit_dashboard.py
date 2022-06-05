from encodings import utf_8
from pickletools import decimalnl_long
from unicodedata import decimal
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np


st.set_page_config(page_title="The FWM Dashboard", page_icon="🌐", layout="wide")
data = 'Data_For_Change_Clean_Version.xlsx'
df = pd.read_excel(data)

#----side bar----#

st.sidebar.header("Please select a Theme")
Event_theme = st.sidebar.selectbox(
    "Select an theme",
    df["Event_Theme"].unique(),
    
)
st.sidebar.header("Please select an actor")
actors = st.sidebar.multiselect(
    "Select an actor",
    df["Actors"].unique(),
    default= df["Actors"].unique()
)

#filter by actors and event theme
df_selection = df.query(
     'Event_Theme ==@Event_theme& Actors == @actors '
)

#----main page----#
st.title(":bar_chart:Data For Change")
st.markdown('---')

#----plotly chart----#
fig_national = px.bar(df_selection['National Event'], orientation='h')

fig_national.update_layout(
    title_text="National Event",
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis = (dict(showgrid=False)),
    
)

fig_events = px.bar(df_selection['Event Place'], orientation='h')

fig_events.update_layout(
    title_text="Event place",
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis = (dict(showgrid=False)),)

fig_location = px.bar(df_selection['Location Type'], orientation='h')
fig_location.update_layout(
    title_text="Location Type",
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis = (dict(showgrid=False)),)

fig_state = px.bar(df_selection['Internal/State'], orientation='h')   
fig_state.update_layout(
    title_text="Internal/State",
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis = (dict(showgrid=False)),)


col1, col2 = st.columns((2,2))
col1.subheader("National Event")
col1.plotly_chart(fig_national, use_container_width=True)
col2.subheader("Event Place")
col2.plotly_chart(fig_events, use_container_width=True)

col3, col4 = st.columns((2,2))
col3.subheader("location of Event")
col3.plotly_chart(fig_location, use_container_width=True)
col4.subheader("Internal/State")
col4.plotly_chart(fig_state, use_container_width=True)


map_df = df_selection[['index','latitude', 'longitude']]
map_df = map_df.dropna()

map_df['latitude'] = map_df['latitude'].astype(float)
map_df['longitude'] = map_df['longitude'].astype(float)

st.map(map_df)

