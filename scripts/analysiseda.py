import os
import pandas as pd
import matplotlib.pyplot as plt

print("Starting Exploratory Data Analysis (EDA)...")

# Define file path
clean_file = os.path.join(os.path.dirname(__file__), "..", "data_processed", "earthquakes_clean.csv")

# Load cleaned data
df = pd.read_csv(clean_file)
print(f" Loaded {len(df)} cleaned earthquake records.")

# ---- 1️ Basic Overview ----
print("\n Dataset Overview:")
print(df.info())
print("\n Basic Statistics:")
print(df.describe())

# ---- 2️ Most Affected Regions ----
top_regions = df["region"].value_counts().head(10)
print("\n Top 10 Most Earthquake-Prone Regions:")
print(top_regions)

# ---- 3️ Risk Level Distribution ----
risk_counts = df["risk_level"].value_counts()
print("\n Earthquake Risk Level Distribution:")
print(risk_counts)

# ---- 4️ Average Magnitude by Region ----
avg_mag_by_region = df.groupby("region")["mag"].mean().sort_values(ascending=False).head(10)
print("\n Top 10 Regions by Average Magnitude:")
print(avg_mag_by_region)

# ---- 5️ Visualization Section ----
plt.figure(figsize=(8, 5))
risk_counts.plot(kind="bar", color=["green", "orange", "red", "purple"])
plt.title("Earthquake Risk Level Distribution")
plt.xlabel("Risk Level")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "..", "data_processed", "risk_distribution.png"))
plt.show()

plt.figure(figsize=(10, 6))
top_regions.plot(kind="barh", color="skyblue")
plt.title("Top 10 Most Earthquake-Prone Regions")
plt.xlabel("Number of Earthquakes")
plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "..", "data_processed", "top_regions.png"))
plt.show()

print("\n Charts saved in 'data_processed' folder as:")
print("  - risk_distribution.png")
print("  - top_regions.png")

print(" EDA Completed Successfully!")
