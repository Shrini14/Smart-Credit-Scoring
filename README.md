# Smart Credit Scoring

## 📌 Project Overview

The **Smart Credit Scoring** project builds a machine learning model to measure **credit risk**. The model predicts the probability of loan default based on customer, loan, and bureau data, enabling better lending decisions and improved risk management.

---

## 🎯 Objectives & Success Criteria

* **Objective:** Develop a model to assess the risk of loan default.
* **Success Criteria:**

  * AUC, Gini > **85**
  * KS statistic > **40**
  * Maximum KS statistic in first 3 deciles
  * Model should be interpretable and explainable

---

## 📂 Dataset

* **Source:** Past two years of loan data
* **Time Frame:**

  * Training & validation: Feb 2022 – Feb 2024
  * Out-of-time validation: Mar 2024 – May 2024
* **Split:** 75% training, 25% test

### Features

* **Customer Data** – demographics, employment, income
* **Loan Data** – purpose, amount, term, repayment history
* **Bureau Data** – credit history, existing obligations

---

## ⚙️ Data Preprocessing

* Handled invalid values (e.g., missing loan purposes replaced with mode)
* Feature selection using **Information Value (IV)**, **Variance Inflation Factor (VIF)**, and domain expertise
* Scaling of numeric features using **Min-Max Normalization**

---

## 🤖 Modeling Approach

* **Algorithms Tested:** Logistic Regression, Random Forest, XGBoost
* **Hyperparameter Tuning:** RandomizedSearchCV, Optuna
* **Evaluation Metrics:** AUC, KS Statistic, Gini Coefficient, Classification Report

---

## 📊 Results

* Achieved strong discriminatory power with AUC, Gini, and KS statistics meeting the success criteria.
* Best results were obtained in the **first 3 deciles**, making the model effective in identifying high-risk customers.

### 🔑 Feature Importance (Final Logistic Regression Model)

The most important predictors of loan default were:

* **loan\_to\_income** (highest impact)
* **credit\_utilization\_ratio**
* **delinquency\_ratio**
* **avg\_dpd\_per\_delinquency**
* Supporting factors: residence type, loan type, loan purpose, and number of open accounts.

Negative coefficients (e.g., **loan\_purpose\_Home**, **residence\_type\_Owned**) indicate features that **reduce the likelihood of default**.

📌 For deeper analysis and insights, please check the attached Jupyter Notebook (`Credit_risk_model.ipynb`).

---

## 🚀 Application

You can try out the live application here:
👉 [Smart Credit Scoring App](https://smart-credit-scoring.streamlit.app/)

---

## 🙌 Credits

Project designed and developed by **Shrinivass Raju**.

---



