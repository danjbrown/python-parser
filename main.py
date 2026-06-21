import parser
import pandas as pd

csvParser = parser.Parser()
csvParser.source_filename = "prices.csv"
data = csvParser.parse_csv()

data.to_csv("prices-cleaned.csv", index=False)

data = pd.read_csv("prices-cleaned.csv").convert_dtypes()