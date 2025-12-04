# 🎬 Netflix Movie Recommendation System (SVD)

This project builds a movie recommendation system using **Collaborative Filtering** and **Singular Value Decomposition (SVD)**. The goal is to predict user ratings and recommend movies based on learned user preferences and movie characteristics.

---

## Project Overview
- **Model Type:** Collaborative Filtering  
- **Algorithm:** Singular Value Decomposition (SVD)  
- **Dataset:** Netflix Ratings Dataset  
- Data contains:
  - `CustomerID`
  - `MovieID`
  - `Rating`
  - Timestamp (not used for modeling)

This dataset is sparse, making it suitable for matrix factorization methods like SVD.

---

## Steps Performed

### **1. Data Loading & Cleaning**
- Loaded the raw Netflix rating data.
- Extracted movie IDs from the text-based format.
- Removed missing or inconsistent rating entries.
- Filtered:
  - Movies with very few ratings  
  - Users with extremely low activity  
- Reduced dataset size using quantile-based thresholds for efficient training.

### **2. Exploratory Data Analysis**
- Observed rating distribution.
- Verified matrix sparsity.
- Constructed a **User–Movie Rating Matrix**.

### **3. Model Building – SVD**
- Used the **Surprise library** to implement SVD.
- Trained SVD to learn latent patterns of users and movies.
- Performed **3-fold cross-validation** using RMSE.
- Trained a final SVD model on the full processed dataset.

### **4. Generating Recommendations**
For any given user:
1. Predict ratings for movies the user has not rated.  
2. Rank predicted ratings in descending order.  
3. Recommend **Top-N movies**.  
4. Mapped movie IDs back to titles using `movie_titles.csv`.

---

## Results
- Successfully generated personalized movie recommendations.
- Achieved stable RMSE performance through cross-validation.
- Demonstrated how matrix factorization can uncover hidden user preferences.

---

## Key Learnings
- Understanding collaborative filtering and user–item interactions.
- Working with extremely sparse datasets.
- Applying SVD for dimensionality reduction in recommender systems.
- Building scalable recommendation pipelines using Surprise.
- Mapping predicted values back to meaningful movie titles.

---

## Tools Used
- Python  
- pandas, numpy  
- Surprise (SVD)  
- matplotlib, seaborn  
- Google Colab  

---

## 📂 Folder Structure

