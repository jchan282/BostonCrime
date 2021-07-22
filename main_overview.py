import streamlit as st
import pandas as pd

def app():
        datafile = "bostoncrime2021.csv"
        df = pd.read_csv(datafile)
        datafile2 = "BostonPoliceDistricts.csv"
        df2 = pd.read_csv(datafile2)

        st.title('Analysis of Boston reported Crime Data')
        st.subheader("Hello! Welcome to the Boston Crime Data App. This app analyzes and visualizes crime incident data in the first half of 2021 in the city of Boston. ")
        from PIL import Image
        image = Image.open('police_report.jpeg')
        st.image(image)

        st.subheader("Background")
        st.markdown("Crime incident reports are provided by Boston Police Department (BPD) to document the initial details surrounding an incident to which BPD officers respond.")
        st.subheader("Dataset Preview")
        st.dataframe(df.head(10))

        st.subheader("District Table")
        st.table(df2)
