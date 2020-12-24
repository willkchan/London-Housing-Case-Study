import pandas as pd
import numpy as np
import matplotlib as plt

url_LondonHousePrices = "https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK%20House%20price%20index.xls"

properties = pd.read_excel(url_LondonHousePrices, sheet_name='Average price', index_col= None)

print(properties.head().to_string())
# print(properties.info())
print(properties.shape)

