import streamlit as st
import pandas as pd
import webbrowser

st.set_page_config(
  page_title="About",
  layout="centered"
)

if "data" not in st.session_state:
  df = pd.read_csv(r"C:\Users\anagr\Documentos\projects-github\data-analysis-projects\nfl-stats\yearly_data.csv", index_col=0)
  df.columns = df.columns.str.title()
  df = df.set_index("Name")
  df = df.sort_values(by="Season", ascending=False)
  st.session_state["data"] = df

st.title("NFL STATS 🏈", anchor=False)
st.markdown("A web app that shows the season offensive stats between 2012 and 2022 for QB, WR and TE.")
btn = st.button("Kaggle dataset")
if btn:
  webbrowser.open_new_tab("https://www.kaggle.com/datasets/philiphyde1/nfl-stats-1999-2022?rvi=1")


st.sidebar.markdown("Developed by [Rita Rodrigues](https://github.com/ritarodrigues08)")