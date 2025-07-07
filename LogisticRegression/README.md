# 🔐 Bank Marketing Term Deposit Prediction using Logistic Regression

This project uses Logistic Regression to predict whether a client will subscribe to a term deposit based on their demographic and campaign-related features. The dataset is sourced from a Portuguese banking institution.

---

## 📁 Project Overview

- 📊 Problem Type: Binary Classification  
- 🎯 Objective: Predict the target variable y (yes/no for term deposit subscription)  
- 📂 Dataset: bank.csv (UCI Bank Marketing Dataset)

---

## 🔍 Features in Dataset

| Feature         | Description                             |
|-----------------|-----------------------------------------|
| age             | Age of the client                       |
| job             | Job type                                |
| marital         | Marital status                          |
| education       | Education level                         |
| default         | Has credit in default?                  |
| balance         | Average yearly balance                  |
| housing         | Has housing loan?                       |
| loan            | Has personal loan?                      |
| contact         | Type of communication                   |
| day/month       | Last contact day/month                  |
| duration        | Last contact duration                   |
| campaign        | Number of contacts during this campaign |
| pdays           | Days since last contact                 |
| previous        | Number of contacts before this campaign |
| poutcome        | Previous campaign outcome               |
| y               | Target: has subscribed (yes/no)         |

---

## 🔧 Steps Performed

1. ✅ Handled missing data & verified nulls  
2. ✅ Removed 1,784 duplicate entries  
3. ✅ Detected and treated outliers using IQR  
4. ✅ Applied Label Encoding to categorical variables  
5. ✅ Dropped irrelevant columns like pdays, poutcome, etc. (based on high VIF)  
6. ✅ Checked for multicollinearity using Variance Inflation Factor (VIF)  
7. ✅ Split data using train_test_split (70% train, 30% test)  
8. ✅ Built and trained Logistic Regression model using scikit-learn

---

## 📈 Model Evaluation

| Metric             | Result       |
|--------------------|--------------|
| Accuracy Score     | ~88.48%      |
| Confusion Matrix   | [[9558, 25], [1225, 46]] |
| Precision / Recall | Calculated using classification report |

✅ Interpretation: The model performs well, though slightly imbalanced in predicting the "yes" class. Could be improved further with class weighting or ensemble models.

---

## 📊 Visualization

- Bar plots of categorical features vs target  
- Heatmap of feature correlations  
- Confusion Matrix

---

## 🧠 Key Learnings

- Understood how Logistic Regression uses the sigmoid function to map probabilities  
- Learned how to reduce multicollinearity using VIF  
- Practiced feature encoding and interpretation of confusion matrix  
- Realized the importance of duration and previous contact success in predicting customer behavior

---

## 📚 Tools & Libraries

- Python 3  
- pandas, numpy  
- seaborn, matplotlib  
- scikit-learn  
- statsmodels (for VIF)

---

## 🙋‍♀️ About Me

Hi, I’m Ruthika Nalajala — an aspiring Machine Learning Engineer actively working through IntelPath and personal projects to build practical skills in predictive modeling.

📬 Connect on [LinkedIn](https://www.linkedin.com/in/ruthika-nalajala-73127628b/) 

---

⭐ Feel free to explore, fork, or suggest improvements. Thanks for visiting!
