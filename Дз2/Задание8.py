import pandas as pd

df = pd.read_csv('orders.csv', sep=',', encoding='utf-8')

filter_df = df[(df['total']> 5000)]
filter_df = filter_df [(filter_df['order_date'] >= '2023-02-01') & (filter_df['order_date'] <= '2023-02-29')]

print(filter_df[['order_id', 'total', 'order_date']])