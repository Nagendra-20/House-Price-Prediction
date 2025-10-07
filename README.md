#  House Price Prediction

###  Project ID: PRCP-1020-HousePricePred

---

##  Problem Statement

The goal of this project is to **analyze the factors affecting house prices** and develop a **robust machine learning model** capable of accurately predicting the price of a house based on various market and property-related attributes.

### Tasks:
- **Task 1:** Perform Exploratory Data Analysis (EDA) to understand data trends, patterns, and relationships.  
- **Task 2:**  
  a) Build and train a regression model to predict house prices.  
  b) Analyze feature importance and correlations among variables.

---

##  Project Workflow

1. **Data Understanding**
   - Loaded the dataset containing **1460 rows and 81 features**.
   - Inspected data types, missing values, and outliers.

2. **Data Preprocessing**
   - Handled missing values and categorical variables.
   - Performed feature encoding and normalization.
   - Removed irrelevant or redundant features.

3. **Exploratory Data Analysis (EDA)**
   - Studied distributions of numerical features.
   - Visualized correlations using heatmaps and pairplots.
   - Investigated the relationship between independent variables and the target variable (`SalePrice`).

4. **Feature Engineering**
   - Created new meaningful features (e.g., TotalSF = TotalSqFeet).
   - Transformed skewed data using log transformations.
   - Selected top contributing features for modeling.

5. **Model Building**
   - Implemented multiple regression algorithms:
     - Linear Regression  
     - Lasso Regression  
     - Ridge Regression  
     - Random Forest Regressor  
     - Gradient Boosting Regressor
   - Evaluated model performance using metrics such as **R² Score**, **MAE**, and **RMSE**.

6. **Model Evaluation**
   - Compared performance across models.
   - Tuned hyperparameters to achieve optimal accuracy.
   - Identified the most influential features impacting house prices.

---

##  Technologies & Tools

- **Python**
- **NumPy**, **Pandas**
- **Matplotlib**, **Seaborn**
- **Scikit-learn**
- **Jupyter Notebook**

