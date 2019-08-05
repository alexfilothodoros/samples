# https://pypi.org/project/CurrencyConverter/
# https://stackoverflow.com/questions/44604440/forex-historical-data-in-python
import pandas as pd
from datetime import date,datetime
from forex_python.converter import get_rate, convert





my_cols= ['TransID',  'Date',   'Currency',  'Net']
df = pd.read_csv('example_data.txt',names=my_cols, sep =',')
df = df.drop(df.index[0])
df.head()
df.columns
df['TransID']
df['Date']
df['Currency']
df['Net']



for index, row in df.iterrows():
#    print(row['Date'], row['Net'])
    curr = 'USD'
    am = float(row['Net'])
    t1=row['Date'];t2=str.split(t1,'-')
    y, m, d = int(t2[0]), int(t2[1]), int(t2[2])
#    c = CurrencyConverter()
#    c.convert(am, 'USD', 'EUR',date=date(y, m, d)) # converts from USD to EUR
    t = datetime(y, m, d); converted=(convert('USD', 'EUR', am,t)) # with forex_python
    print(row['Date'],y , m , d ,am, converted)

    