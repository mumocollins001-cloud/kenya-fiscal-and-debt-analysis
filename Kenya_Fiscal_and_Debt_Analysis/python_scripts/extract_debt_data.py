import pandas as pd

file_path = r"C:\Users\ADMIN\Desktop\Kenya_Fiscal_and_Debt_Analysis\data\Chapter-5-Public-Finance.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="Table 5.10",
    header=None
)

# Extract years
years = df.iloc[2, 2:8].values

# Extract debt rows
external = df.iloc[26, 2:8].values
internal = df.iloc[33, 2:8].values
total = df.iloc[34, 2:8].values

debt_df = pd.DataFrame({
    "Year": years,
    "External_Debt": external,
    "Internal_Debt": internal,
    "Total_Debt": total
})

print(debt_df)
debt_df.to_csv(
    r"C:\Users\ADMIN\Desktop\Kenya_Fiscal_and_Debt_Analysis\output\debt_analysis_dataset.csv",
    index=False
)

print("Dataset exported successfully.")
print(
    gdp[
        (gdp["Year"] >= 2019) &
        (gdp["Year"] <= 2024)
    ]
)