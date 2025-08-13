import pandas as pd

df = pd.read_csv('group_orders.csv', sep=',', encoding='utf-8')
df_unique = df.drop_duplicates(subset="order_id")

counts = df_unique.groupby('city')['order_id'].count().reset_index()
counts = counts.sort_values(by='order_id', ascending=True)

print(counts)