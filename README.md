# airline-dashboard-project

## Problem Statement
The airline industry is a critical part of global transportation, but it is often plagued by flight delays, which can significantly affect passengers and airline operations. Understanding the patterns and causes of flight delays can help airlines, airports, and passengers improve their planning and decision-making. In this project, we aim to analyze flight delay data to uncover insights into the factors influencing delays and how these delays have evolved over time.

This project involves building an end-to-end data pipeline that ingests, processes, and analyzes the airline dataset, which contains flight records, including flight delays, departure and arrival times, airlines, and flight routes. Using this dataset, we will:

Analyze average flight delays by airline to identify which airlines are most punctual and which are prone to delays.

Track flight delay trends over time (daily, monthly) to uncover any patterns in delays.

Examine the distribution of delays across different airports and flight routes to identify the most affected areas and high-risk routes.

The goal is to provide actionable insights for airline operations and improve the customer experience by understanding how delays impact different regions, airlines, and times of the year. Ultimately, this project will visualize these insights on an interactive dashboard, providing a comprehensive view of flight delays and trends.

# Airline Delay Analysis

## 🚀 Project Overview
This project builds an **end-to-end data pipeline** on **Google Cloud** to analyze flight delays.

![AirlineProject_HL_architecture](https://github.com/user-attachments/assets/c08b3fcc-9694-41bf-a698-1575002fca26)

## 🔧 Technologies Used
- **Google Cloud Storage (GCS)** - Raw data storage
- **BigQuery** - Data warehouse
- **Python** - Data processing (ETL)
- **Google Data Studio** - Dashboard visualization

## 🛠️ Setup Instructions
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt

2. Run below command:
python dashboard_project/main.py

---

## **📊 Dashboard Visuals**  

### **Tile 1: Categorical Distribution Graph**
🔹 **Bar Chart - Flight Status Distribution**  
- Shows how many flights were **Delayed, On Time, or Canceled**.

![Flight_status_bar_chart](https://github.com/user-attachments/assets/160daf67-acb8-4e9e-94be-204650478c5a)



### **Tile 2: Time-Series Graph**
🔹 **Line Chart - Delays Over Time**  
- Shows how delays change **daily or monthly** over time.  



![Flight_status_line_chart](https://github.com/user-attachments/assets/84291c6a-69ff-48e3-83b5-f7b22393780f)








