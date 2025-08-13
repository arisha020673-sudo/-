import pandas as pd

df = pd.read_csv('shop.csv', sep=',', encoding='utf-8')

gender1 = df.loc[:,'gender':'total'].drop_duplicates() 
print(gender1['gender'].value_counts())