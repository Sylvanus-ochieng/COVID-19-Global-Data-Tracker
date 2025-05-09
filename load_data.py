import pandas as pd

# ✅ Load confirmed cases data
df_confirmed = pd.read_csv('../data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

# 🔍 Preview first 5 rows
print("First 5 rows:")
print(df_confirmed.head())

# 🔍 Columns
print("\nColumns:")
print(df_confirmed.columns)

# 🔍 Missing values
print("\nMissing values:")
print(df_confirmed.isnull().sum())

# 🔍 Shape
print("\nData shape (rows, columns):")
print(df_confirmed.shape)
