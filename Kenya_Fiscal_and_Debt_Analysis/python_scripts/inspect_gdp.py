import pandas as pd

gdp = pd.read_csv(
    r"C:\Users\ADMIN\Desktop\Kenya_Fiscal_and_Debt_Analysis\data\API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_262909.csv",
    skiprows=4
)

gdp = gdp[gdp["Country Code"] == "KEN"]

gdp = gdp.loc[:, "1960":"2025"]

gdp = gdp.transpose()

gdp.columns = ["GDP_Growth"]

gdp.index.name = "Year"

gdp = gdp.reset_index()

gdp["Year"] = pd.to_numeric(gdp["Year"])

print(
    gdp[
        (gdp["Year"] >= 2019) &
        (gdp["Year"] <= 2024)
    ]
)