import pandas as pd

users = pd.read_csv('users_new.csv')
orders = pd.read_csv('orders_new.csv')

df = users[(users['region'] == 'North') & (users['age'] < 30)]
merged = pd.merge(df, orders, on='user_id', how='left')
count = merged.groupby(['name']).size().reset_index(name='orders_count')

print(count)