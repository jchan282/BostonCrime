import pandas as pd #this is how I usually import pandas
import streamlit as st
import seaborn as sns

def app():

    st.set_option('deprecation.showPyplotGlobalUse', False)



    datafile = "bostoncrime2021.csv"
    df = pd.read_csv(datafile)
    df =df[['DISTRICT','MONTH','OFFENSE_DESCRIPTION']]
    df['MONTH'] = df['MONTH'].astype(str)
    df['MONTH'] = df['MONTH'].replace(['1','2','3','4','5','6'],["January","February","March","April","May","June"])
    df['OFFENSE_DESCRIPTION'] = df['OFFENSE_DESCRIPTION']
    df = df[(df.DISTRICT != "External")]

    datafile2 = "BostonPoliceDistricts.csv"
    df2 = pd.read_csv(datafile2)

    def districtcodetoname(df2,dname):
        df2=df2.values.tolist()
        for i in range(len(df2)):
            if df2[i][1]==dname:
                dname=df2[i][0]
        return dname



    df2.columns = df2.columns.str.replace(" ", "_")

    district_list = df2.District_Name.unique().tolist()
    print(district_list)
    month_list = df.MONTH.unique().tolist()


    st.subheader("Hello! Welcome to the Boston Crime Data App. This app analyzes and visualizes crime incident data in the first half of 2021 in the city of Boston. ")
    option = st.selectbox('Please select the district',district_list)
    option_Month = st.selectbox('Please select the month',month_list)

    code = districtcodetoname(df2,option)

    #new df based on options for graphs
    newdf2 = df[(df.DISTRICT == code) & (df.MONTH == option_Month)]

    st.dataframe(newdf2)
    barNum = st.slider('Slide to select the number of top common crimes', min_value=1, max_value=10)
    ax = sns.countplot(y="OFFENSE_DESCRIPTION",data=newdf2,order=newdf2.OFFENSE_DESCRIPTION.value_counts().iloc[:barNum].index,palette="Set3")
    ax.set(ylabel='Types of Crimes')

    st.write("Here a chart showing the top",barNum,"most common crimes in",option,"in the month of",option_Month'!')
    st.pyplot()





