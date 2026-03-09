# Retail Store Sales Analysis & Dashboard

![Python](https://img.shields.io/badge/python-3.11-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.25-orange)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Project Overview

This project analyzes over **12,000 retail transactions** to uncover patterns in customer spending and product sales.  
The goal is to clean and analyze the data and build an **interactive dashboard** for exploring insights.  

The project combines **data cleaning, exploratory data analysis (EDA), and dashboard development** using Python.

---

## Dataset

The dataset contains **12,575 retail transactions** with the following variables:

- Transaction ID  
- Customer ID  
- Category  
- Item  
- Price Per Unit  
- Quantity  
- Total Spent  
- Payment Method  
- Location (Online or In-Store)  
- Transaction Date  
- Discount Applied  

The dataset initially contained **missing values and inconsistent data types**, which required preprocessing before analysis.  

**Source:** [Kaggle – Retail Store Sales Dirty Dataset](https://www.kaggle.com/datasets/ahmedmohamed2003/retail-store-sales-dirty-for-data-cleaning)

---

## Data Cleaning

Key preprocessing steps:

- Convert **Transaction Date** to datetime format  
- Handle missing **Price Per Unit** and **Quantity** with column mean  
- Fill missing **Item** values with `"Unknown"`  
- Recalculate **Total Spent = Price Per Unit × Quantity**  
- Create time-based features (**Year, Month, Day of Week**)  
- Convert **Discount Applied** into boolean  
- Remove identifiers (**Transaction ID, Customer ID**)  
- Encode categorical variables (**one-hot encoding**)  
- Standardize numerical variables using **StandardScaler**

---

## Exploratory Data Analysis

Visualizations created using:

- **Matplotlib**  
- **Seaborn**  
- **Plotly**  

Key analyses:

- Distribution of **Total Spent**  
- Category and payment method distributions  
- Relationship between **Price Per Unit, Quantity, and Total Spent**  
- Impact of **discounts** on spending behavior  
- Comparison of **online vs in-store transactions**  
- Top performing product categories and items  

---

## Key Insights

- **Quantity drives revenue**: Customers buying more items contribute most to total revenue  
- **Online transactions slightly higher**: Higher average transaction value compared to in-store  
- **Discounts have minimal impact**: Discounts did not significantly increase spending  
- **Revenue stable across the week**: Slight spike on Fridays; overall fairly even  

---

## Interactive Dashboard

Built using **Streamlit**. Features include:

- Dataset preview  
- Key performance metrics  
- Monthly sales trends  
- Revenue by category  
- Discount impact on spending  
- Online vs in-store comparison  
- Correlation heatmap  
- Top selling items  

**Screenshot Placeholder:**  
![Dashboard Preview](screenshots/dashboard_preview.png)

---

## Technologies Used

- **Python**  
- **Pandas**  
- **Matplotlib & Seaborn**  
- **Plotly**  
- **Streamlit**  
- **Scikit-learn**  

---

## Project Structure

```text
retail-sales-analysis/
│
├─ data/                 # Raw and cleaned datasets
│  ├─ raw/               # Original dataset
│  └─ cleaned/           # Preprocessed dataset
│
├─ colab_notebooks/      # Google Colab notebooks for EDA
│  └─ eda_analysis.ipynb
│
├─ app.py                # Streamlit dashboard
├─ requirements.txt      # Python dependencies
├─ README.md             # Project documentation
└─ .gitignore            # Git ignore file