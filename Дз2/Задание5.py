import pandas as pd

df = pd.read_csv('orders.csv', sep=',', encoding='utf-8')

filter_df = df [(df['customer_id'] >= 10) & (df['customer_id'] <= 20)]
filter_df = filter_df [(filter_df['total'] > 8000)]

print(filter_df[['order_id', 'customer_id', 'total']])
