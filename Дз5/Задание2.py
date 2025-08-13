import pandas as pd

orders = pd.read_csv('orders_new.csv')

orders2 = orders.query('product == "C" and (quantity * price) > 250')
print(orders2)