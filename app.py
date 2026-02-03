import streamlit as st
import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Customer Churn Analysis Dashboard")

# Load cleaned data from SQLite
conn = sqlite3.connect("churn.db")
df = pd.read_sql("SELECT * FROM customer_churn", conn)
conn.close()

# Display sample
st.subheader("Sample Data")
st.dataframe(df.head())

# Insights
st.subheader("Key Insights")
insights = [
    "Month-to-month or short-term contract customers have higher churn rates.",
    "Customers with fewer services used are more likely to churn.",
    "High account length correlates with higher churn risk.",
]
for i, insight in enumerate(insights,1):
    st.write(f"{i}. {insight}")

# Churn distribution
st.subheader("Churn Distribution")
fig, ax = plt.subplots()
sns.countplot(x='Churn', data=df, ax=ax)
st.pyplot(fig)

# Feature importance (if model added)
st.subheader("Tenure vs Churn")
fig2, ax2 = plt.subplots()
sns.boxplot(x='Churn', y='tenure', data=df, ax=ax2)
st.pyplot(fig2)
