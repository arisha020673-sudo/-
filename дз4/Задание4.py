import pandas as pd

df = pd.read_csv('group_orders.csv', sep=',', encoding='utf-8')

df_unique = df.drop_duplicates(subset="order_id")
df_unique['order_date'] = pd.to_datetime(df_unique['order_date'].str.strip(), errors='coerce')
df_unique['month'] = df_unique['order_date'].dt.to_period('M')

revenue_by_month = df_unique.groupby('month')['total'].sum().reset_index()

print(revenue_by_month)