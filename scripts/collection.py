
import os
import pandas as pd
import requests

print("🚀 Starting Earthquake Data Collection...")

# Create folder if not exists
raw_data_dir = os.path.join(os.path.dirname(__file__), "..", "data_raw")
os.makedirs(raw_data_dir, exist_ok=True)

# URL of the USGS Earthquake API
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv"
file_path = os.path.join(raw_data_dir, "earthquakes.csv")

try:
    response = requests.get(url)
    response.raise_for_status()  # Check for bad response

    # Save content directly to CSV file
    with open(file_path, "wb") as f:
        f.write(response.content)

    df = pd.read_csv(file_path)
    print(f"✅ Data successfully saved to: {file_path}")
    print(f"📊 Total records fetched: {len(df)}")

    if len(df) == 0:
        print("⚠️ Warning: File is empty (no earthquake data found today).")
    else:
        print("🎉 Earthquake data collection complete!")

except Exception as e:
    print("❌ Error fetching data:", e)
