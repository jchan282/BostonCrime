import main_overview
import Folium_Map
import crime_chart
import streamlit as st

PAGES = {
    "Home Page": main_overview,
    "Shooting Data With Map": Folium_Map,
    "Top 1-10 Most Common Crimes": crime_chart
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

#add a summary page with a district map
