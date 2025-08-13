import pandas as pd

df = pd.read_csv('orders.csv', sep=',', encoding='utf-8')

filter_df = df [ (df['customer_id'] >= 68) & (df['customer_id'] <= 88) ]
filter_df = filter_df [(filter_df['order_date'] >= '2022-01-01') & (filter_df['order_date'] <= '2022-12-01')]
test = filter_df.head(11).tail(6)
print(test[['order_id', 'total']])