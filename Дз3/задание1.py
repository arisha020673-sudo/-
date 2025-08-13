import pandas as pd

orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
contacts = pd.read_csv('contacts.csv', sep=',', encoding='utf-8')

df = customers.merge(contacts, on='customer_id', how='left') \
.merge(orders, on='customer_id', how='left')

df["order_date"] = pd.to_datetime(
df["order_date"].str.strip(),
format="%Y-%m-%d %H:%M:%S",
errors="coerce"
)

countries = [
"Germany", "France", "Italy", "Spain","Russia", "UK",
]

mask = (
df["country"].isin(countries) &
(df["order_date"].dt.year == 2023) &
(df["order_date"].dt.quarter <= 2)
)
filtered_brackets = df[mask][["order_id", "total"]]

filtered_loc = df.loc[mask, ["order_id", "total"]]

filtered_query = df.query(
"country in @countries and order_date.dt.year == 2023 and order_date.dt.quarter <= 2"
)[["order_id", "total"]]

total_sales = filtered_brackets["total"].sum()
print("Сумма продаж:", total_sales)
