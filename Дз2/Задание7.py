import pandas as pd

orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')

customers['birth_date'] = pd.to_datetime(customers['birth_date'], errors='coerce')

date = customers[customers['birth_date'].dt.year == 1990]
merged = orders.merge(date[['customer_id']], on='customer_id', how='inner')

result = merged[['order_id', 'customer_id']]

print(result)
