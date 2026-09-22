import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import sqlite3 
db = sqlite3.connect("clean_data.db")
query = """
SELECT DISTINCT *
FROM sales
WHERE Order_ID IS NOT NULL
    AND Product IS NOT NULL
    AND Category IS NOT NULL
    AND Price IS NOT NULL
    AND Quantity IS NOT NULL;
    """
df = pd.read_sql(query, db)
df["Revenue"] = df["Price"]*df["Quantity"]

x = df.groupby("Product")["Revenue"].sum()
y = df.groupby("Product")["Quantity"].sum()
#Chart Product Revenue
plt.figure(figsize=(8,5))
plt.bar(x.index,x.values)
plt.title("Product vs Total Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()
#Chart Product Quantity
plt.figure(figsize=(8,5))
plt.bar(y.index,y.values)
plt.title("Product vs Total Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()