import streamlit as st
import pandas as pd
import preprocessor,helper

df = pd.read_csv('athlete_events.csv.zip')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df,region_df)

st.sidebar.title("Olympic Analysis")
user_menu = st.sidebar.radio(
    "Select an option",("Medal Tally","Overall analysis","Country- wise analysis","Athlete wise analysis")
)
#st.dataframe(df)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    st.dataframe(medal_tally)

    '''
    if selected_year == 'overall' and selected_country == 'overall':
         st.title("Overall Tally")
    if selected_year != 'overall' and selected_country == 'overall':
        st.title("Medal Tally in " + str(selected_year))
    if selected_year == 'overall' and selected_country != 'overall':
        st.title(selected_country + " Overall performance")
    if selected_year != 'overall' and selected_country != 'overall':
        st.title(selected_country + " performance in " + str(selected_year) + " Olymipcs")
'''


