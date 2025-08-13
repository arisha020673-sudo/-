import pandas as pd

users = pd.read_csv('users_new.csv')
orders = pd.read_csv('orders_new.csv')

orders_count = orders.groupby('user_id').size().reset_index(name='orders_count')
multiple = orders_count[orders_count['orders_count'] > 1]
result = pd.merge(multiple, users[['user_id', 'name']], on='user_id', how='left')

print(result[['name', 'orders_count']])