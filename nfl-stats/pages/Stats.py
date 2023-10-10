import streamlit as st
import pandas as pd

st.set_page_config(
  page_title="Stats",
  layout="wide"
)

st.header("Player Statistics 📈", anchor=False)

df = st.session_state["data"]

# Selectbox creation - Season
seasons = sorted(df["Season"].unique(), reverse=True)
season_selectbox = st.sidebar.multiselect("Season", seasons)

# Selectbox creation - Teams
teams = sorted(df["Team"].unique())
team_selectbox = st.sidebar.multiselect("Team", teams)

# Selectbox creation - Positions
positions = sorted(df["Position"].unique())
position_selectbox = st.sidebar.multiselect("Position", positions)

# Selectbox creation - Player
index = sorted(df.index.unique(), reverse=False)
player_selectbox = st.sidebar.multiselect("Player", index)

df_filtered = df
# Output
if len(season_selectbox) > 0:
  df_filtered = df_filtered[df_filtered["Season"].isin(season_selectbox)]
if len(team_selectbox)  > 0:        
  df_filtered = df_filtered[df_filtered["Team"].isin(team_selectbox)]
if len(position_selectbox) > 0:
  df_filtered = df_filtered[df_filtered["Position"].isin(position_selectbox)]
if len(player_selectbox) > 0:
  df_filtered = df_filtered.loc[player_selectbox]

st.dataframe(df_filtered)