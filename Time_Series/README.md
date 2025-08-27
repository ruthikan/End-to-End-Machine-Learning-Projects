# ⏳ Time Series Forecasting – AirPassengers Dataset

This project applies **Time Series Forecasting** techniques to the classic **AirPassengers dataset**, which contains monthly totals of international airline passengers from 1949 to 1960. The goal was to understand stationarity, apply ARIMA-based models, and forecast future passenger traffic.

---

## 📁 Project Overview
- **Problem Type:** Time Series Forecasting  
- **Objective:** Predict future passenger numbers based on historical airline data  
- **Dataset:** AirPassengers (monthly airline passenger totals, 1949–1960)  
- **Techniques:** ARIMA, Auto ARIMA, SARIMAX  

---

## 🔍 Workflow

1. **Data Preprocessing**  
   - Converted the `Month` column to `datetime` and set as index  
   - Verified data integrity (no nulls or duplicates)  

2. **Stationarity Check**  
   - Applied Augmented Dickey-Fuller (ADF) test → series was non-stationary  
   - Differenced the series to achieve stationarity  

3. **Exploratory Data Analysis (EDA)**  
   - Visualized the time series trend, seasonality, and rolling statistics  
   - Observed strong upward trend and seasonal variation  

4. **Model Building**  
   - Implemented **ARIMA model** (manual order selection)  
   - Used **Auto ARIMA** for automatic parameter tuning  
   - Built **SARIMAX** model for seasonality handling  

5. **Model Evaluation & Forecasting**  
   - Compared actual vs. predicted passenger counts  
   - Extended forecast for 24 months into the future  

---

## 📊 Results

- **Models Used:** ARIMA, Auto ARIMA, SARIMAX  
- **Evaluation Metric:** RMSE (Root Mean Squared Error)  
- **Forecasting:** Generated predictions for unseen test data and future months  

---

## 🧠 Key Learnings
- Understood **stationarity** and its importance in time series forecasting  
- Learned **differencing** to stabilize time series data  
- Explored **ARIMA vs. SARIMAX models** for handling trend and seasonality  
- Gained experience with **Auto ARIMA** for parameter tuning  
- Built confidence in forecasting future data points with time series models  

---

## 📚 Libraries Used
- Python 3  
- pandas, numpy  
- matplotlib, seaborn  
- statsmodels (ARIMA, SARIMAX)  
- pmdarima (Auto ARIMA)  

---

## 📂 Folder Structure
📦 Time_Series_AirPassengers/
├── AirPassengers.csv
├── TS_Airpassengers.ipynb
├── README.md
└── results/
├── original_vs_stationary.png
├── rolling_mean_std.png
├── forecast_plot.png

---

## 🙋‍♀️ About Me
lipI’m **Ruthika Nalajala**, an aspiring ML Engineer passionate about building end-to-end Machine Learning and Deep Learning projects. This project is part of my ML journey under **Intellipaat training**, showcasing my skills in **Time Series Analysis & Forecasting**.

📌 Explore all my projects here: [End-to-End Machine Learning Projects](https://github.com/ruthikan/End-to-End-Machine-Learning-Projects)

