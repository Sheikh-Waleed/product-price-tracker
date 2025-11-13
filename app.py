# app.py
import streamlit as st
import pandas as pd

st.title("Product Price Tracker (Demo)")

df = pd.read_csv('products_all.csv')
st.write("Showing first 50 products", df.head(50))

min_price = float(df['price'].min())
max_price = float(df['price'].max())

price_filter = st.slider("Price range", min_price, max_price, (min_price, max_price))
filtered = df[(df['price'] >= price_filter[0]) & (df['price'] <= price_filter[1])]

st.dataframe(filtered)
st.download_button("Download CSV", filtered.to_csv(index=False).encode('utf-8'), "filtered_products.csv")
