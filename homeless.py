import pandas as pd
import matplotlib.pyplot as plt

#keeping Brown School from this excel sheet only
elem=pd.read_excel("JCPS_20-21 Homeless.xlsx")
#total elem homeless population
elem_total_homeless=elem.iloc[89]
#district total homeless population
district_total_homeless=elem.iloc[93]
print(elem.describe())
print(elem.info())
print(elem.columns)
print(elem.shape)
print(elem.head())
print(elem.tail(15))
elem.drop(labels=[89,90], inplace=True)
print(elem.tail(15))
elem.drop(labels=range(92,102), inplace=True)
print(elem.tail(15))

#keeping Moore Traditional and The Academy @ Shawnee from this excel sheet only
hs=pd.read_excel("JCPS_20-21_HS.xlsx")
#total hs homeless population 
hs_total_homeless=hs.iloc[18]
print(hs.describe())
print(hs.info())
print(hs.columns)
print(hs.shape)
print(hs.head())
print(hs.tail(20))
hs.drop(labels=[18,19,20], inplace=True)
hs.drop(labels=range(23,33), inplace=True)
print(hs.tail())

ms=pd.read_excel("JCPS_20-21_MS.xlsx")
#total ms homeless population
ms_total_homeless=ms.iloc[22]
print(ms.describe())
print(ms.info())
print(ms.columns)
print(ms.shape)
print(ms.head())
print(ms.tail(25))
ms.drop(labels=range(22,37), inplace=True)
print(ms.tail())

df=pd.concat([elem, ms, hs])
print(df.shape)
print(df.describe())
print(df.info())
print(df.columns)
print(df.head())
print(df.tail())
#dropped unwanted columns
df.drop(columns=['SLN', 'Male', 'Female', 'Homeless % Among Total Homeless Population'], inplace=True)
print(df.columns)
print(df.head())

for i in range(1,9):
    df[df.columns[i]]=pd.to_numeric(df[df.columns[i]], errors='coerce')
    #df[df.columns[i]]=df[df.columns[i]].fillna(0)
    #df[df.columns[i]]=df[df.columns[i]].astype('int16')
print(df.head())
asian_sum=df['Asian'].sum()
print(asian_sum)
totals=df.iloc[:,range (1,8)].sum()
print(totals)

totals.plot.pie()