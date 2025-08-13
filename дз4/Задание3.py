import pandas as pd

df = pd.read_csv('group_orders.csv', sep=',', encoding='utf-8')
unique = df.drop_duplicates(subset="order_id")

product1 = unique.groupby('product')['quantity'].sum().reset_index()
product1 = product1.sort_values(by='quantity', ascending=False)

top = product1.head(1)
print(top)