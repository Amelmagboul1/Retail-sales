import streamlit as st
import pandas as pd

st.title("Retail Store Sales Dashboard")

df = pd.read_csv("04_retail_store_sales.csv")


st.subheader("Dataset Preview")
st.dataframe(df.head())

df_cleancopy = df.copy()
st.sidebar.header("Filters")

category_filter = st.sidebar.multiselect(
    "Category",
    options=df_cleancopy["Category"].unique(),
    default=df_cleancopy["Category"].unique()
)

payment_filter = st.sidebar.multiselect(
    "Payment Method",
    options=df_cleancopy["Payment Method"].unique(),
    default=df_cleancopy["Payment Method"].unique()
)

filtered_df = df_cleancopy[
    (df_cleancopy["Category"].isin(category_filter)) &
    (df_cleancopy["Payment Method"].isin(payment_filter))
]

st.header("Data Cleaning")

df_cleancopy['Transaction Date'] = pd.to_datetime(df_cleancopy['Transaction Date'], errors='coerce')

st.success("Data loaded successfully!")
import matplotlib.pyplot as plt

st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

total_revenue = filtered_df["Total Spent"].sum()
total_transactions = filtered_df["Transaction ID"].nunique()
avg_order_value = filtered_df["Total Spent"].mean()


col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Transactions", total_transactions)
col3.metric("Average Order Value", f"${avg_order_value:,.2f}")

st.header("Total Spending Distribution")

fig, ax = plt.subplots()
ax.hist(df_cleancopy['Total Spent'], bins=20)
ax.set_xlabel("Total Spent")
ax.set_ylabel("Frequency")

st.pyplot(fig)


st.subheader("Monthly Sales Trend")


monthly_sales = filtered_df.groupby(
    df_cleancopy["Transaction Date"].dt.to_period("M")
)["Total Spent"].sum()

monthly_sales.index = monthly_sales.index.astype(str)

st.line_chart(monthly_sales)

import seaborn as sns

st.header("Correlation Between Numerical Features")

corr = df_cleancopy[['Price Per Unit','Quantity','Total Spent']].corr()

fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

st.pyplot(fig)

st.header("Sales by Category")

category_sales = filtered_df.groupby("Category")["Total Spent"].sum().sort_values()

st.bar_chart(category_sales)

st.header("Payment Method Distribution")

payment_counts = filtered_df["Payment Method"].value_counts()

st.bar_chart(payment_counts)



st.header("Average Transaction Value by Location")

avg_loc = df_cleancopy.groupby('Location')['Total Spent'].mean()

st.bar_chart(avg_loc)

st.header("Impact of Discounts on Spending")

discount_avg = df_cleancopy.groupby("Discount Applied")["Total Spent"].mean()

st.bar_chart(discount_avg)

st.header("Top 10 Selling Items")

top_items = (
    df_cleancopy[df_cleancopy["Item"] != "Unknown"]
    .groupby("Item")["Total Spent"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_items)

st.header("Explore Transactions")

st.dataframe(filtered_df)

st.header("Key Insights")

st.write("""
• Quantity is the strongest driver of revenue.

• Online purchases generate slightly higher transaction values than in-store.

• Discounts have minimal effect on customer spending behavior.

• Revenue is driven by transaction volume rather than price increases.
""")



