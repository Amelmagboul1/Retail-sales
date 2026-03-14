import streamlit as st
import pandas as pd


df = pd.read_csv("04_retail_store_sales.csv")
df_cleancopy = df.copy()
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Overview", "Plots", "Insights"]
)
min_spent = int(df_cleancopy["Total Spent"].min())
max_spent = int(df_cleancopy["Total Spent"].max())

spent_range = st.sidebar.slider(
    "Total Spent Range",
    min_value=min_spent,
    max_value=max_spent,
    value=(min_spent, max_spent)
)
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
if page == "Overview":
   st.title("Retail Store Sales Dashboard")

   st.markdown("### Interactive Retail Sales Analysis Dashboard")
   st.write("Use the filters on the left to explore sales performance, customer behavior, and product trends.")
   st.header("Dataset Preview")
   st.dataframe(df_cleancopy.head())

   st.subheader("Key Metrics")

   col1, col2, col3 = st.columns(3)

   total_revenue = filtered_df["Total Spent"].sum()
   total_transactions = filtered_df["Transaction ID"].nunique()
   avg_order_value = filtered_df["Total Spent"].mean()

   col1.metric("Total Revenue", f"${total_revenue:,.2f}")
   col2.metric("Total Transactions", total_transactions)
   col3.metric("Average Order Value", f"${avg_order_value:,.2f}")

   st.header("Explore Transactions")
   st.dataframe(filtered_df)
import matplotlib.pyplot as plt
import seaborn as sns
  
if page == "Plots":
    st.header("Explore univariate, bivariate, and multivariate relationships in the retail dataset.")

    tab1, tab2, tab3 = st.tabs([
        "Univariate Analysis",
        "Bivariate Analysis",
        "Multivariate Analysis"
    ])
    with tab1:

        st.subheader("Total Spending Distribution")

        fig, ax = plt.subplots()
        ax.hist(filtered_df['Total Spent'], bins=20)
        st.pyplot(fig)

        st.subheader("Sales by Category")

        category_sales = filtered_df.groupby("Category")["Total Spent"].sum()
        st.bar_chart(category_sales)

        st.subheader("Payment Method Distribution")

        payment_counts = filtered_df["Payment Method"].value_counts()
        st.bar_chart(payment_counts)
        with tab2:

         st.subheader("Average Transaction Value by Location")

         avg_loc = filtered_df.groupby('Location')['Total Spent'].mean()
         st.bar_chart(avg_loc)

         st.subheader("Impact of Discounts on Spending")

         discount_avg = filtered_df.groupby("Discount Applied")["Total Spent"].mean()
         st.bar_chart(discount_avg)

         st.subheader("Monthly Sales Trend")

         filtered_df["Transaction Date"] = pd.to_datetime(filtered_df["Transaction Date"])

         Yearly_sales = filtered_df.groupby(
            filtered_df["Transaction Date"].dt.to_period("Y")
         )["Total Spent"].sum()

         Yearly_sales.index = Yearly_sales.index.astype(str)

         st.line_chart(Yearly_sales)
        with tab3:

         st.subheader("Correlation Heatmap")

         corr = filtered_df[['Price Per Unit','Quantity','Total Spent']].corr()

         fig, ax = plt.subplots(figsize=(8,5))
         sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
         st.pyplot(fig)

         st.subheader("Top 10 Selling Items")

         top_items = (
            filtered_df[filtered_df["Item"] != "Unknown"]
            .groupby("Item")["Total Spent"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

         st.bar_chart(top_items)
if page == "Insights":
   st.header("Summary of the most important findings from the retail sales analysis.")
   st.header("Key Insights")
   st.write("""
    • Quantity is the strongest driver of revenue.

    • Online purchases generate slightly higher transaction values than in-store.

    • Discounts have minimal effect on customer spending behavior.

    • Revenue is driven primarily by transaction volume rather than price increases.
    """)

