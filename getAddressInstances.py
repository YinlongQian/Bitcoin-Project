import pandas as pd

#txout="txout.dat"
#chosenAddress=351859145
#txoutColNames=['txid','output_seq','addrid','sum']

def getAllAddressInstances(filename, address, columnNames, chunksize = 10 ** 5):
    df=pd.DataFrame()
    for chunk in pd.read_csv(filename, names=columnNames, sep='\t', chunksize=chunksize):
            df=df.append (chunk [chunk['addrid']==address])
    return df

#outputFile=''. join([str(chosenAddress),'.dat'])
#getAllAddressInstances(txout, chosenAddress, txoutColNames).to_csv(outputFile, sep='\t')
