#Выполните фильтрацию с помощью .query().
#Отберите все записи продаж пользователеиS , прошедших регистрацию начиная с 2022 года и совершивших заказы в 2023 году на сумму более 30000 руб. 
# Оставьте поля с ФИО и total. ПодсчитаиS те количество таких продаж.

import pandas as pd

orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
contacts = pd.read_csv('contacts.csv', sep=',', encoding='utf-8')

df = customers.merge(contacts, on="customer_id", how="left") \
.merge(orders, on="customer_id", how="inner")

df["registration_date"] = pd.to_datetime(df["registration_date"].str.strip(), errors="coerce")
df["order_date"] = pd.to_datetime(df["order_date"].str.strip(), errors="coerce")

mask = (
(df["registration_date"].dt.year >= 2022) & 
(df["order_date"].dt.year == 2023) & 
(df["total"] > 30000)
)

filtered = df.loc[mask, ["first_name", "last_name", "total"]]
count_sales = filtered.shape[0]

print(filtered)
print("Количество таких продаж:", count_sales)