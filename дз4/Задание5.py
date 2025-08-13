import pandas as pd

df = pd.read_csv('group_orders.csv', sep=',', encoding='utf-8')

df_unique = df.drop_duplicates(subset="order_id")
avg_total = df_unique.groupby('city')['total'].mean().reset_index()
top = avg_total.sort_values(by='total', ascending=False).head(3)

print(top)