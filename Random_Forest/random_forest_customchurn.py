# -*- coding: utf-8 -*-
"""Random_forest_customchurn.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ATuKT_Ogp2TJaZdo7Ucg7VU8ATOfRrID

##**1.Importing libraries**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

df=pd.read_csv('customer_churn_.csv')
df

"""# customerID: A unique identifier for each customer.
# gender: The gender of the customer (Male/Female).
# SeniorCitizen: Indicates if the customer is a senior citizen (1 = Yes, 0 = No).
# Partner: Indicates if the customer has a partner (Yes/No).
# Dependents: Indicates if the customer has dependents (Yes/No).
# tenure: Number of months the customer has stayed with the company.
# PhoneService: Indicates if the customer has a phone service (Yes/No).
# MultipleLines: Indicates if the customer has multiple lines (Yes/No/No phone service).
# InternetService: Type of internet service (DSL, Fiber optic, None).
# OnlineSecurity: Indicates if the customer has online security add-ons (Yes/No/No internet service).
# DeviceProtection: Indicates if the customer has device protection add-ons (Yes/No/No internet service).
# TechSupport: Indicates if the customer has tech support add-ons (Yes/No/No internet service).
# StreamingTV: Indicates if the customer streams TV services (Yes/No/No internet service).
# StreamingMovies: Indicates if the customer streams movies (Yes/No/No internet service).
# Contract: Type of contract (Month-to-month, One year, Two year).
# PaperlessBilling: Indicates if the customer uses paperless billing (Yes/No).
# PaymentMethod: The payment method used (e.g., Electronic check, Mailed check, Bank transfer, Credit card).
# MonthlyCharges: Monthly charges for the customer.
# TotalCharges: Total charges billed to the customer.
# Churn: Indicates if the customer has churned (Yes/No).

##**2.EDA**
"""

df.isnull().sum().sum()

df.duplicated().sum()

df.info()

#df['TotalCharges']=df['TotalCharges'].astype(float) - could not convert string to float

df['TotalCharges']=pd.to_numeric(df['TotalCharges'],errors='coerce')

df.isnull().sum()

df.dropna(inplace=True)
df.isnull().sum().sum()

from sklearn.preprocessing import LabelEncoder

Le=LabelEncoder()
for col in df.columns:
  df[col]=Le.fit_transform(df[col])

df.info()

"""##**3.Model Building**"""

x=df.drop('Churn',axis=1)
y=df['Churn']

x

y

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=34)

model=RandomForestClassifier(n_estimators=50,random_state=23)

model.fit(x_train,y_train)

y_pred=model.predict(x_test)
y_pred

accuracy_score(y_test,y_pred)*100

"""##**GridSearchCV**"""

# GridSearchCV is a powerful tool in scikit-learn that allows for exhaustive search
# over specified parameter values for an estimator

from sklearn.model_selection  import GridSearchCV

base_model=RandomForestClassifier(random_state=23)

param_grid={
    'n_estimators':[100,200,300],
    'max_depth':[1,5,10],
    'min_samples_split':[2,5,7],
    'min_samples_leaf':[1,2,4],
    'criterion':['gini','entropy']
}

grid_search=GridSearchCV(estimator=base_model,param_grid=param_grid)

grid_search.fit(x_train,y_train)

print(grid_search.best_params_)

final_model=RandomForestClassifier(n_estimators=300,max_depth=10,min_samples_leaf=4,min_samples_split=2,criterion= 'entropy',random_state=23)

final_model.fit(x_train,y_train)

y_pred_final=final_model.predict(x_test)

accuracy_score(y_test,y_pred_final)*100