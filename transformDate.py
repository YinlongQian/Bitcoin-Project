import pandas as pd
from datetime import datetime
file='bh_simplified.dat'

df=pd.read_csv(file, sep='\t')
def getYear(data):
    d=datetime.fromtimestamp(data)
    return d.timetuple().tm_year
def getMonth(data):
    d=datetime.fromtimestamp(data)
    return d.timetuple().tm_mon
df['month']=df['timestamp'].apply(getMonth)
df['year']=df['timestamp'].apply(getYear)
df.to_csv('bh_readable.dat', sep='\t', index=False)
