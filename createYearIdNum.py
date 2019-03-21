import pandas as pd
import numpy as np
df_Addr_Year=pd.DataFrame(data=list(range(range_id_each_year['2010'][0], range_id_each_year['2010'][1])), columns=['Address ID'])
df_Addr_Year['Year'] = 10
df_Addr_Year.to_csv('id_num_10.dat', mode='a' , sep='\t', index=False, header=True)

df_Addr_Year=pd.DataFrame(data=list(range(range_id_each_year['2011'][0], range_id_each_year['2011'][1])), columns=['Address ID'])
df_Addr_Year['Year'] = 11
df_Addr_Year.to_csv('id_num_11.dat', mode='a' , sep='\t', index=False, header=True)

df_Addr_Year=pd.DataFrame(data=list(range(range_id_each_year['2012'][0], range_id_each_year['2012'][1])), columns=['Address ID'])
df_Addr_Year['Year'] = 12
df_Addr_Year.to_csv('id_num_12.dat', mode='a' , sep='\t', index=False, header=True)

df_Addr_Year=pd.DataFrame(data=list(range(range_id_each_year['2013'][0], range_id_each_year['2013'][1])), columns=['Address ID'])
df_Addr_Year['Year'] = 13
df_Addr_Year.to_csv('id_num_13.dat', mode='a' , sep='\t', index=False, header=True)

df_Addr_Year=pd.DataFrame(data=list(range(range_id_each_year['2014'][0], range_id_each_year['2014'][1])), columns=['Address ID'])
df_Addr_Year['Year'] = 14
df_Addr_Year.to_csv('id_num_14.dat', mode='a' , sep='\t', index=False, header=True)

df_Addr_Year=pd.DataFrame(data=list(range(range_id_each_year['2015'][0], range_id_each_year['2015'][1])), columns=['Address ID'])
df_Addr_Year['Year'] = 15
df_Addr_Year.to_csv('id_num_15.dat', mode='a' , sep='\t', index=False, header=True)

df_Addr_Year=pd.DataFrame(data=list(range(int(range_id_each_year['2016'][0]), int(range_id_each_year['2016'][1]))), columns=['Address ID'])
df_Addr_Year['Year'] = 16
df_Addr_Year.to_csv('id_num_16.dat', mode='a' , sep='\t', index=False, header=True)

df_Addr_Year=pd.DataFrame(data=list(range(int(range_id_each_year['2017'][0]), range_id_each_year['2017'][1])), columns=['Address ID'])
df_Addr_Year['Year'] = 17
df_Addr_Year.to_csv('id_num_17.dat', mode='a' , sep='\t', index=False, header=True)


def addTransactions(ay):
    return len(duplicates_df_Addr_Year[duplicates_df_Addr_Year['Address ID']==ay])

#df_Addr_Year['NumTX'] = df_Addr_Year['Address ID'].apply(addTransactions)

df_Addr_Year = pd.read_csv('id_num_year.dat', sep='\t')
for index, row in pd.read_csv('id_num_year.dat', sep='\t'):
#for frame in data_10_17:
#    for index, row in frame.iterrows():
#        if row['address ID'] in df_Addr_Year['Address ID']:
#            df_Addr_Year.loc[df_Addr_Year['Address ID']==row['address ID']][NumTX]=len(frame['address ID'])
#        else:
#            df_Addr_Year.append(pd.DataFrame([row['address ID'], len(frame['address ID'])]))
