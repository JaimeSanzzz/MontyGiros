import pandas as pd

def numeric(df):
    df.replace({'Weekday of Fecha Referencia':{'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday':7}}, inplace=True)
    df.replace({'Month of Fecha Referencia': {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7,
    'August':8, 'September':9, 'October':10, 'November':11, 'December':12}}, inplace=True)
    
    