import pandas as pd
df=pd.read_excel("JCPS_20-21 Homeless.xlsx")
print(df.describe())
print(df.head())
print(df.columns)