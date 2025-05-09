import pandas as pd
import matplotlib.pyplot as plt

# Set file path
file_path = "C:\\Users\\USER\\OneDrive\\Desktop\\PERSONAL PORTDOLIO\\owid-covid-data.csv"

# Load data
df = pd.read_csv(file_path)

# Filter Kenya data
kenya_data = df[df['location'] == 'Kenya'].copy()

# Convert 'date' to datetime
kenya_data['date'] = pd.to_datetime(kenya_data['date'])

# 1️⃣ Total COVID-19 Cases in Kenya
plt.figure(figsize=(12, 6))
plt.plot(kenya_data['date'], kenya_data['total_cases'], marker='o', linestyle='-', color='blue')
plt.title('Total COVID-19 Cases in Kenya Over Time')
plt.xlabel('Date')
plt.ylabel('Total Confirmed Cases')
plt.grid(True)
plt.savefig('total_cases_kenya.png')
plt.show()

# 2️⃣ Daily New COVID-19 Cases in Kenya
plt.figure(figsize=(12, 6))
plt.bar(kenya_data['date'], kenya_data['new_cases'].fillna(0), color='orange')
plt.title('Daily New COVID-19 Cases in Kenya')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.grid(True)
plt.savefig('daily_new_cases_kenya.png')
plt.show()

# 3️⃣ COVID-19 Total Vaccinations in Kenya Over Time
kenya_vax = kenya_data.dropna(subset=['total_vaccinations'])
plt.figure(figsize=(12, 6))
plt.plot(kenya_vax['date'], kenya_vax['total_vaccinations'], marker='o', linestyle='-', color='green')
plt.title('COVID-19 Total Vaccinations in Kenya Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.grid(True)
plt.savefig('total_vaccinations_kenya.png')
plt.show()

# 4️⃣ Death Rate in Kenya Over Time
kenya_data['death_rate'] = kenya_data['total_deaths'] / kenya_data['total_cases']
plt.figure(figsize=(12, 6))
plt.plot(kenya_data['date'], kenya_data['death_rate'], marker='o', linestyle='-', color='red')
plt.title('Death Rate in Kenya Over Time (Total Deaths / Total Cases)')
plt.xlabel('Date')
plt.ylabel('Death Rate')
plt.grid(True)
plt.savefig('death_rate_kenya.png')
plt.show()

# 5️⃣ (Optional) Cumulative COVID-19 Vaccinations in Kenya (again)
plt.figure(figsize=(12, 6))
plt.plot(kenya_data['date'], kenya_data['total_vaccinations'], marker='o', linestyle='-', color='green')
plt.title('Cumulative COVID-19 Vaccinations in Kenya Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.grid(True)
plt.savefig('cumulative_vaccinations_kenya.png')
plt.show()

# 6️⃣ Cumulative Vaccinations for Kenya, USA, India
countries = ['Kenya', 'United States', 'India']
df_filtered = df[df['location'].isin(countries)].copy()
df_filtered['date'] = pd.to_datetime(df_filtered['date'])

plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], marker='o', label=country)

plt.title('Cumulative COVID-19 Vaccinations Over Time (Kenya, USA, India)')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.grid(True)
plt.savefig('vaccinations_kenya_usa_india.png')
plt.show()

# ✅ Save cleaned Kenya data
kenya_data.to_csv('kenya_covid_cleaned.csv', index=False)
