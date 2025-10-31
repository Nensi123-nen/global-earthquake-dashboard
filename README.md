# global-earthquake-dashboard
Real-time earthquake data analytics and visualization dashboard built using Python, Power BI, and the USGS live API.
# 🌎 Global Earthquake Dashboard

An interactive, real-time data visualization project that tracks and analyzes worldwide earthquake activity.  
Built with **Python, Power BI**, and **USGS Earthquake API**, this dashboard provides insights into seismic patterns, magnitudes, and regions most affected by earthquakes.

---

## 📊 Project Overview

The **Global Earthquake Dashboard** collects real-time earthquake data, cleans and processes it, and visualizes global seismic trends using Power BI.  
It enables users to identify **high-risk zones**, **magnitude distributions**, and **tsunami-related events** through interactive visuals.

---

## 🚀 Key Features

- 🌍 Real-time data collection from **USGS Earthquake API**  
- 🧹 Automated **data cleaning and preprocessing** with Python  
- 📈 Interactive **Power BI dashboard** for deep insights  
- 🌐 Displays top regions by frequency and intensity  
- 🌊 Tracks tsunami-related seismic events  
- 📦 Exportable visual analytics and CSV reports  

---

## 🛠️ Tech Stack

| Category | Tools Used |
|-----------|-------------|
| Programming | Python (Pandas, Requests) |
| Data Visualization | Power BI |
| Data Source | USGS Earthquake API |
| Version Control | Git & GitHub |
| Others | VS Code, CSV Data Files |

---

## 📂 Project Structure
GLOBAL_DISASTER_PROJECT/
│

├── data_raw/ # Raw data fetched from API

├── data_clean/ # Cleaned and processed data

├── scripts/ # Python scripts for data handling

│ ├── collection.py # Fetch real-time data

│ ├── cleaning.py # Clean and prepare data

│ ├── analysiseda.py # Exploratory data analysis

│ ├── geovisualization.py # Geospatial data visualization

│ └── model_prediction.py # (Optional) Predictive analytics

│

├── dashboard/ # Power BI dashboard files

│ └── global_disaster_dashboard.pbix

│

├── output/ # Exported visualizations & results
│

├── README.md # Project documentation

└── requirements.txt # Python dependencies (optional)

---

## ⚙️ How It Works

1. **Data Collection** → Fetches live earthquake data from USGS API (`collection.py`)  
2. **Data Cleaning** → Removes nulls, duplicates, and formats columns (`cleaning.py`)  
3. **Data Processing** → Saves cleaned data into `data_clean/earthquakes_clean.csv`  
4. **Visualization** → Power BI dashboard built using cleaned data  
5. **Insights** → Displays frequency, magnitude, tsunami impact, and regional hotspots  

---

## 🧮 KPIs in Dashboard

- Total Earthquake Events  
- Average Magnitude  
- Tsunami Events Count  
- Most Affected Countries/Regions  
- Yearly Earthquake Trends  

---

## 🖼️ Dashboard Preview

*(Attach an image from your dashboard here)*  
Example:  
![Global Earthquake Dashboard](dashboard_preview.png)

---

## 🧠 Insights & Findings

- Most earthquakes occur along **Pacific Ring of Fire**  
- **Magnitude 4–5** earthquakes are most frequent globally  
- Significant **tsunami correlation** with high-magnitude events  

---

## 💡 Future Enhancements

- Integrate live update through API every hour  
- Add machine learning for earthquake pattern prediction  
- Automate dashboard updates via Power BI Service  

---

## 👩‍💻 Author

**Nensi Dhameliya**  
📍 Data Analyst | Power BI Developer | Machine Learning Enthusiast  
🔗 [LinkedIn](https://www.linkedin.com/in/nensi-dhameliya/)  
🔗 [GitHub](https://github.com/Nensi123-nen)

---

## 🪪 License

This project is open source under the [MIT License](LICENSE).

---

## ⭐ Support

If you like this project, please ⭐ the repository — it helps others find it!

---


