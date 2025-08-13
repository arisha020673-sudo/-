import pandas as pd

df = pd.read_csv('orders.csv', sep=',', encoding='utf-8')

filter_df = df[(df['total']> 10000)&(df['total']< 15000)]
filter_df = filter_df [(filter_df['order_date'] >= '2023-01-01') & (filter_df['order_date'] <= '2023-12-31')]

print(filter_df[['order_id', 'total', 'order_date']])