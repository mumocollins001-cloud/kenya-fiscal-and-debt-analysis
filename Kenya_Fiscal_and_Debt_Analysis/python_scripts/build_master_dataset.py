import pandas as pd

# GDP DATA
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

gdp = gdp[
    (gdp["Year"] >= 2019) &
    (gdp["Year"] <= 2024)
]


# DEBT DATA
debt = pd.DataFrame({
    "Year":[2019,2020,2021,2022,2023,2024],
    "External_Debt":[2863732.896219,3350563.0,3842321.82,4154590.92,5276331.98,5071538.69],
    "Internal_Debt":[2278054.0,2674217.0,3140664.0,3910916.77,4347529.08,4884058.41],
    "Total_Debt":[5141786.896219,6024780.0,6982985.82,8065507.69,9623861.06,9955597.10]
})

# MERGE
master_df = pd.merge(
    gdp,
    debt,
    on="Year"
)
print(master_df)

master_df.to_csv(
    r"C:\Users\ADMIN\Desktop\Kenya_Fiscal_and_Debt_Analysis\output\master_dataset.csv",
    index=False
)

print("Master dataset exported successfully.")

print("\nDataset Shape:")
print(master_df.shape)

print("\nColumn Names:")
print(master_df.columns)
print("\nSummary Statistics:")
print(master_df.describe())
print("\nCorrelation Matrix:")
print(
    master_df[
        ["GDP_Growth",
         "External_Debt",
         "Internal_Debt",
         "Total_Debt"]
    ].corr()
)