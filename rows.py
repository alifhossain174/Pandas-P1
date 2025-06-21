import pandas as pd

df = pd.read_json("users.json")
print("First 2 Rows")
print(df.head(2))

print("Last 2 Rows")
print(df.tail(2))
