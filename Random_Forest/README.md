# Customer Churn Prediction using Random Forest Classifier

This project predicts whether a customer will churn based on their subscription, service, and account details. I implemented Random Forest — a powerful ensemble model — along with RandomizedSearchCV for hyperparameter tuning. This project is part of my ML journey through IntelPath.

---

## Project Overview

- Problem Type: Binary Classification  
- Objective: Predict whether a telecom customer will churn  
- Dataset: customer_churn.csv (7,043 rows × 21 columns)

---

## Features in Dataset

| Feature           | Description                                |
|-------------------|--------------------------------------------|
| gender            | Male or Female                             |
| SeniorCitizen     | Whether the customer is a senior citizen   |
| Partner           | Has a partner (Yes/No)                     |
| Dependents        | Has dependents (Yes/No)                    |
| tenure            | Number of months with the company          |
| PhoneService      | Whether phone service is active            |
| MultipleLines     | Whether customer has multiple lines        |
| InternetService   | Type of internet service                   |
| OnlineSecurity    | Whether online security is active          |
| ...               | ...more features (see dataset)             |
| TotalCharges      | Total bill amount (continuous)             |
| Churn             | Target variable (Yes = churned, No = retained) |

---

## Steps Performed

1. Loaded dataset and performed EDA  
2. Handled missing values in TotalCharges  
3. Removed customerID (irrelevant to prediction)  
4. Applied Label Encoding to all categorical variables  
5. Split data into training (80%) and testing (20%)  
6. Trained a baseline Random Forest model (n_estimators=50)  
7. Used RandomizedSearchCV to tune hyperparameters:
   - n_estimators
   - max_depth
   - min_samples_leaf
   - min_samples_split
   - criterion (gini/entropy)

---

## Hyperparameter Tuning (RandomizedSearchCV)

| Best Parameters Found | Value           |
|------------------------|----------------|
| n_estimators           | 300            |
| max_depth              | 10             |
| min_samples_leaf       | 4              |
| min_samples_split      | 2              |
| criterion              | entropy        |

---

## Model Evaluation

| Metric           | Score          |
|------------------|----------------|
| Baseline Accuracy | 77.82%         |
| Tuned Accuracy    | 78.96% ✅      |
| Confusion Matrix  | Included in notebook |
| Feature Importance | Visualized using barplot |

✅ Interpretation: Model performance improved after tuning. Features like tenure, Contract type, and MonthlyCharges had the highest influence on churn prediction.

---

## Visualizations

- Churn distribution plot  
- Feature importance ranking  
- Confusion matrix  
- Correlation heatmap

---

## Key Learnings

- Random Forest improves stability and accuracy over single Decision Trees by using Bagging  
- RandomizedSearchCV speeds up tuning on large datasets  
- Feature importance helps interpret what drives customer churn  
- Handling imbalanced data and categorical variables properly boosts model performance

---

## Tools & Libraries

- Python 3  
- pandas, numpy  
- matplotlib, seaborn  
- scikit-learn  
- RandomizedSearchCV

---

## About Me

Hi, I’m Ruthika Nalajala — a passionate Machine Learning Engineer in training, exploring real-world projects through Intellipaat and personal learning. I’m building a strong ML foundation with practical experience and clean documentation.

📬 Let’s connect on [LinkedIn](https://www.linkedin.com/in/ruthika-nalajala-73127628b/) 

---

⭐ Feel free to fork, explore, and share suggestions. Thanks for stopping by!
