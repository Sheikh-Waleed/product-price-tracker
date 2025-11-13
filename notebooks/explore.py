import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('products_all.csv')
df = df.dropna(subset=['price'])  # ensure numeric
df_sorted = df.sort_values('price').head(10)  # 10 cheapest

plt.figure(figsize=(10,6))
plt.barh(df_sorted['title'], df_sorted['price'])
plt.xlabel('Price (GBP)')
plt.title('Top 10 Cheapest Books')
plt.gca().invert_yaxis()
plt.subplots_adjust(left=0.35)
plt.tight_layout()
plt.savefig('top10_cheapest.png')
plt.show()