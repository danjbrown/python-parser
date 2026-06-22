import parser
import pandas as pd

dataParser = parser.Parser()
dataParser.source_type = "csv"

if dataParser.source_type == "csv":
    dataParser.source_filename = "prices.csv"
    data = dataParser.parse()
    data.to_csv("prices-cleaned.csv", index=False)
else:
    dataParser.source_filename = "prices.json"
    data = dataParser.parse()
    data.to_json("prices-cleaned.json", orient='records')