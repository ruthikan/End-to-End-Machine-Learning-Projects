# Medical Insurance Charges Prediction using Linear Regression

This project aims to predict the medical insurance charges a person might incur based on their personal attributes using Linear Regression. The dataset includes demographic information like age, BMI, sex, smoking status, region, etc.

---

## Project Overview

- Problem Type: Regression  
- Objective: Predict the "charges" (insurance cost) column  
- Dataset: insurance.csv 

---

## Features in Dataset

| Feature         | Description                          |
|-----------------|--------------------------------------|
| age             | Age of the individual (numeric)      |
| sex             | Gender (male/female)                 |
| bmi             | Body mass index                      |
| children        | Number of children covered by insurance |
| smoker          | Smoking status (yes/no)              |
| region          | Residential region                   |
| charges         | Medical charges (Target Variable)    |

---

## EDA & Data Preprocessing

- ✔ Checked for missing values (None found)
- ✔ Visualized data distribution (boxplots, histograms)
- ✔ Detected and handled outliers using IQR method
- ✔ Converted categorical columns using Label Encoding
- ✔ Split data into train/test sets (80/20)

---

## Model: Linear Regression

- Imported LinearRegression from scikit-learn
- Trained on the preprocessed training set
- Made predictions on the test set
- Evaluated the model using:
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)
  - R² Score

---

## Model Evaluation

| Metric   | Score           |
|----------|------------------|
| MSE      | 587936.1964791534 |
| RMSE     | 766.7699762504745 |
| R² Score | 95.92307201834575 |

Interpretation: A high R² score indicates the model explains a large proportion of the variance in insurance charges.

---

## Visualization

- Scatter plot of predicted vs actual charges
- Distribution plot of residuals
- Feature vs Target correlation heatmap

---

## Key Learnings

- Understood the linear relationship between input features and output variable
- Learned how outliers can skew regression models
- Gained hands-on experience in model evaluation using real-world metrics
- Practiced feature encoding, model fitting, and visualization techniques

---

## Tools & Libraries

- Python 3
- pandas, numpy
- matplotlib, seaborn
- scikit-learn

---

## About Me

Hi, I’m Ruthika Nalajala – an aspiring Machine Learning Engineer currently learning through Intellipaat and hands-on projects.  
This is part of my end-to-end ML portfolio for showcasing practical knowledge.

🔗 Let’s connect on [LinkedIn](https://www.linkedin.com/in/ruthika-nalajala-73127628b/)

---

⭐ Feel free to fork, star, or raise issues/suggestions. Thanks for visiting this project!


