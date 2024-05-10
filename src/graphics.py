import streamlit as st

def top_videogames(year):
    st.image(f'Images/bar_chart_top_5_{year}.png')

def pie_diagrams(year):
    st.image(f'Images/pie_chart_genres_{year}.png')

def general_diagrams():
     st.image(f'Images/Global_VideoGames_Sales_Trends_by_Region.png')
     st.image(f'Images/sales_by_platform_year.png')
