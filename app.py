import streamlit as st
import src.data as data
import src.graphics as graphics
import src.generatePDF as reportPDF
import src.generateExcel as reportExcel
st.title('videoGamesApp')
st.divider()
st.header('The dataset is:')
st.write(data.readData())

# Crear pestañas
year = st.selectbox('Year: ',options= data.obtain_years())

tabs = st.tabs(["Platform Sales", "Genres Sales", "Top 10 Videogames", "Reports"])
col1,col2 = st.columns(2)
with tabs[0]:
    graphics.general_diagrams()
with tabs[1]:
    graphics.pie_diagrams(year)
with tabs[2]:
    graphics.top_videogames(year)
with tabs[3]:
    
    pdf = reportPDF.create_report(year)
    st.divider()
    col_1,col_2 = st.columns(2)
    html = reportPDF.create_download_link(pdf.output(dest="S").encode("latin-1"), f"Videogame_Report_{year}")
    col_1.markdown(html, unsafe_allow_html=True)
    pdf = reportPDF.create_report(year)

    wb = reportExcel.create_excel(year)
    excel_file = reportExcel.download_excel(wb)
    col_2.download_button(
    label="Descargar Reporte en Excel",
    data=excel_file,
    file_name=f"Videogame_Report_{year}.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


    
