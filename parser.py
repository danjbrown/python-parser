import pandas as pd

class Parser:
    # constructor
    def __init__(self):
        self.source_filename=''
        self.source_type='csv'

    def parse(self):

        if self.source_type == "csv":
            df = pd.read_csv(self.source_filename, parse_dates=["Date"]).convert_dtypes()
        else:
            df = pd.read_json(self.source_filename).convert_dtypes()

        print("First 10 rows:")
        print(df.head(10))

        # rename columns
        new_column_names = {
            "Date": "date",
            "Open Price": "open_price",
            "Close Price": "close_price",
            "High Price": "high_price",
            "Low Price": "low_price",
            "Volume": "volume",
        }
        df.rename(columns=new_column_names, inplace = True)

        # drop null values in original data frame
        # df.dropna(inplace = True)

        print("Renamed columns:")
        print(df.columns)

        print("Check for missing data:")
        print(df.info())

        print("Missing data:")
        print(df.loc[df.isna().any(axis="columns")])

        print("Adding missing low prices using mean low price...")
        mean_low_price = df["low_price"].mean()
        self.custom_fillna(df, 'low_price', round(mean_low_price, 2))

        # Remove duplicates
        df.drop_duplicates(inplace = True)

        print("Statistics:")
        print(df.describe())

        print("First 10 corrected rows:")
        print(df.head(10))
    
        return df
    
    def custom_fillna(self, df, column_name, fill_value):
        s = df[column_name]
        for i in range(len(s)):
            if pd.isna(s[i]):
                df.loc[i, column_name] = fill_value
