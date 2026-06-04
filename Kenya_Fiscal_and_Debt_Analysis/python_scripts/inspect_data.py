import pandas as pd

gdp = pd.read_csv(
    r"C:\Users\ADMIN\Desktop\Kenya_Public_Debt_Analysis\data\API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_262909.csv",
    skiprows=4
)

debt = pd.read_csv(
    r"C:\Users\ADMIN\Desktop\Kenya_Public_Debt_Analysis\data\API_GC.DOD.TOTL.GD.ZS_DS2_en_csv_v2_276954.csv",
    skiprows=4
)

# Filter Kenya only
gdp_kenya = gdp[gdp["Country Code"] == "KEN"]

debt_kenya = debt[debt["Country Code"] == "KEN"]

print("GDP KENYA")
print(gdp_kenya.iloc[:, :10])

print("\n")

print("DEBT KENYA")
print(debt_kenya.iloc[:, :10])