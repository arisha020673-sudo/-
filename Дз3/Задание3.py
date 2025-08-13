import pandas as pd

shop = pd.read_csv("shop.csv")
shop["order_date"] = pd.to_datetime(shop["order_date"].str.strip(), errors="coerce")
shop = shop.drop_duplicates(subset="order_id")

mask = shop["order_date"].dt.year.isin([2022, 2023])
counts = shop.loc[mask, "gender"].value_counts()

print(counts)