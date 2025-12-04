# 🌳 Heart Disease Prediction using Decision Tree Classifier

This project aims to predict whether a patient is likely to develop heart disease based on medical and demographic features. The model used is a Decision Tree Classifier, which is highly interpretable and effective for classification problems.

---

## Project Overview

- Problem Type: Binary Classification  
- Objective: Predict the presence (1) or absence (0) of heart disease  
- Dataset: heart.csv (UCI Heart Disease Dataset)

---

## Features in Dataset

| Feature     | Description                                      |
|-------------|--------------------------------------------------|
| age         | Age of the patient                               |
| sex         | Gender (0 = female, 1 = male)                    |
| cp          | Chest pain type (categorical: 0–3)              |
| trestbps    | Resting blood pressure                           |
| chol        | Serum cholesterol level                          |
| fbs         | Fasting blood sugar > 120 mg/dl (1 = true, 0 = false) |
| restecg     | Resting ECG results                              |
| thalach     | Maximum heart rate achieved                      |
| exang       | Exercise-induced angina (1 = yes, 0 = no)       |
| oldpeak     | ST depression induced by exercise                |
| slope       | Slope of peak exercise ST segment                |
| ca          | Number of major vessels (0–3)                    |
| thal        | Thalassemia (0 = normal, 1 = fixed, 2 = reversible) |
| target      | Diagnosis of heart disease (1 = disease, 0 = no disease) |

---

##  Steps Performed

1. Loaded and explored dataset (703 rows × 14 columns)  
2. Verified no missing/null values  
3. Dropped 1 duplicate row  
4. No encoding needed (dataset already numerical)  
5. Split data into 80% training and 20% testing  
6. Built Decision Tree Classifier using scikit-learn  
7. Tuned max_depth parameter (1–10) to prevent overfitting  
8. Visualized decision tree structure and feature splits

---

## Model Evaluation

| Metric           | Score         |
|------------------|---------------|
| Accuracy Score   | 80.32%        |
| Best max_depth   | 8             |
| Confusion Matrix | [[TN, FP], [FN, TP]] format included in notebook |

Interpretation: A max_depth of 8 gave the best performance, balancing bias and variance.

---

## Visualization

- Decision Tree plotted using plot_tree  
- Feature importance ranking  
- Correlation heatmap (EDA)

---

## Key Learnings

- Decision Trees split data based on feature purity (homogeneity)  
- Learned about ID3 and CART algorithms (Information Gain vs Gini Index)  
- Understood pruning (max_depth) as a method to reduce overfitting  
- Visualizing the tree makes it easy to interpret how decisions are made

---

## Tools & Libraries

- Python 3  
- pandas, numpy  
- matplotlib, seaborn  
- scikit-learn

---

## About Me

Hi, I’m Ruthika Nalajala — an aspiring Machine Learning Engineer on a mission to build impactful AI solutions. This project is part of my ML journey through Intellipaat and personal practice.

📬 Connect with me on [LinkedIn](https://www.linkedin.com/in/ruthika-nalajala-73127628b/)

---

⭐ Feel free to fork this repo, explore the notebook, and suggest improvements. Thanks for visiting!
