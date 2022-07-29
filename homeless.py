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

#JCPS Unsuppressed Homeless Population Data (sum of columns)
plt.pie
plt.figure(figsize=(15,15))
plt.title('JCPS Homeless Population (Unsuppressed)', fontsize=20, fontweight="bold")
dataframe=pd.DataFrame({"Race": ['Asian', 'Two or More', 'Hispanic', 'White', 'African American'], "Per_Group": [52, 152, 325, 868, 1896]})
plt.pie(dataframe["Per_Group"], labels =dataframe["Race"], autopct='%1.1f%%',textprops={'fontsize': 15} )

#JCPS Total Homeless Population Data (includes suppressed data)
plt.pie
plt.figure(figsize=(15,15))
plt.title('JCPS Total Homeless Population (Suppressed)', fontsize=20, fontweight="bold")
dataframe=pd.DataFrame({"Race": ['Asian', 'Two or More', 'Hispanic', 'White', 'African American'], "Per_Group": [112, 228, 561, 940, 2105]})
plt.pie(dataframe["Per_Group"], labels =dataframe["Race"], autopct='%1.1f%%',textprops={'fontsize': 15} )

#plt.show()

##Check to ensure it dispays correctly
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
print(df)

#Sort to see which schools have the highest population of homeless students 
sort_by_total = df.sort_values('Total Homeless Count', ascending=False)
print(sort_by_total.head(20))


elem_enrollment=pd.read_excel("jcps_20-21_enrollment_elem.xlsx")
#total elementary students enrolled
elem_total_enrollment=elem_enrollment.iloc[91]
#total district enrollment (including Pre-K)
total_district_enrollment=elem_enrollment.iloc[95]
print(elem_enrollment.describe())
print(elem_enrollment.info())
print(elem_enrollment.columns)
print(elem_enrollment.shape)
print(elem_enrollment.head())
print(elem_enrollment.tail(15))
elem_enrollment.drop(labels=range(91,97), inplace=True)
print(elem_enrollment.tail())

ms_enrollment=pd.read_excel("jcps_20-21_enrollment_ms.xlsx")
#total ms students enrolled
ms_total_enrollment=ms_enrollment.iloc[25]
print(ms_enrollment.describe())
print(ms_enrollment.info())
print(ms_enrollment.columns)
print(ms_enrollment.shape)
print(ms_enrollment.head())
print(ms_enrollment.tail(8))
ms_enrollment.drop(labels=range(25,31), inplace=True)
print(ms_enrollment.tail())

hs_enrollment=pd.read_excel("jcps_20-21_enrollment_hs.xlsx")
#total hs students enrolled
hs_total_enrollment=hs_enrollment.iloc[21]
print(hs_enrollment.describe())
print(hs_enrollment.info())
print(hs_enrollment.columns)
print(hs_enrollment.shape)
print(hs_enrollment.head())
print(hs_enrollment.tail(8))
hs_enrollment.drop(labels=range(21,27), inplace=True)
print(hs_enrollment.tail())

#combined files
df2=pd.concat([elem_enrollment, ms_enrollment, hs_enrollment])
print(df2.head())
print(df2.tail())
#dropped unwanted columns, leaving Unnamed: 1 (school name) and total enrollment. changed Unnamed: 1 column name to School
df2.drop(df2.columns.difference(['Unnamed: 1', 'Total']), axis=1, inplace=True)
#print(df2.head())
print(df2.info())


for i in range(1,2):
    df2[df2.columns[i]]=pd.to_numeric(df2[df2.columns[i]], errors='coerce')
    df2[df2.columns[i]]=df2[df2.columns[i]].fillna(0)
    df2[df2.columns[i]]=df2[df2.columns[i]].astype('int')
print(df2.head())

df2.rename(columns = {'Unnamed: 1':'School'}, inplace=True)

df.drop(df.columns.difference(['School', 'Total Homeless Count']), axis=1, inplace=True)
for i in range(1,2):
    df[df.columns[i]]=pd.to_numeric(df[df.columns[i]], errors='coerce')
    df[df.columns[i]]=df[df.columns[i]].fillna(0)
    df[df2.columns[i]]=df[df.columns[i]].astype('int')
df2.drop(df2.columns.difference(['School', 'Total']), axis=1, inplace=True)
#df=df.astype(int)
#df2=df2.astype(int)

#print(df, df2)
#df_left = pd.merge(df2, df, how="left", indicator=True)
#df_outer = pd.merge(df2, df, how="outer", indicator=True)
#print(df_left)
#print(df_outer)
#df1_join = df.join(df2, rsuffix="_right")
#print(df1_join)