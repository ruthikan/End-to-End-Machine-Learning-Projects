# 🏏 Cricket Player Segmentation using K-Means Clustering

This project uses K-Means clustering to segment international cricket players based on their performance statistics. The goal is to identify distinct player types (e.g., aggressive batters, all-rounders, bowlers) using unsupervised learning.

---

## 📁 Project Overview

- 📊 Problem Type: Unsupervised Learning – Clustering  
- 🎯 Objective: Group players into meaningful clusters based on performance metrics  
- 📂 Dataset: cricket_clean.csv (preprocessed performance stats)

---

## 🔍 Features in Dataset

| Feature         | Description                            |
|------------------|----------------------------------------|
| Player Name      | Name of the cricketer                  |
| Matches Played   | Total matches played                   |
| Batting Average  | Average runs scored per innings        |
| Strike Rate      | Batting strike rate                    |
| Bowling Average  | Average runs conceded per wicket       |
| Economy Rate     | Bowling economy                        |
| ...              | Additional skill-based features        |

---

## 🔧 Workflow

1. ✅ Data Cleaning & Preprocessing  
2. ✅ Handled outliers using IQR and visual inspection  
3. ✅ Normalized features using StandardScaler  
4. ✅ Used Elbow Method & Silhouette Score to choose optimal K  
5. ✅ Applied KMeans Clustering with K=4  
6. ✅ Visualized clusters in 2D space using PCA-reduced components

---

## 📈 Results

- Optimal Clusters: 4  
- Cluster Distribution: Aggressive Batters, Balanced All-Rounders, Specialist Bowlers, Support Roles  
- Used PCA for dimensionality reduction before plotting

---

## 🧠 Key Learnings

- How K-Means works and the importance of normalization  
- How to determine optimal K using Elbow and Silhouette methods  
- PCA helps simplify visualization for high-dimensional data  
- Valuable insights can be derived from unsupervised learning on sports data

---

## 📚 Libraries Used

- Python 3  
- pandas, numpy  
- scikit-learn  
- matplotlib, seaborn

---

## 🙋‍♀️ About Me

Hi, I’m Ruthika Nalajala — a Machine Learning enthusiast building real-world projects as part of my IntelPath journey. This project is a part of my unsupervised learning series.
📬 Let’s connect on [LinkedIn](https://linkedin.com/in/ruthika-nalajala-73127628b)
