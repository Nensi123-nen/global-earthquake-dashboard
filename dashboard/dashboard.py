import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Title ---
st.set_page_config(page_title="🌍 Earthquake Dashboard", layout="wide")
st.title("🌍 Global Earthquake Data Dashboard")

# --- Load Dataset ---
@st.cache_data
def load_data():
    df = pd.read_csv("earthquakes.csv")
    return df

df = load_data()

# --- Data Overview ---
st.sidebar.header("📋 Data Overview")
st.sidebar.write(f"Total Records: {len(df)}")
st.sidebar.write(f"Columns: {list(df.columns)}")

st.subheader("🔍 Preview of Earthquake Data")
st.dataframe(df.head())

# --- Filters (if columns exist) ---
if "mag" in df.columns:
    min_mag, max_mag = float(df["mag"].min()), float(df["mag"].max())
    mag_range = st.slider("Select Magnitude Range", min_mag, max_mag, (min_mag, max_mag))
    df = df[(df["mag"] >= mag_range[0]) & (df["mag"] <= mag_range[1])]

if "time" in df.columns:
    df["time"] = pd.to_datetime(df["time"], errors="coerce")
    start_date = df["time"].min()
    end_date = df["time"].max()
    date_range = st.date_input("Select Date Range", [start_date, end_date])
    df = df[(df["time"].dt.date >= date_range[0]) & (df["time"].dt.date <= date_range[1])]

# --- Key Stats ---
st.subheader("📊 Key Statistics")
if "mag" in df.columns:
    col1, col2, col3 = st.columns(3)
    col1.metric("Average Magnitude", round(df["mag"].mean(), 2))
    col2.metric("Maximum Magnitude", round(df["mag"].max(), 2))
    col3.metric("Minimum Magnitude", round(df["mag"].min(), 2))

# --- Line Chart: Magnitude Over Time ---
if "time" in df.columns and "mag" in df.columns:
    st.subheader("📈 Magnitude Over Time")
    fig = px.line(df, x="time", y="mag", title="Earthquake Magnitude Trend")
    st.plotly_chart(fig, use_container_width=True)

# --- Map Visualization ---
if "latitude" in df.columns and "longitude" in df.columns:
    st.subheader("🗺️ Earthquake Locations Map")
    st.map(df[["latitude", "longitude"]].dropna())
else:
    st.warning("No latitude/longitude columns found in data.")
