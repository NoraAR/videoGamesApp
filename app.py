import streamlit as st
import src.data as data
import src.graficos as graficos

st.title('videoGamesApp')
st.divider()
st.header('The dataset is:')
st.write(data.readData())

# Crear pestañas
tabs = st.tabs(["General Sales", "Platform Sales", ""])

# Contenido de la pestaña 1
with tabs[0]:
    graficos.histogram(2014)

# Contenido de la pestaña 2
with tabs[1]:
    st.write("Contenido de la pestaña 2")
    st.write("Contenido de la pestaña 2")
    