# 🩺 Disease Prediction using K-Nearest Neighbors (KNN)

This project uses the K-Nearest Neighbors (KNN) algorithm to predict diseases based on the symptoms provided by a patient. It's a multi-class classification problem that demonstrates how distance-based algorithms can be applied in healthcare scenarios.

---

## 📁 Project Overview

- 📊 Problem Type: Multi-class Classification  
- 🎯 Objective: Predict the most likely disease using symptoms  
- 📂 Dataset: Symptom-to-Disease Dataset (medical.csv or dataset.csv)  
- 🧪 Algorithm: K-Nearest Neighbors using scikit-learn

---

## 🔍 Dataset Description

| Feature Name   | Description                             |
|----------------|------------------------------------------|
| Symptom_1–6    | Categorical symptoms (e.g., vomiting, fatigue, etc.) |
| Disease        | Target variable (diagnosed disease)      |
| Classes        | 40+ different diseases                   |

Each row in the dataset represents a patient case with up to six symptoms and the corresponding diagnosed disease.

---

## 🔧 Workflow Steps

1. ✅ Loaded and cleaned the dataset  
2. ✅ Retained only required columns (Symptom_1 to Symptom_6 and Disease)  
3. ✅ Filled missing values with the mode (most common symptom)  
4. ✅ Applied Label Encoding to symptoms and disease names  
5. ✅ Split data into training and testing sets (80/20 split)  
6. ✅ Trained KNeighborsClassifier from scikit-learn  
7. ✅ Tested the model on unseen test data  
8. ✅ Measured performance using Accuracy Score

---

## 📐 Distance Metrics Covered

- Euclidean Distance  
- Manhattan Distance  
- Minkowski Distance

🧪 In this implementation, Euclidean distance was used by default to find the nearest neighbors.

---

## 📈 Model Performance

| Metric          | Result        |
|------------------|---------------|
| Train Accuracy   | 99.62%        |
| Test Accuracy    | 98.47% ✅     |
| Neighbors (K)    | 5             |
| Distance Metric  | Euclidean     |

The model was able to generalize well and predict the correct disease based on symptoms in most test cases.

---

## 🧠 Key Learnings

- Understood how KNN classifies a data point by voting among k-nearest neighbors  
- Learned how to tune k-value and choose distance metrics  
- Understood pros and cons of instance-based learning  
- Demonstrated how a simple algorithm like KNN can be effective for medical predictions

---

## 📚 Tools & Libraries

- Python 3  
- pandas, numpy  
- scikit-learn  
- Jupyter Notebook / Google Colab


---

## 🙋‍♀️ About Me

Hi, I’m Ruthika Nalajala — an aspiring Machine Learning Engineer building real-world projects as part of my learning journey through IntelPath and self-study. This project is one of many in my growing ML portfolio.

📬 Let’s connect on [LinkedIn](https://linkedin.com/in/ruthika-nalajala-73127628b) (replace with your profile link)

---

⭐ Feel free to explore, fork, or improve this project. Thanks for visiting!

