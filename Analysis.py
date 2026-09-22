import sqlite3
import pandas as pd
import numpy as np
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
print(pd.DataFrame(df))
print("----------------------------------------------------------")
print("Total Order: ",np.size(df["Order_ID"]))
print("Product: ",df["Product"].unique())
print("Category: ",df["Category"].unique())
print("Any Missing Value: \n",df.isna().sum())
print("----------------------------------------------------------")

#Task 2
df["Revenue"] = df["Price"]*df["Quantity"]
print(pd.DataFrame(df))
print("----------------------------------------------------------")
print("Total Revenue: ",sum(df["Revenue"]))
print("----------------------------------------------------------")
#Task 3 
print("Best Product Performance")
print("=========================")
print(df.sort_values("Revenue",ascending=False))
print("-----------------------------------------------------------------")
'''Task 4'''
print("Highest Revenue product: ",df.loc[df["Revenue"].idxmax(),"Product"])
print("Lowest Revenue product: ",df.loc[df["Revenue"].idxmin(),"Product"])
print("Highest Quantity Product: ",df.loc[df["Quantity"].idxmin(),"Product"])