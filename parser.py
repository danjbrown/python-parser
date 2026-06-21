import pandas as pd

class Parser:
    # constructor
    def __init__(self):
        self.source_filename=''

    def parse_csv(self):

        parsed_data = pd.read_csv(self.source_filename, parse_dates=["Date"]).convert_dtypes()

        print("First 5 Rows:")
        print(parsed_data.head())

        new_column_names = {
            "Date": "date",
            "Open Price": "open_price",
            "Close Price": "close_price",
            "High Price": "high_price",
            "Low Price": "low_price",
            "Volume": "volume",
        }

        data = parsed_data.rename(columns=new_column_names)

        print("Columns:")
        print(data.columns)

        print("First 5 rows:")
        print(data.head())

        print("Check for missing data:")
        print(data.info())

        print("Print location of missing daat:")
        print(data.loc[data.isna().any(axis="columns")])

        print("Adding missing data...")
        data = data.rename(columns=new_column_names).combine_first(pd.DataFrame({"low_price": {3: 710032.92}}))

        print("First 5 corrected rows:")
        print(data.head())

        # Remove duplicates
        data.loc[data.duplicated(keep=False)]

        data = data.drop_duplicates()

        return data