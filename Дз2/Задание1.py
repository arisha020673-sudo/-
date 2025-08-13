import pandas as pd

df = pd.read_csv('orders.csv', sep=',', encoding='utf-8')


filter_df = df[(df['total']>=30000)&(df['total']<=40000) & (df['order_date'] >= '2023-01-01')][['order_id']]

print(filter_df[['order_id']])