#Выполните фильтрацию с помощью .query().
#Отберите все записи продаж пользователеиS , прошедших регистрацию начиная с 2022 года и совершивших заказы в 2023 году на сумму более 30000 руб. 
# Оставьте поля с ФИО и total. ПодсчитаиS те количество таких продаж.

import pandas as pd

df = pd.read_csv('shop.csv', sep=',', encoding='utf-8')

df['registration_date'] = pd.to_datetime(df['registration_date'], errors='coerce')
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

filter_df = df.query('registration_date.dt.year >= 2022 and order_date.dt.year == 2023 and total > 30000')[['first_name', 'last_name', 'total']]
result = filter_df.shape[0]

print(filter_df)
print(result)