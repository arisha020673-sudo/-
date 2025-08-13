import pandas as pd

df = pd.read_csv('products.csv', sep=',', encoding='utf-8')

filter_df = df [(df['price'] < 500) & (df['volume_ml'] == 5.0)][['product_name', 'price']]

print(filter_df)