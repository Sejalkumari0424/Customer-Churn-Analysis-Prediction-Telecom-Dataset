# Customer-Churn-Analysis-Prediction-Telecom-Dataset

## Project Objective

The goal of this project is to analyze customer churn patterns for a telecom company, identify key factors influencing churn, and build a predictive model to forecast potential churners. By combining **data engineering, analytics, and machine learning**, this project provides actionable insights to reduce churn, improve customer retention, and guide business decisions.

---

## Dataset Used

This project uses two complementary datasets from the **Orange Telecom Churn dataset collection**:

1. **`churn-bigml-80.csv`** – Training dataset (~80% of customers)  
2. **`churn-bigml-20.csv`** – Testing dataset (~20% of customers)  

The combined dataset includes customer demographics, service usage patterns, account information, and historical churn labels. Handling **multi-file data** simulates a real-world business scenario, allowing for realistic train/test splits and comprehensive analytics.

---

## Project Workflow

The project follows an **end-to-end pipeline**:

### 1. ETL (Extract, Transform, Load)

- Load **training and testing datasets** into Pandas DataFrames.  
- Handle missing values, duplicates, and inconsistent data formats.  
- Convert categorical variables to numeric or category types for analysis.  
- Feature engineering:  
  - **Tenure buckets** (0–1 year, 1–2 years, 2+ years)  
  - **Total services used** by each customer  
  - **High account charge flag** for monthly billing insights  
- Store cleaned data in **SQLite** for easy aggregation and SQL-based analysis.

---

### 2. Exploratory Data Analysis (EDA)

- Visualize churn distribution across customer segments.  
- Analyze **tenure, contract type, and service usage** against churn rates.  
- Identify patterns and correlations that provide business insights.  
- Generate plots using **Matplotlib** and **Seaborn** to support findings.

---

### 3. Predictive Modeling (Optional)

- Use **Random Forest Classifier** to predict churn on unseen data.  
- Train on `churn-bigml-80.csv` and validate on `churn-bigml-20.csv`.  
- Evaluate model using **accuracy, precision, recall, F1-score, and ROC-AUC**.  
- Analyze **feature importance** to understand which factors contribute most to churn.

---

### 4. Insights & Recommendations

- **Short-term contracts** have the highest churn rates → consider retention offers.  
- Customers using **fewer services** are more likely to churn → upsell additional services.  
- High account charges correlate with churn → explore loyalty programs or discounts.  
- **Tenure is a key indicator** → focus on improving early customer experience.

These insights enable **data-driven business decisions** for reducing churn and improving customer satisfaction.

---

### Optional Extension: Interactive Dashboard

- The project can be extended to an **interactive dashboard** using **Streamlit or Power BI**.  
- The dashboard would allow stakeholders to filter by **contract type, tenure, and service usage** and visualize churn trends in real-time.  
- This feature enhances **stakeholder engagement** and demonstrates the practical application of analytics.

---

## Key Takeaways

- Demonstrates **full data analytics lifecycle**: ETL → EDA → Modeling → Insights.  
- Handles **realistic multi-file datasets** with preprocessing and SQL integration.  
- Provides **actionable, business-oriented recommendations**.  
- Optional dashboard deployment highlights **presentation and deployment skills**.
