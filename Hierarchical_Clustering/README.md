# 🛍️ Customer Segmentation using Hierarchical Clustering

This project applies Hierarchical Clustering to segment mall customers based on their income and spending behavior. The goal is to identify distinct customer groups for targeted marketing strategies.

---

## 📁 Project Overview

- 📊 Problem Type: Unsupervised Learning – Clustering  
- 🎯 Objective: Segment mall customers into distinct groups  
- 📂 Dataset: Mall_Customers.csv  
- 🧪 Model: Agglomerative Hierarchical Clustering

---

## 🔍 Dataset Features

| Feature Name     | Description                     |
|------------------|---------------------------------|
| CustomerID       | Unique customer identifier      |
| Gender           | Male / Female                   |
| Age              | Age of the customer             |
| Annual Income    | Income in thousands (k$)        |
| Spending Score   | Score (1–100) assigned by mall  |

---

## 🔧 Workflow

1. ✅ Loaded and cleaned the dataset  
2. ✅ Selected relevant features: Annual Income & Spending Score  
3. ✅ Used Dendrogram (Ward linkage) to determine number of clusters  
4. ✅ Applied Agglomerative Clustering (Euclidean distance)  
5. ✅ Visualized clusters using scatter plot

---

## 📈 Results

- Optimal Clusters: 5  
- Interpretation:
  - Cluster 1: High income, high spenders  
  - Cluster 2: High income, low spenders  
  - Cluster 3: Low income, low spenders  
  - Cluster 4: Average earners, moderate spenders  
  - Cluster 5: Young high-value customers

---

## 🧠 Key Learnings

- Understood how hierarchical clustering groups data based on similarity  
- Dendrograms help decide the number of clusters  
- Agglomerative Clustering is intuitive for customer segmentation use cases  
- Useful for customer targeting, loyalty programs, and promotions

---

## 📚 Libraries Used

- Python 3  
- pandas, numpy  
- matplotlib, seaborn  
- scipy, scikit-learn

---

## 🙋‍♀️ About Me

Hi, I’m Ruthika Nalajala — an aspiring ML Engineer, passionate about solving business problems with data. This project is part of my unsupervised learning portfolio under IntelPath training.

📬 Let’s connect on [LinkedIn](https://linkedin.com/in/ruthika-nalajala-73127628b)
