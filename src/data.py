import pandas as pd

def readData():
    base = pd.read_csv('Datasets/vgsales.csv')
    base.drop_duplicates(inplace=True)
    base.dropna(inplace=True)
    return base

def obtain_years():
    base = readData() 
    base = base.sort_values(by='Year', ascending=False)
    base['Year'] = base['Year'].astype(int) 
    years = list(base['Year'].unique())
    # Excluir los años 2017 y 2020 porque casi no hay datos
    years = [year for year in years if year not in [2016,2017, 2020]]
    return years
