import streamlit as st
import pandas as pd

st.set_page_config(
  page_title="Stats",
  layout="wide"
)

st.header("Player Statistics 📈", anchor=False)

df = st.session_state["data"]

# Selectbox creation - Season
seasons = df["Season"].sort_values(ascending=False).unique()
season_selectbox = st.sidebar.selectbox("Season", seasons)

# Selectbox creation - Teams
teams = df["Team"].sort_values().unique()
team_selectbox = st.sidebar.selectbox("Team", teams)

# Output
df_filtered = df[df["Season"] == season_selectbox].set_index("Name")
df_filtered = df_filtered[df_filtered["Team"] == team_selectbox]
st.dataframe(df_filtered, height=500)

#df

