import pandas as pd

df=pd.read_csv("C:/Users/jdunc/JCPSHomelessPopulation/jcps_total_homeless (2).csv")

df.head()
print(df.head(20))

df.drop('SLN', 'Male', 'Female', 'Homeless % Among Total Homeless Population')