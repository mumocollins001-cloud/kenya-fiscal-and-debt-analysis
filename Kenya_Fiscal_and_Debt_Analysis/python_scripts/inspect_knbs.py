import pandas as pd

file_path = r"C:\Users\ADMIN\Desktop\Kenya_Fiscal_and_Debt_Analysis\data\Chapter-5-Public-Finance.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="Table 5.2",
    header=None
)

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 50)
pd.set_option("display.width", None)

print(df.iloc[:40])