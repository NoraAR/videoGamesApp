import pandas as pd

def readData():
    base = pd.read_csv('Datasets/vgsales.csv')
    base.drop_duplicates(inplace=True)
    base.dropna(inplace=True)
    return base

