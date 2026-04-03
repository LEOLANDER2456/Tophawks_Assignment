import pandas as pd
import numpy as np

df = pd.read_csv("messy_ecommerce_sales_data.csv")
print("First five without cleaning")
print(df.head())
df.columns = df.columns.str.strip().str.lower()

df = df.replace(["[null]", "null", ""], np.nan)

df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['price'] = df['price'].fillna(df['price'].median())

df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['quantity'] = df['quantity'].fillna(1)

df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

df = df.drop_duplicates()

df['customer_name'] = df['customer_name'].fillna("Unknown")
df['product'] = df['product'].fillna("Unknown")

valid_payments = ["Cash on Delivery", "PayPal", "Bank Transfer"]
df['payment_method'] = df['payment_method'].apply(
    lambda x: x if x in valid_payments else "Other"
)

df = df[df['price'] > 0]
print("Cleaned data")
print(df.head())

df.to_csv("data/cleaned_data.csv", index=False)