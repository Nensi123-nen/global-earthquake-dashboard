import os
import pandas as pd

print("🔍 Checking for new earthquake data...")

data_dir = os.path.join(os.path.dirname(__file__), "..", "data_raw")
file_path = os.path.join(data_dir, "earthquakes.csv")
prev_file_path = os.path.join(data_dir, "earthquakes_prev.csv")

if not os.path.exists(file_path):
    print("❌ No latest earthquake file found. Run data_collection.py first.")
    exit()

# Load current data
current_df = pd.read_csv(file_path)

# Check if previous data exists
if os.path.exists(prev_file_path):
    previous_df = pd.read_csv(prev_file_path)

    # Compare by event ID or time
    new_events = current_df[~current_df['time'].isin(previous_df['time'])]

    if len(new_events) > 0:
        print(f"✅ {len(new_events)} new earthquake(s) detected!")
        print("🌍 Example:")
        print(new_events.head(3))
    else:
        print("⚠️ No new earthquake data since last run.")
else:
    print("🆕 No previous data found. Saving current dataset as baseline.")

# Save the current data as the new 'previous' version
current_df.to_csv(prev_file_path, index=False)
print("💾 Baseline updated successfully.")
