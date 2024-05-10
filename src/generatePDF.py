from fpdf import FPDF
import base64

class PDFWithBackground(FPDF):
    def __init__(self):
        super().__init__()
        self.background = None

    def set_background(self, image_path):
        self.background = image_path

    def add_page(self, orientation=''):
        super().add_page(orientation)
        if self.background:
            self.image(self.background, 0, 0, self.w, self.h)

    def footer(self):
        # Posición a 1.5 cm desde el fondo
        self.set_y(-15)
        # Configurar la fuente para el pie de página
        self.set_font('Arial', 'I', 8)
        # Número de página
        self.cell(0, 10, 'Página ' + str(self.page_no()), 0, 0, 'C')

def create_report(year):    
    pdf = PDFWithBackground()
    pdf.set_background('Images/background.png')

    pdf.add_page()

    pdf.set_y(100)
    pdf.set_font('Courier',style='B',size=57)
    pdf.cell(0,0,'Report',0,1,'C')

    pdf.set_y(125)
    pdf.set_font('Courier',style='B',size=57)
    pdf.cell(0,0,'  Videogames',0,1,'C')

    pdf.set_y(150)
    pdf.set_font('Courier',style='B',size=57)
    pdf.cell(0,0,'Sales',0,1,'C')

    pdf.add_page()

    pdf.set_y(50)
    pdf.set_font('Courier',style='B',size=27)   # Arial, Times, Courier
    pdf.cell(0,0,'Videogames Sales',0,1,'C')

    pdf.set_y(75)
    pdf.set_font('Courier','B',size=20)   # Arial, Times, Courier
    pdf.cell(0,0,'',0,1,'R')

    pdf.set_y(155)
    pdf.set_font('Courier',size=15) 
    pdf.multi_cell(190,6,'This report presents an analysis of video game sales in recent years, exploring trends in the industry and how different factors impact game sales and reception. Key statistics on global video game sales are examined, as well as changes in consumer preferences over time. This analysis provides a clear insight into the dynamic relationship between video game production and its audience, offering relevant information to understand the market and guide future development and marketing strategies.',0,1,'L')
    pdf.add_page()
    pdf.set_y(50)
    pdf.set_font('Courier',style='B',size=27)   # Arial, Times, Courier
    pdf.cell(0,0,'Videogames Sales by platform',0,1,'C')
    pdf.image(f'Images/sales_by_platform_year.png',x=10,y=75,w=200,h=150)
    pdf.add_page()
    pdf.set_y(50)
    pdf.set_font('Courier',style='B',size=27)   # Arial, Times, Courier
    pdf.cell(0,0,'Global Video Game Sales Trends by Region',0,1,'C')
    pdf.image(f'Images/Global_VideoGames_Sales_Trends_by_Region.png',x=10,y=75,w=200,h=150)
    pdf.add_page()

    pdf.set_y(45)
    pdf.set_font('Courier',style='B',size=23)   # Arial, Times, Courier
    pdf.cell(0,0,f'',0,1,'R')
    
    pdf.cell(0,0,f'Report year {year}',0,1,'C')
    
    pdf.image(f'Images/pie_chart_genres_{year}.png',x=50,y=50,w=120,h=120)
    pdf.image(f'Images/bar_chart_top_5_{year}.png',x=50,y=160,w=120,h=120)

    return pdf

def create_download_link(val, filename):
    b64 = base64.b64encode(val)
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Descargar reporte en PDF</a>'