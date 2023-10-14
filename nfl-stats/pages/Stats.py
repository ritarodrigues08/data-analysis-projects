import streamlit as st
import pandas as pd

st.set_page_config(
  page_title="Stats",
  layout='wide'
)


st.header("Player Statistics 📈", anchor=False)
st.markdown(
  '''
  Please follow these instructions for a better use of the filters:
  * The data that is shown for the QB, RB, WR and TE positions is different for each one of them
  * First, select the position you want to visualize
  * Then, select da season and/or the team
  ''')

df = st.session_state["data"]


# Selectbox creation - Positions
position_selectbox = st.sidebar.multiselect("Position", df["Position"].unique())
df_qb = ['Position', 'Team', 'Season', 'Completions', 'Attempts', 'Passing_Yards','Passing_Tds','Interceptions','Sacks', 'Comp_Percentage', 'Pass_Td_Percentage', 'Int_Percentage', 'Total_Tds', 'Td_Percentage', 'Pass_Ypg']
df_rb = ['Position', 'Team', 'Season', 'Carries', 'Rushing_Yards', 'Rushing_Tds', 'Rushing_Fumbles', 'Receptions', 'Targets', 'Receiving_Yards', 'Receiving_Tds', 'Receiving_Fumbles', 'Rush_Td_Percentage', 'Rec_Td_Percentage', 'Total_Tds', 'Rush_Ypg', 'Rec_Ypg']
df_wr = ['Position', 'Team', 'Season', 'Carries', 'Receptions', 'Targets', 'Receiving_Yards', 'Receiving_Tds', 'Receiving_Fumbles', 'Rec_Td_Percentage', 'Total_Tds', 'Rec_Ypg']
df_te = ['Position', 'Team', 'Season', 'Carries', 'Receptions', 'Targets', 'Receiving_Yards', 'Receiving_Tds', 'Receiving_Fumbles', 'Rec_Td_Percentage', 'Total_Tds', 'Rec_Ypg']

# Selectbox creation - Season
seasons = sorted(df["Season"].unique(), reverse=True)
season_selectbox = st.sidebar.multiselect("Season", seasons)

# Selectbox creation - Teams
teams = sorted(df["Team"].unique())
team_selectbox = st.sidebar.multiselect("Team", teams)


df_filtered = df

# Output
if len(season_selectbox) > 0:
  df_filtered = df_filtered[df_filtered["Season"].isin(season_selectbox)]
if len(team_selectbox)  > 0:        
  df_filtered = df_filtered[df_filtered["Team"].isin(team_selectbox)]
if "QB" in position_selectbox:
  df_filtered = df_filtered[df_filtered["Position"].isin(position_selectbox)]
  st.dataframe(df_filtered[df_qb])
  col1, col2, col3 = st.columns(3)
  col1.markdown(
    '''
    **Info**:
    * Position
    * Team
    * Season
    * Completions
    * Attempts
    ''')
  col2.markdown(
    '''
    &nbsp;
    * Passing_Yards
    * Passing_Tds
    * Interceptions
    * Sacks 
    * Comp_Percentage (Completition percentage)
    '''
  )
  col3.markdown(
    '''
    &nbsp;
    * Pass_Td_Percentage
    * Int_Percentage (Interception percentation)
    * Total_Tds
    * Td_Percentage
    * Pass_Ypg (Passing yards per game)
    '''
  )
elif "RB" in position_selectbox:
  df_filtered = df_filtered[df_filtered["Position"].isin(position_selectbox)]
  st.dataframe(df_filtered[df_rb])
  col1, col2, col3 = st.columns(3)
  col1.markdown(
    '''
    **Info**:
    * Position
    * Team
    * Season
    * Carries
    * Rushing_Yards
    * Rushing_Tds
    '''
  )
  col2.markdown(
    '''
    &nbsp;
    * Rushing_Fumbles
    * Receptions
    * Targets
    * Receiving_Yards
    * Receiving_Tds
    * Receiving_Fumbles
    '''
  )
  col3.markdown(
    '''
    &nbsp;
    * Rush_Td_Percentage
    * Rec_Td_Percentage
    * Total_Tds
    * Rush_Ypg (Rush yards per game)
    * Rec_Ypg (Receiving yards per game)
    '''
  )
elif "WR" in position_selectbox:
  df_filtered = df_filtered[df_filtered["Position"].isin(position_selectbox)]
  st.dataframe(df_filtered[df_wr])
  col1, col2, col3 = st.columns(3)
  col1.markdown(
    '''
    **Info:**
    * Position
    * Team
    * Season
    * Carries
    '''
  )
  col2.markdown(
    '''
    &nbsp;
    * Receptions
    * Targets
    * Receiving_Yards
    * Receiving_Tds
    '''
  )
  col3.markdown(
    '''
    &nbsp;
    * Receiving_Fumbles
    * Rec_Td_Percentage
    * Total_Tds
    * Rec_Ypg (Receiving yards per game)
    '''
  )
elif "TE" in position_selectbox:
  df_filtered = df_filtered[df_filtered["Position"].isin(position_selectbox)]
  st.dataframe(df_filtered[df_te])
  col1, col2, col3 = st.columns(3)
  col1.markdown(
    '''
    **Info:**
    * Position
    * Team
    * Season
    * Carries
    '''
  )
  col2.markdown(
    '''
    &nbsp;
    * Receptions
    * Targets
    * Receiving_Yards
    * Receiving_Tds
    '''
  )
  col3.markdown(
    '''
    &nbsp;
    * Receiving_Fumbles
    * Rec_Td_Percentage
    * Total_Tds
    * Rec_Ypg (Receiving yards per game)
    '''
  )
else:
  st.dataframe(df_filtered)
  