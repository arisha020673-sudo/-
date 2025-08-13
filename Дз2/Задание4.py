import pandas as pd

df = pd.read_csv('customers.csv', sep=',', encoding='utf-8')

filter_df = df[(df['gender']== 'F') & (df['birth_date'] <= '1995-01-01')][['customer_id', 'first_name', 'last_name', 'birth_date']]

print(filter_df)