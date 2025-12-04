# 💻 Machine Learning Projects  – Ruthika Nalajala

Welcome to my Machine Learning portfolio! 👋  
This repository contains all the ML projects I’ve worked on during my learning journey with Intellipaat and personal practice. Each project is built from scratch using real-world datasets and covers EDA, model building, evaluation, and tuning.

---

## 📁 Projects Overview

### 🔹 1. Medical Insurance Charges Prediction
- Dataset: `insurance.csv`
- Model: Linear Regression
- Goal: Predict insurance charges based on features like age, BMI, smoking status, etc.
- Tasks: EDA, outlier handling, label encoding, model evaluation using RMSE & R² Score

---

### 🔹 2. Bank Marketing Term Deposit Prediction
- Dataset: `bank.csv`
- Model: Logistic Regression
- Goal: Predict whether a customer will subscribe to a term deposit
- Tasks: Null check, duplicate removal, outlier detection, label encoding, VIF for multicollinearity reduction
- Accuracy: ~88.48%

---

### 🔹 3. Heart Disease Classification
- Dataset: `heart.csv`
- Model: Decision Tree Classifier
- Goal: Predict presence of heart disease
- Tasks: Outlier check, depth pruning, EDA, confusion matrix, accuracy evaluation
- Accuracy: ~80.3%

---

### 🔹 4. Customer Churn Prediction
- Dataset: `customer_churn.csv`
- Model: Random Forest + GridSearchCV
- Goal: Predict customer churn in telecom
- Tasks: Data cleaning, label encoding, GridSearchCV for tuning
- Accuracy Improved: 77.8% → 78.96%

---

### 🔹 5. Census Income Classification
- Dataset: UCI Adult Dataset
- Models: Logistic Regression, Decision Tree, Random Forest + RandomizedSearchCV
- Goal: Predict if a person earns >$50K/year
- Tasks: Outlier removal, encoding, model comparison, RandomizedSearchCV for large dataset tuning
- Best Accuracy: ~85% with Random Forest

---

### 🔹 6. Disease Prediction
- Dataset: medical.csv (Symptom-based dataset)
- Model: K-Nearest Neighbors (KNN)
- Goal: Predict disease based on top 6 patient symptoms
- Tasks: Missing value handling, label encoding, distance metric selection (Euclidean), model training
- Accuracy Achieved: 98.47%

---

### 🔹 7. Cricket Player Segmentation
- Dataset: cricket_clean.csv
- Model: K-Means Clustering
- Goal: Segment international cricket players based on performance metrics
- Tasks: Data cleaning, outlier handling, standardization, elbow method, silhouette score, clustering
- Insights: Identified 4 optimal player clusters using performance indicator.

---
### 🔹 8. Customer Segmentation
- Dataset: Mall_Customers.csv
- Model: Hierarchical Clustering
- Goal: Segment mall customers based on income and spending score
- Tasks: Dendrogram analysis, agglomerative clustering, cluster visualization
- Outcome: Discovered 5 distinct customer groups for targeted marketing

---
### 🔹 9. Airline Passenger Forecasting  
- Dataset: AirPassengers.csv
- Model: ARIMA, Auto ARIMA, SARIMAX
- Goal: Forecast monthly international airline passengers (1949–1960 dataset)
- Tasks: Stationarity check (ADF test), differencing, trend & seasonality analysis, ARIMA modeling, Auto ARIMA tuning, SARIMAX forecasting
- Outcome: Successfully forecasted passenger growth for the next 24 months  

---
### 🔹10. Netflix Movie Recommendation System
- Dataset: https://drive.google.com/file/d/1G1UvjtdVip0W9JT8vK5M-HVOqj8NEffu/view?usp=sharing , copy of movie_titles.csv
- Model: SVD (Singular Value Decomposition)
- Goal: Generate personalized movie recommendations using collaborative filtering
- Tasks: Data cleaning, user–movie matrix creation, SVD model training, 3-fold cross-validation (RMSE), predicting top-N recommended movies for users
- Outcome: Built a recommendation system capable of predicting user preferences from sparse rating data

---
## 🚀 Tools & Technologies Used
- Python (Jupyter Notebook / Google Colab)  
- pandas, numpy, matplotlib, seaborn  
- scikit-learn  
- statsmodels (ARIMA, SARIMAX)  
- pmdarima (Auto ARIMA)  
- GridSearchCV & RandomizedSearchCV  

---

## 📌 Folder Structure
Each project folder contains:
- ✅ .py file and pdf 
- 📊 Dataset(csv)
- 📄 Mini README 

---

## 🙋‍♀️ About Me
Hi, I’m Ruthika Nalajala — an aspiring Machine Learning Engineer passionate about data, model interpretability, and solving real-world problems using AI.  
📚 Currently learning ML & DL through Intellipaat & self-guided projects.

📬 Let’s connect: [LinkedIn](https://www.linkedin.com/in/ruthika-nalajala-73127628b/)

---

⭐ Feel free to fork, explore, and suggest improvements. Thanks for visiting!
