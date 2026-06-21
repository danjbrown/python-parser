import pandas as pd

ftse100Data = pd.read_csv("prices.csv").convert_dtypes()

print("First 5 Rows:")
print(ftse100Data.head())