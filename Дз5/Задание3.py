import pandas as pd

orders = pd.read_csv('orders_new.csv')

product = orders['product'].value_counts().reset_index()

print(product)