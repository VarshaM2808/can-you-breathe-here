import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

air = pd.read_csv("air_quality_city.csv")

print("=== AIR DATA INFO ===")
print(air.info())

# Extract country from city
air["Country"] = air["City"].apply(lambda x: x.split(",")[-1].strip())

# Keep only required columns
air_clean = air[["Country", "Year", "AQI"]]

print("\n=== FIRST 5 ROWS OF CLEANED DATA ===")
print(air_clean.head())

air_country = (
    air_clean
    .groupby(["Country", "Year"], as_index=False)
    .agg(
        avg_aqi=("AQI", "mean"),
        median_aqi=("AQI", "median"),
        n_cities=("AQI", "size")
    )
)

print("\n=== COUNTRY-YEAR AQI (FIRST 10) ===")
print(air_country.head(10))

print("\nRows (country-year):", air_country.shape[0])
print("Unique countries:", air_country["Country"].nunique())
print("Year range:", air_country["Year"].min(), "-", air_country["Year"].max())

health = pd.read_csv("health_data.csv")

print("\n=== HEALTH DATA INFO ===")
print(health.info())

print("\n=== HEALTH DATA COLUMNS ===")
print(list(health.columns))

print("\n=== HEALTH FIRST 5 ROWS ===")
print(health.head())

# Select relevant health columns
health_clean = health[[
    "Country",
    "Year",
    "Mortality Rate (%)",
    "Prevalence Rate (%)",
    "Healthcare Access (%)",
    "Urbanization Rate (%)"
]].copy()

# Rename for easier use
health_clean = health_clean.rename(columns={
    "Mortality Rate (%)": "resp_mortality",
    "Prevalence Rate (%)": "resp_prevalence",
    "Healthcare Access (%)": "healthcare_access",
    "Urbanization Rate (%)": "urbanization"
})

print("\n=== CLEANED HEALTH DATA ===")
print(health_clean.head())

health_country = (
    health_clean
    .groupby(["Country", "Year"], as_index=False)
    .mean()
)

print("\n=== COUNTRY-YEAR HEALTH DATA ===")
print(health_country.head())
print("Rows:", health_country.shape[0])

df = pd.merge(
    air_country,
    health_country,
    on=["Country", "Year"],
    how="inner"
)

print("\n=== MERGED DATASET ===")
print(df.head())
print("\nMerged rows:", df.shape[0])

sns.scatterplot(
    data=df,
    x="avg_aqi",
    y="resp_mortality"
)
plt.title("Air Quality vs Respiratory Mortality")
plt.xlabel("Average AQI")
plt.ylabel("Respiratory Mortality Rate (%)")
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(
    df[["avg_aqi", "resp_mortality", "resp_prevalence", "healthcare_access", "urbanization"]]
    .corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Between Air Quality and Health Indicators")
plt.show()

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

df[["aqi_norm", "mortality_norm"]] = scaler.fit_transform(
    df[["avg_aqi", "resp_mortality"]]
)
df["breathability_score"] = 100 - (
    50 * df["aqi_norm"] +
    50 * df["mortality_norm"]
)

print(df[["Country", "Year", "breathability_score"]].head())

score_by_country = (
    df.groupby("Country")["breathability_score"]
    .mean()
    .sort_values(ascending=False)
)

score_by_country.head(10).plot(kind="bar", color="green")
plt.title("Top 10 Most Breathable Countries")
plt.ylabel("Breathability Score")
plt.show()

score_by_country.tail(10).plot(kind="bar", color="red")
plt.title("Top 10 Least Breathable Countries")
plt.ylabel("Breathability Score")
plt.show()
