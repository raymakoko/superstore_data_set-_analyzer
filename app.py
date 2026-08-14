import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

sns.set_style("whitegrid")


@st.cache_data
def load_data():
    df = pd.read_csv("data/Superstore.csv")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
    return df


def filter_data(df):
    regions = df["Region"].dropna().unique().tolist()
    categories = df["Category"].dropna().unique().tolist()
    segments = df["Segment"].dropna().unique().tolist()

    selected_region = st.sidebar.multiselect("Region", regions, default=regions)
    selected_category = st.sidebar.multiselect("Category", categories, default=categories)
    selected_segment = st.sidebar.multiselect("Segment", segments, default=segments)

    filtered = df[
        df["Region"].isin(selected_region)
        & df["Category"].isin(selected_category)
        & df["Segment"].isin(selected_segment)
    ].copy()

    return filtered


def main():
    st.set_page_config(page_title="Superstore Dashboard", page_icon="📊", layout="wide")
    st.title("Superstore Sales and Profit Dashboard")
    st.caption("A simple Streamlit dashboard built from the Superstore dataset.")

    df = load_data()
    filtered = filter_data(df)

    if filtered.empty:
        st.warning("No data matches the selected filters.")
        return

    total_sales = filtered["Sales"].sum()
    total_profit = filtered["Profit"].sum()
    avg_discount = filtered["Discount"].mean() * 100
    order_count = filtered.shape[0]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Sales", f"${total_sales:,.0f}")
    col2.metric("Total Profit", f"${total_profit:,.0f}")
    col3.metric("Avg. Discount", f"{avg_discount:.1f}%")
    col4.metric("Orders", f"{order_count:,}")

    sales_by_region = filtered.groupby("Region", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)
    profit_by_category = filtered.groupby("Category", as_index=False)["Profit"].sum().sort_values("Profit", ascending=False)

    monthly = filtered.assign(Month=filtered["Order Date"].dt.to_period("M").astype(str))
    monthly_profit = monthly.groupby("Month", as_index=False)["Profit"].sum()

    col5, col6 = st.columns(2)

    with col5:
        st.subheader("Sales by Region")
        fig, ax = plt.subplots(figsize=(7, 4))
        sns.barplot(data=sales_by_region, x="Sales", y="Region", palette="viridis", ax=ax)
        ax.set_xlabel("Sales")
        ax.set_ylabel("Region")
        st.pyplot(fig)

    with col6:
        st.subheader("Profit by Category")
        fig, ax = plt.subplots(figsize=(7, 4))
        sns.barplot(data=profit_by_category, x="Profit", y="Category", palette="magma", ax=ax)
        ax.set_xlabel("Profit")
        ax.set_ylabel("Category")
        st.pyplot(fig)

    st.subheader("Monthly Profit Trend")
    fig, ax = plt.subplots(figsize=(12, 4))
    sns.lineplot(data=monthly_profit, x="Month", y="Profit", marker="o", ax=ax)
    ax.set_xlabel("Month")
    ax.set_ylabel("Profit")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.subheader("Discount vs Profit")
    scatter = filtered[["Discount", "Profit", "Sales", "Category"]].copy()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(data=scatter, x="Discount", y="Profit", hue="Category", alpha=0.8, ax=ax)
    ax.set_xlabel("Discount")
    ax.set_ylabel("Profit")
    st.pyplot(fig)

    st.subheader("Filtered Data Preview")
    st.dataframe(filtered.head(50), use_container_width=True)


if __name__ == "__main__":
    main()
