import streamlit as st
import plotly.express as px
import pandas as pd

# 🌊 Page Configuration
st.set_page_config(
    page_title="Water Pollution & Disease Outbreaks",
    page_icon="🌊",
    layout="wide"
)

# 📋 App Title
st.title("🌊 Water Pollution and Disease Outbreaks: The Cost of Inaction")

# KPI Values (Replace with your own calculations if needed)
total_cases = 15720
avg_gdp = 8230
avg_contaminant = 54.6

# 🌗 Theme Toggle
theme = st.sidebar.radio("Choose Theme:", ["Light", "Dark"])

if theme == "Dark":
    st.markdown("""
        <style>
        body, .stApp { background-color: #1e1e1e; color: #f5f5f5; }
        .kpi-card { background-color: #333333; color: #ffffff; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        body, .stApp { background-color: #ffffff; color: #262730; }
        .kpi-card { background-color: #f2f2f2; color: #262730; }
        </style>
    """, unsafe_allow_html=True)

# 🧮 KPI Summary Cards
st.markdown("""
<style>
.kpi-container {
    display: flex;
    justify-content: space-around;
    margin: 25px 0 40px 0;
}
.kpi-card {
    padding: 25px;
    border-radius: 15px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    flex: 1;
    margin: 0 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="kpi-container">
    <div class="kpi-card">🧬 Total Disease Cases<br>{total_cases:,}</div>
    <div class="kpi-card">💸 Avg GDP per Capita<br>${avg_gdp:,}</div>
    <div class="kpi-card">💧 Avg Contaminant Level<br>
    {avg_contaminant} ppm</div>
</div>
""", unsafe_allow_html=True)


# 📥 Load Data
@st.cache_data
def load_data():
    file_path = ("jupyter_notebooks/input_data/"
                 "cleaned_water_pollution_disease_with_cost.csv")
    return pd.read_csv(file_path)


df = load_data()

# 🎛️ Sidebar Filters
st.sidebar.header("🌍 Filter Data")
regions = st.sidebar.multiselect(
    "Select Region(s)",
    df["Region"].unique(),
    default=df["Region"].unique()
)
df_filtered = df[df["Region"].isin(regions)]

# 🧭 App Tabs
tab1, tab2, tab3 = st.tabs([
    "📊 Hypotheses",
    "🤖 ML Estimations",
    "📌 Tableau Dashboards"
])

# 📊 Hypotheses Tab
with tab1:
    st.subheader("📘 H1 – Pollution & Disease Burden")
    fig_h1 = px.scatter(
        df_filtered,
        x="Contaminant Level (ppm)",
        y="Health Burden Index",
        color="Region",
        hover_data=["Country"],
        trendline="ols",
        template="plotly_white"
    )
    st.plotly_chart(fig_h1, use_container_width=True)

    st.subheader("🩺 H2a – GDP vs Disease Burden")
    fig_h2a = px.scatter(
        df_filtered,
        x="GDP per Capita (USD)",
        y="Health Burden Index",
        color="Country",
        hover_data=["Region"],
        trendline="ols",
        template="plotly_white"
    )
    st.plotly_chart(fig_h2a, use_container_width=True)

    st.subheader("⚖️ H2b – GDP + Pollution vs Disease Burden")
    fig_h2b = px.scatter_3d(
        df_filtered,
        x="GDP per Capita (USD)",
        y="Contaminant Level (ppm)",
        z="Health Burden Index",
        color="Region",
        hover_name="Country"
    )
    st.plotly_chart(fig_h2b, use_container_width=True)

    st.subheader("📉 H3 – Wealth vs Health Burden")
    fig_h3 = px.scatter(
        df_filtered,
        x="GDP per Capita (USD)",
        y="Health Burden Index",
        color="Region",
        hover_data=["Country"],
        trendline="ols",
        template="plotly_white"
    )
    st.plotly_chart(fig_h3, use_container_width=True)

# 🤖 ML Estimations Tab
with tab2:
    st.subheader("💰 Estimated Cost per Outbreak")
    fig_ml_cost = px.scatter(
        df_filtered,
        x="Contaminant Level (ppm)",
        y="Estimated Cost per Outbreak (€)",
        color="Region",
        hover_data=["Country"],
        trendline="ols",
        template="plotly_white"
    )
    st.plotly_chart(fig_ml_cost, use_container_width=True)

    st.subheader("📊 Health Burden Analysis")
    fig_ml_health = px.scatter(
        df_filtered,
        x="Contaminant Level (ppm)",
        y="Health Burden Index",
        color="Region",
        hover_data=["Country"],
        trendline="ols",
        template="plotly_white"
    )
    st.plotly_chart(fig_ml_health, use_container_width=True)

# 📌 Tableau Dashboards Tab
with tab3:
    st.subheader("📌 Tableau Dashboard 1")
    st.components.v1.iframe(
        "https://public.tableau.com/views/"
        "Waterpollutionanddiseaseoutbreakspart1/Dashboard1",
        height=800,
        scrolling=True
    )

    st.subheader("📌 Tableau Dashboard 2")
    st.components.v1.iframe(
        "https://public.tableau.com/views/"
        "Waterpollutionanddiseaseoutbreakspart2/Dashboard12",
        height=800,
        scrolling=True
    )
