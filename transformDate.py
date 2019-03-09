import pandas as pd
from datetime import datetime
file='bh_simplified.dat'

df=pd.read_csv(file, sep='\t')
def changeDate(data):
    d=datetime.fromtimestamp(data)
    return d.strftime('%d/%m/%y')
df['timestamp']=df['timestamp'].apply(changeDate)
df.to_csv('bh_readable.dat', sep='\t')
