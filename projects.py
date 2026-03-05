import streamlit as st
import pandas as pd
import plotly.express as px



def show_projects():

    st.title("📁 Projects Portfolio")
    st.write("Interactive demonstrations of selected data analysis projects.")

    # ============================================================
    # PROJECT 1 — SUPER STORE SALES ANALYSIS
    # ============================================================

    with st.expander("📊 Super Store Sales Analysis", expanded=False):

        st.write(
        "Exploratory Data Analysis of retail sales data to identify "
        "high-performing states, profit trends, and global sales distribution."
        )

        st.link_button(
        "🔗 View on GitHub",
        "https://github.com/Tushar-Patil28/Super_Store_Sales-Only-Visualization-"
        )

        df = pd.read_csv("sales.csv")
        df.columns = df.columns.str.strip().str.lower()

        # ---------- SALES VS PROFIT ---------- #

        st.subheader("Top 10 States — Sales vs Profit")

        top_states = (
            df.groupby("state")[["sales", "profit"]]
            .sum()
            .nlargest(10, "sales")
            .reset_index()
        )

        heatmap_data = top_states.set_index("state")

        fig = px.imshow(
            heatmap_data,
            text_auto=True,
            aspect="auto",
            color_continuous_scale="RdBu",
            height=400
        )

        fig.update_traces(texttemplate="$%{z:,.0f}")

        st.plotly_chart(fig, use_container_width=True)

        # ---------- SALES MAP ---------- #

        st.subheader("🌍 Global Sales Distribution")

        country_sales = (
            df.groupby("country")["sales"]
            .sum()
            .reset_index()
        )

        fig2 = px.choropleth(
            country_sales,
            locations="country",
            locationmode="country names",
            color="sales",
            color_continuous_scale="Blues",
            height=450
        )

        st.plotly_chart(fig2, use_container_width=True)

    # ============================================================
    # PROJECT 2 — UNIVERSITY RANKING ANALYSIS
    # ============================================================

    with st.expander("🎓 World University Ranking Analysis", expanded=False):

        st.write(
        "Data analysis of global university rankings to explore "
        "top institutions and country performance."
        )

        st.link_button(
        "🔗 View on GitHub",
        "https://github.com/Tushar-Patil28/world_ranking_univeristy_analysis"
        )

        df = pd.read_csv("world_university_rankings.csv")

        # ---------- TOP UNIVERSITIES ---------- #
        st.subheader("Share of Ranked Universities by Country")

        # Count universities by country
        country_counts = df['country'].value_counts().reset_index()
        country_counts.columns = ['country', 'university_count']

        # Take top N countries
        top_n = 5
        top_countries = country_counts.head(top_n).copy()

        # Calculate 'Others'
        others_count = country_counts['university_count'][top_n:].sum()

        # Create 'Others' row
        others_row = pd.DataFrame([{
            'country': 'Others',
            'university_count': others_count
        }])

        # Combine
        top_countries = pd.concat([top_countries, others_row], ignore_index=True)

        # Pie / Donut chart
        fig = px.pie(
            top_countries,
            values='university_count',
            names='country',
            title='Share of Ranked Universities by Country',
            hole=0.4,
            color_discrete_sequence=px.colors.sequential.Viridis
        )

        fig.update_traces(textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Correlation Heatmap of University Metrics")

        columns = ['teaching', 'research', 'citations', 'international', 'income', 'total_score']

        df_corr = df[columns].select_dtypes(include='number').corr()

        fig = px.imshow(
            df_corr,
            text_auto=True,
            color_continuous_scale="RdBu_r",
            title="Correlation Heatmap of University Metrics"
        )

        fig.update_layout(height=500)

        st.plotly_chart(fig, use_container_width=True)
    # ============================================================
    # PROJECT 3 — FIFA PLAYER VALUE PREDICTION (SHOWCASE ONLY)
    # ============================================================

    with st.expander("⚽ FIFA 22 Player Value Prediction", expanded=False):

        st.write(
        "Machine learning regression model designed to predict football player "
        "market value based on performance attributes such as overall rating, "
        "potential, and player statistics."
        )

        st.link_button(
        "🔗 View on GitHub",
        "https://github.com/Tushar-Patil28/Fifa22_model-training"
        )

        st.info(
        "This project focuses on model training, feature engineering, and regression "
        "evaluation techniques to estimate player market value."
        )