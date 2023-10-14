import streamlit as st
import pandas as pd
import webbrowser

st.set_page_config(
  page_title="About"
)

if "data" not in st.session_state:
  df = pd.read_csv(r"C:\Users\anagr\Documentos\projects-github\data-analysis-projects\nfl-stats\yearly_data.csv", index_col=0)
  df.columns = df.columns.str.title()
  df = df.set_index("Name")
  df = df.sort_values(by="Season", ascending=False)
  df = df[['Position', 'Team', 'Season', 'Completions', 'Attempts', 'Passing_Yards', 'Passing_Tds', 'Interceptions', 'Sacks', 'Carries', 'Rushing_Yards', 'Rushing_Tds', 'Rushing_Fumbles', 'Receptions', 'Targets', 'Receiving_Yards', 'Receiving_Tds', 'Receiving_Fumbles', 'Comp_Percentage', 'Pass_Td_Percentage', 'Int_Percentage', 'Rush_Td_Percentage', 'Rec_Td_Percentage', 'Total_Tds', 'Td_Percentage', 'Pass_Ypg', 'Rush_Ypg', 'Rec_Ypg']]
  columns_percentage = ['Comp_Percentage', 'Pass_Td_Percentage', 'Int_Percentage', 'Rush_Td_Percentage', 'Rec_Td_Percentage', 'Td_Percentage']
  for columns in columns_percentage:
    df[columns] = df[columns].apply(lambda x: f'{x:.2%}')
    columns_integer = ["Season", "Passing_Yards", "Rushing_Yards", "Receiving_Yards"]
  for columns in columns_integer:
    df[columns] = df[columns].apply(lambda x: f'{int(x):d}')
    columns_decimals = ['Pass_Ypg', 'Rush_Ypg', 'Rec_Ypg']
  for columns in columns_decimals:
    df[columns] = df[columns].apply(lambda x: f'{x:.1f}')
    st.session_state["data"] = df

st.title("NFL STATS 🏈", anchor=False)
st.markdown("A web app that shows the season offensive stats between 2012 and 2022 for QB, WR, RB and TE.")
btn = st.button("Kaggle dataset")
if btn:
  webbrowser.open_new_tab("https://www.kaggle.com/datasets/philiphyde1/nfl-stats-1999-2022?rvi=1")

st.subheader("✔️ Filters", anchor=False)
st.markdown("**Season**: 2012 - 2022")
st.markdown("**Position:** QB, WR, RB, TE")
col1, col2, col3 = st.columns(3)
col1.markdown(
  '''
  **Team**:
  * ARI (Arizona Cardinals)
  * ATL (Atlanta Falcons)
  * BAL (Baltimore Ravens)
  * BUF (Buffalo Bills)
  * CAR (Carolina Panthers)
  * CHI (Chicago Bears)
  * CIN (Cincinnati Bengals)
  * CLE (Cleveland Browns)
  * DAL (Dallas Cowboys)
  * DEN (Denver Broncos)
  * DET (Detroit Lions)
  ''')
col2.markdown(
  '''
  &nbsp;
  * GB (Green Bay Packers)
  * HOU (Houston Texans)
  * IND (Indianapolis Colts)
  * JAX (Jacksonville Jaguars)
  * KC (Kansas City Chiefs)
  * LV (Las Vegas Raiders)
  * LAC (Los Angeles Chargers)
  * LA (Los Angeles Rams)
  * MIA (Miami Dolphins)
  * MIN (Minnesota Vikings)
  * NE (New England Patriots)
  '''
)
col3.markdown(
  '''
  &nbsp;
  * NO (New Orleans Saints)
  * NYG (New York Giants)
  * NYJ (New York Jets)
  * PHI (Philadelphia Eagles)
  * PIT (Pittsburgh Steelers)
  * SF (San Francisco 49ers)
  * SEA (Seattle Seahawks)
  * TB (Tampa Bay Buccaneers)
  * TEN (Tennessee Titans)
  * WAS (Washington Commanders)
  '''
)


st.sidebar.markdown("Developed by [Rita Rodrigues](https://github.com/ritarodrigues08)")