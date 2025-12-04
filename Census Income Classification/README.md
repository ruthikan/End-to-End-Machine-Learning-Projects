# 📊 Census Income Classification – UCI Adult Dataset

This project predicts whether an individual earns **more than $50K per year** using demographic and socioeconomic features from the **UCI Adult Census Dataset**.  
It uses multiple ML models to compare performance, along with proper preprocessing, feature engineering, and hyperparameter tuning.

---

## Project Overview
- **Problem Type:** Binary Classification  
- **Goal:** Predict if a person earns `>50K` annually  
- **Dataset:** UCI Adult Dataset  
- **Models Used:**  
  - Logistic Regression  
  - Decision Tree Classifier  
  - Random Forest Classifier  
  - RandomizedSearchCV for tuning  

---

## Dataset Description

**Features include:**
- Age  
- Workclass  
- Education / Education-Num  
- Marital Status  
- Occupation  
- Relationship  
- Race  
- Sex  
- Capital Gain / Capital Loss  
- Hours per Week  
- Native Country  

**Target Variable:**  
- `income` → `<=50K` or `>50K`

---

## Steps Performed

### **1. Data Cleaning & Preprocessing**
- Checked for missing values and cleaned inconsistent records  
- Detected and removed **outliers** in numerical columns  
- Applied **Label Encoding** to categorical variables  
- Converted target variable to binary format  

### **2. Exploratory Data Analysis (EDA)**
- Visualized distributions of age, education, occupation, and income classes  
- Explored relationships between education level and salary  
- Identified key patterns (e.g., more work hours correlating with higher income)  

### **3. Model Building**
Implemented and evaluated multiple models:
- **Logistic Regression**  
- **Decision Tree Classifier**  
- **Random Forest Classifier**  

Each model was trained on an **80/20 train–test split**.

### **4. Hyperparameter Tuning**
- Applied **RandomizedSearchCV** to tune Random Forest parameters  
- Used performance metrics to select the best model  

---

## Model Performance

| Model                     | Accuracy |
|---------------------------|----------|
| Logistic Regression       | ~83%     |
| Decision Tree             | ~80%     |
| Random Forest (Tuned)     | **~85%** |

➡️ **Random Forest with RandomizedSearchCV achieved the highest performance.**

---

## Key Learnings
- Handling mixed-type datasets (numerical + categorical)  
- Feature encoding for tree-based vs linear models  
- Impact of outliers on classification performance  
- Using **RandomizedSearchCV** for faster tuning on large datasets  
- Model comparison and performance interpretation  

---

## Tools & Libraries
- Python  
- pandas, numpy  
- scikit-learn  
- matplotlib, seaborn  
- RandomizedSearchCV  

---

## 👩‍💻 Author
**Ruthika Nalajala**  
Aspiring Machine Learning Engineer  
Learning ML & DL through Intellipaat and real-world projects.



