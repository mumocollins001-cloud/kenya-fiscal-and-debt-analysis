import pandas as pd

gdp = pd.read_csv(
    r"C:\Users\ADMIN\Desktop\Kenya_Public_Debt_Analysis\data\API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_262909.csv",
    skiprows=4
)

# Kenya only
gdp = gdp[gdp["Country Code"] == "KEN"]

# Keep only year columns
gdp = gdp.loc[:, "1960":"2025"]

# Convert columns into rows
gdp = gdp.T

# Rename column
gdp.columns = ["GDP_Growth"]

# Move years into a column
gdp = gdp.reset_index()

# Rename year column
gdp.rename(columns={"index": "Year"}, inplace=True)

print(gdp.head())

print(gdp.head())

debt = pd.read_csv(
    r"C:\Users\ADMIN\Desktop\Kenya_Public_Debt_Analysis\data\API_GC.DOD.TOTL.GD.ZS_DS2_en_csv_v2_276954.csv",
    skiprows=4
)

debt = debt[debt["Country Code"] == "KEN"]

debt = debt.loc[:, "1960":"2025"]

print(debt.iloc[:, 40:66])