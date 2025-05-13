### UNIVERSE SELECTION ###
    # This file is used to gather the universe of stocks we will proceed to analyze
    # It reads from spx_constituents_annual_data.xlsx (data that was downloaded via Bloomberg)

import pandas as pd

fh = "/Users/henrycosentino/Desktop/Python/Projects/Event Drift/Data/spx_constituents_annual_data.xlsx"
year_range = range(2021, 2025, 1)
df_year_ls = [pd.read_excel(fh, sheet_name=str(year)) for year in year_range]

# Returning only the unique securites for each year (our true sample security set)
master_frame = pd.DataFrame()
for df_year in df_year_ls:
    df_year = df_year[['Ticker Symbol','GICS Ind Name\n', 'GICS Sector\n']]
    df_year = df_year.rename(columns={'Ticker Symbol': 'ticker',
                            'GICS Ind Name\n': 'industry',
                            'GICS Sector\n': 'sector'})
    if master_frame.empty:
        master_frame = df_year
    else:
        master_frame = pd.concat([master_frame, df_year], ignore_index=True)

master_frame = master_frame.drop_duplicates()
master_frame = master_frame[~master_frame["ticker"].str.contains(r"\d", regex=True)]
master_frame = master_frame.dropna().reset_index(drop=True)
print("=="*40)
print("S&P 500 Constituents Data (annual)".upper())
print(master_frame.head())
print("=="*40)
print(master_frame.info())
print("=="*40)

# The universe of equities we will eventually randomly sample from
equities_ls = list(master_frame.ticker)