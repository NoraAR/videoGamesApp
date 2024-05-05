import streamlit as st
st.title('Mi primera aplicacion en la web')

nombre = st.text_input('Cual es tu nombre?')

if nombre is not None:
    st.write(f'Bienvenido {nombre} a mi primera app web')