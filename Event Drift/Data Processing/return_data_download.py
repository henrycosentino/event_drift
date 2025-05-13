### STOCK RETURN DOWNLOAD ###
    # This file is used to download stock prices
    # It uses the securities from our universe, reading in from universe_selection.py
    # Then, calculates daily price returns and downloads them to an Excel file

import pandas as pd
import yfinance as yf
import os
from universe_selection import equities_ls

# Add the market (this will be used in the regression analysis as an independent control variable)
equities_ls.append("SPY")

# Download data from yfinance
start = "2020-12-31"
end = "2024-12-31"

px_data = yf.download(
        tickers=equities_ls,
        start=start,
        end=end,
        interval='1d',
        group_by='ticker',
        auto_adjust=True,
        prepost=False,
        threads=True
    )

# Get only close price columns
close_prices = px_data.xs('Close', level='Price', axis=1)

# Drop any columns that have more than 5 NaN values (these columns do not have ample return data)
new_close_price_cols = []
for col in close_prices.columns:
    if close_prices[col].isna().sum() > 5:
        continue
    else:
        new_close_price_cols.append(col)

close_prices = close_prices[new_close_price_cols]

# Get daily returns
return_df = close_prices / close_prices.shift(1) - 1
return_df = return_df.dropna(how='all')
return_df = return_df.interpolate(method='linear')
print("=="*40)
print("SAMPLE RETURN DATA")
print(return_df.head())
print("=="*40)
print(return_df.info())
print("=="*40)

# Download Data
if __name__ == '__main__':
    file_path = '/Users/henrycosentino/Desktop/Python/Projects/Event Drift/Data/return_data.xlsx'

    if not os.path.exists(file_path):
        return_df.to_excel(file_path)
        print(f"File saved to {file_path}")
    else:
        print(f"File already exists at {file_path}")