import pandas as pd
import time
import datetime

timestamps='bh.dat'

def getBlockAtDate(year, month):
    df=pd.DataFrame()
    df=pd.read_csv(timestamps, names=['blockID', 'hash', 'block_timestamp', 'n_txs'], sep='\t')
    formattedDate='/'.join([month,'01',year])
    formattedDate=time.mktime(datetime.datetime.strptime(formattedDate, '%m/%d/%y').timetuple())
    return df.ix[(df.block_timestamp-formattedDate).abs().argsort()[:1]]


