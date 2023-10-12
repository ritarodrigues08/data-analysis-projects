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
position_selectbox = st.sidebar.multiselect("Position", df["Position"].unique())
df_qb = ['Position', 'Team', 'Season', 'Completions', 'Attempts', 'Passing_Yards','Passing_Tds','Interceptions','Sacks', 'Comp_Percentage', 'Pass_Td_Percentage', 'Int_Percentage', 'Total_Tds', 'Td_Percentage', 'Pass_Ypg']
df_rb = ['Position', 'Team', 'Season', 'Carries', 'Rushing_Yards', 'Rushing_Tds', 'Rushing_Fumbles', 'Receptions', 'Targets', 'Receiving_Yards', 'Receiving_Tds', 'Receiving_Fumbles', 'Rush_Td_Percentage', 'Rec_Td_Percentage', 'Total_Tds', 'Rush_Ypg', 'Rec_Ypg']
df_wr = ['Position', 'Team', 'Season', 'Carries', 'Receptions', 'Targets', 'Receiving_Yards', 'Receiving_Tds', 'Receiving_Fumbles', 'Rec_Td_Percentage', 'Total_Tds', 'Rec_Ypg']
df_te = ['Position', 'Team', 'Season', 'Carries', 'Receptions', 'Targets', 'Receiving_Yards', 'Receiving_Tds', 'Receiving_Fumbles', 'Rec_Td_Percentage', 'Total_Tds', 'Rec_Ypg']

# Selectbox creation - Player
index = sorted(df.index.unique(), reverse=False)
player_selectbox = st.sidebar.multiselect("Player", index)

df_filtered = df

# Output
if len(season_selectbox) > 0:
  df_filtered = df_filtered[df_filtered["Season"].isin(season_selectbox)]
if len(team_selectbox)  > 0:        
  df_filtered = df_filtered[df_filtered["Team"].isin(team_selectbox)]
if len(player_selectbox) > 0:
  df_filtered = df_filtered.loc[player_selectbox]
if "QB" in position_selectbox:
  df_filtered = df_filtered[df_filtered["Position"].isin(position_selectbox)]
  st.dataframe(df_filtered[df_qb])
elif "RB" in position_selectbox:
  df_filtered = df_filtered[df_filtered["Position"].isin(position_selectbox)]
  st.dataframe(df_filtered[df_rb])
elif "WR" in position_selectbox:
  df_filtered = df_filtered[df_filtered["Position"].isin(position_selectbox)]
  st.dataframe(df_filtered[df_wr])
elif "TE" in position_selectbox:
  df_filtered = df_filtered[df_filtered["Position"].isin(position_selectbox)]
  st.dataframe(df_filtered[df_te])
else:
  st.dataframe(df_filtered)
  