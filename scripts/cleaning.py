import pandas as pd
import os

print("🧹 Starting data cleaning...")

# Paths
raw_data_path = os.path.join(os.path.dirname(__file__), "..", "data_raw", "earthquakes.csv")
clean_data_path = os.path.join(os.path.dirname(__file__), "..", "data_clean", "earthquakes_clean.csv")

# Load data
df = pd.read_csv(raw_data_path)
print(f"📥 Loaded {len(df)} records")

# Step 1: Drop completely empty rows
df.dropna(how='all', inplace=True)

# Step 2: Fill important columns
df['mag'].fillna(df['mag'].mean(), inplace=True)  # Replace missing magnitudes with mean
df['place'].fillna("Unknown Location", inplace=True)
df['depth'].fillna(df['depth'].median(), inplace=True)

# Step 3: Drop columns with too many missing values (optional)
threshold = 0.6  # keep columns with at least 60% data
df = df.loc[:, df.isnull().mean() < threshold]

# Step 4: Save cleaned file
os.makedirs(os.path.dirname(clean_data_path), exist_ok=True)
df.to_csv(clean_data_path, index=False)

print(f"✅ Cleaned data saved to: {clean_data_path}")
print(f"📊 Final record count: {len(df)} | Columns: {len(df.columns)}")
