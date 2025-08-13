import pandas as pd

df = pd.read_csv('shop.csv', sep=',', encoding='utf-8')

filter_df = df[(df['birth_date'] >= '1990-01-01') & (df['birth_date'] <= '1990-12-31')]
print(filter_df[['order_id', 'customer_id']])