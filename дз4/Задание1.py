import pandas as pd

df = pd.read_csv('group_orders.csv', sep=',', encoding='utf-8')

order_count = df.loc[:,'order_id':'total'].drop_duplicates() 
print(order_count['city'].value_counts())