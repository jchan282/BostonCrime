import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import folium #customize the map


def app():


    datafile = "bostoncrime2021.csv"
    df = pd.read_csv(datafile)
    df = df.rename(columns = {'Lat':'lat'})
    df = df.rename(columns = {'Long':'lon'})
    df = df[~(df.lat == 0)] #ignore 0 lat and long
    print("\nAfter read:")
    print(df.dtypes)

    print("Shooting Location")
    df=df.loc[df['SHOOTING']== 1, ['lat','lon','OFFENSE_DESCRIPTION','MONTH',"STREET","OCCURRED_ON_DATE"]]
    df['MONTH'] = df['MONTH'].astype(str) #convert float to string
    df['MONTH'] = df['MONTH'].replace(['1','2','3','4','5','6'],["January","February","March","April","May","June"])
    #print(df)

    #Streamlit layout and Input
    st.subheader("Hello! Welcome to the Boston Crime App. This app analyzes and visualizes crime incident data in the first half of 2021 in Boston. ")
    crime_list = df.OFFENSE_DESCRIPTION.unique().tolist()
    month_list = df.MONTH.unique().tolist()
    option = st.selectbox('Please select the type of crime:',crime_list)
    option_Month = st.multiselect('Please select the month/months:',month_list)


    #new df based on options
    newdf = df[(df.OFFENSE_DESCRIPTION==option) & (df.MONTH.isin(option_Month))]
    st.dataframe(newdf)


    st.write('You selected:', option)
    map_results = ":high_brightness:" f"Here is a map showing all the shooting incidents associated with **{option.lower()}** in the selected month(s) !"
    st.markdown(map_results)
    st.write("*Note that different colors of pins represent different months")

    #customize the map
    m = folium.Map(location=[42.3601,-71.0589],zoom_start=11) #I try many numbers for zoom_start and 11 looks the best

    #function to assign color to month

    def color(MONTH):
        if MONTH == 'January':
            col = 'darkpurple'
        elif MONTH == 'February':
            col = 'blue'
        elif MONTH == 'March':
            col = 'red'
        elif MONTH == 'April':
            col = 'orange'
        elif MONTH == 'May':
            col = 'pink'
        elif MONTH == 'June':
            col = 'green'
        return col

    for column, row in newdf.iterrows():
        location = [row['lat'], row['lon']]
        folium.Marker(location,
                      popup = f'Date_and_Time:{row["OCCURRED_ON_DATE"]}',
                      icon=folium.Icon(color=color(row['MONTH'])
                      )).add_to(m)

    folium_static(m)

