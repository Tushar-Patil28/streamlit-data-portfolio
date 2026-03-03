import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def show_projects():

    st.title("📁 Projects")

    # Project 1
    st.subheader("Super Store Sales Analysis")
    st.write("Exploratory Data Analysis on sales performance and business insights.")
    st.markdown("[🔗 View on GitHub](https://github.com/Tushar-Patil28/Super_Store_Sales-Only-Visualization-)")
    st.markdown("---")

    # Project 2
    st.subheader("World University Ranking Analysis")
    st.write("Statistical analysis and visualization of global university rankings.")
    st.markdown("[🔗 View on GitHub](https://github.com/Tushar-Patil28/world_ranking_univeristy_analysis)")
    st.markdown("---")

    # Project 3
    st.subheader("FIFA 22 Player Value Prediction")
    st.write("Machine Learning model to predict player market value.")
    st.markdown("[🔗 View on GitHub](https://github.com/Tushar-Patil28/Fifa22_model-training)")

    st.markdown('---') 
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    st.set_page_config(page_title="Projects | Tushar Patil", layout="wide")

    # ------------------ SUPERSTORE ------------------ #

    st.subheader("Super Store Sales Analysis")

    df = pd.read_csv("sales.csv")
 

    # --------Sales and profit per state--------#

    # clean column names
    df.columns = df.columns.str.strip().str.lower()

    # check columns exist
    if "state" not in df.columns:
        st.error("Column 'state' not found in dataset")
    else:

        # group data
        top_states = (
            df.groupby("state")[["sales", "profit"]]
            .sum()
            .nlargest(10, "sales")
            .reset_index()
        )

        # set index for heatmap
        heatmap_data = top_states.set_index("state")

        st.markdown("### Top 10 States — Sales vs Profit")

        # create heatmap
        fig = px.imshow(
            heatmap_data,
            text_auto=True,
            aspect="auto",
            color_continuous_scale="RdBu",
            height=350
        
        )

        # styling
        fig.update_layout(
            margin=dict(l=0, r=0, t=40, b=0),
            font=dict(size=12),
            coloraxis_colorbar=dict(title="$ Amount")
        )

        # currency formatting
        fig.update_traces(
            texttemplate="$%{z:,.0f}",
            hovertemplate="$%{z:,.0f}<extra></extra>"
        )

        # display
        st.plotly_chart(fig, use_container_width=True)




        # ---------- INTERACTIVE MAP ---------- #
    
    st.markdown("### Sales Map")

        


    # clean column names
    df.columns = df.columns.str.strip().str.lower()

    # group by country
    country_sales = (
        df.groupby("country")["sales"]
        .sum()
        .reset_index()
        .sort_values("sales", ascending=False)
    )

    # build map
    fig = px.choropleth(
        country_sales,
        locations="country",
        locationmode="country names",
        color="sales",
        hover_name="country",
        color_continuous_scale="Blues",
        height=400
    )

    # layout styling
    fig.update_layout(
        title="Total Sales by Country",
        title_x=0.3,
        font=dict(size=12),
        margin=dict(l=0, r=0, t=40, b=0),
        coloraxis_colorbar=dict(title="$ Sales")   # ← legend $
    )

    # hover + value formatting
    fig.update_traces(
        hovertemplate="<b>%{location}</b><br>Sales: $%{z:,.0f}<extra></extra>"
    )

    # display
    st.plotly_chart(fig, use_container_width=True)



    

