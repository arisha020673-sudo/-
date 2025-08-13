import pandas as pd

users = pd.read_csv('users_new.csv')
orders = pd.read_csv('orders_new.csv')

merged = pd.merge(orders, users, on='user_id', how='left')
merged['total_amount'] = merged['price'] * merged['quantity']

table = pd.pivot_table(merged, values='total_amount', index='region', columns='product',
aggfunc='sum', fill_value=0)

print(table)