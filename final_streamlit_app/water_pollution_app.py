
import streamlit as st
import pandas as pd
import random
import os

# Page configuration
st.set_page_config(
    page_title="Water Pollution & Health Risk Explorer",
    page_icon="🌍",
    layout="wide"
)

# Load data with error handling


@st.cache_data
def load_data():
    try:
        # Try current directory first
        if os.path.exists("final_dataset_with_predictions.csv"):
            df = pd.read_csv("final_dataset_with_predictions.csv")
        else:
            # Try parent directory
            df = pd.read_csv(
                "../jupyter_notebooks/input_data/"
                "final_dataset_with_predictions.csv"
            )
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None


df = load_data()

if df is None:
    st.stop()

# Create derived columns for the app
df['Average Contamination (ppm)'] = df['contaminant_level_ppm']
df['Total Health Burden Index'] = df['total_disease_burden']
df['Infant Mortality Rate'] = df['infant_mortality_rate_per_1000_live_births']
df['Healthcare Access Index'] = df['healthcare_access_index_0100']
df['Water Sanitation Index'] = df['sanitation_coverage_percent_of_population']
df['Predicted Infant Mortality Rate'] = df['predicted_infant_mortality']

# Create Region column based on country (simplified mapping)
region_mapping = {
    'Mexico': 'North America',
    'Brazil': 'South America',
    'Indonesia': 'Asia',
    'Nigeria': 'Africa',
    'Ethiopia': 'Africa',
    'China': 'Asia',
    'USA': 'North America',
    'India': 'Asia',
    'Bangladesh': 'Asia',
    'Pakistan': 'Asia'
}
df['Region'] = df['country'].map(region_mapping).fillna('Other')

# Sidebar filters
st.sidebar.title("🔧 Filters")
selected_year = st.sidebar.selectbox(
    "Select Year", sorted(df["year"].unique()), index=0
)
selected_region = st.sidebar.selectbox(
    "Select Region", sorted(df["Region"].dropna().unique()), index=0
)
theme_option = st.sidebar.radio("Theme", ["Light", "Dark"])

# Filtered data
filtered_df = df[
    (df["year"] == selected_year) & (df["Region"] == selected_region)
]

# Apply theme
if theme_option == "Dark":
    st.markdown(
        '''
        <style>
        body { background-color: #111; color: #eee; }
        .stApp { background-color: #111; color: #eee; }
        </style>
        ''',
        unsafe_allow_html=True
    )

# Title and subtitle
st.title("🌍 Water Pollution & Health Risk Explorer")
st.caption(
    "By Sheila | Data Analysis • Machine Learning • Visual Storytelling"
)

# KPI Styling
kpi1, kpi2, kpi3 = st.columns(3)

# Add error handling for empty filtered data
if not filtered_df.empty:
    avg_contamination = filtered_df['Average Contamination (ppm)'].mean()
    avg_disease_burden = filtered_df['Total Health Burden Index'].mean()
    avg_predicted_mortality = filtered_df[
        'Predicted Infant Mortality Rate'
    ].mean()
    kpi1.metric("📊 Avg Contamination", f"{avg_contamination:.2f} ppm")
    kpi2.metric("💉 Avg Disease Burden", f"{avg_disease_burden:.2f}")
    kpi3.metric(
        "👶 Predicted Infant Mortality", f"{avg_predicted_mortality:.2f}"
    )
else:
    kpi1.metric("📊 Avg Contamination", "No data")
    kpi2.metric("💉 Avg Disease Burden", "No data")
    kpi3.metric("👶 Predicted Infant Mortality", "No data")

# Country Explorer
st.markdown("### 🗺️ Country Explorer")
if not filtered_df.empty:
    selected_country = st.selectbox(
        "Select a country",
        sorted(filtered_df["country"].unique())
    )
    country_data = filtered_df[
        filtered_df["country"] == selected_country
    ].mean(numeric_only=True)
    st.write(f"**Stats for {selected_country}**")
    if not country_data.empty:
        display_columns = [
            "Average Contamination (ppm)", "Total Health Burden Index",
            "Infant Mortality Rate", "Healthcare Access Index",
            "Water Sanitation Index", "Predicted Infant Mortality Rate"
        ]
        st.write(country_data[display_columns])
    else:
        st.warning(f"No data available for {selected_country}")
else:
    st.warning("No data available for the selected filters")

# Show data preview
if st.checkbox("🔍 Show data preview"):
    st.dataframe(filtered_df.head())

# Tabs for hypotheses and ML
tab1, tab2, tab3, tab4 = st.tabs([
    "H1: Contamination vs Disease Burden",
    "H2: Healthcare Access vs Disease Burden",
    "H3: Water & Sanitation vs Infant Mortality",
    "ML: Predicted Infant Mortality"
])

with tab1:
    st.subheader("H1: Contamination vs Disease Burden")
    # Use embedded Tableau format for better loading
    tableau_url_h1 = (
        "https://public.tableau.com/views/"
        "Waterpollutionhealthriskh1/Dashboard1"
    )
    st.markdown(f"[View Interactive Dashboard]({tableau_url_h1})")
    try:
        st.image(
            f"{tableau_url_h1}.png",
            caption="Tableau Dashboard H1",
            use_column_width=True
        )
    except Exception:
        st.info("📊 Interactive dashboard available at the link above")
    st.markdown(
        "**Insight:** High contamination correlates with "
        "increased disease burden."
    )
    st.markdown("**Explore:** Filter by year or region.")

with tab2:
    st.subheader("H2: Healthcare Access vs Disease Burden")
    tableau_url_h2 = (
        "https://public.tableau.com/views/"
        "WaterpollutionHealthriskh2/Dashboard2"
    )
    st.markdown(f"[View Interactive Dashboard]({tableau_url_h2})")
    try:
        st.image(
            f"{tableau_url_h2}.png",
            caption="Tableau Dashboard H2",
            use_column_width=True
        )
    except Exception:
        st.info("📊 Interactive dashboard available at the link above")
    st.markdown(
        "**Insight:** Better healthcare access tends to "
        "reduce disease burden."
    )
    st.markdown("**Explore:** Investigate regional disparities.")

with tab3:
    st.subheader("H3: Water & Sanitation vs Infant Mortality")
    tableau_url_h3 = (
        "https://public.tableau.com/views/"
        "WaterpollutionHealthriskH3real/Dashboard3"
    )
    st.markdown(f"[View Interactive Dashboard]({tableau_url_h3})")
    try:
        st.image(
            f"{tableau_url_h3}.png",
            caption="Tableau Dashboard H3",
            use_column_width=True
        )
    except Exception:
        st.info("📊 Interactive dashboard available at the link above")
    st.markdown(
        "**Insight:** Improved sanitation links to lower infant mortality."
    )
    st.markdown("**Explore:** Track changes by year.")

with tab4:
    st.subheader("ML: Predicted Infant Mortality")
    tableau_url_ml = (
        "https://public.tableau.com/views/"
        "WaterpollutionHealthriskML/Dashboard4"
    )
    st.markdown(f"[View Interactive Dashboard]({tableau_url_ml})")
    try:
        st.image(
            f"{tableau_url_ml}.png",
            caption="ML Prediction Dashboard",
            use_column_width=True
        )
    except Exception:
        st.info("📊 Interactive dashboard available at the link above")
    st.markdown("**Model Insight:** Predictions align with high-risk zones.")
    st.markdown("**Explore:** Compare actual vs predicted rates.")

# Facts section
facts = [
    "Unsafe water kills more people annually than all forms of violence, "
    "including war.",
    "Over 80% of the world's wastewater is released untreated.",
    "Children under five are especially vulnerable to waterborne illness."
]
st.markdown("### 🧠 Did You Know?")
st.info(random.choice(facts))

# Engagement
st.markdown(
    "### 💬 What surprised you most? Use filters to dig deeper "
    "and share insights!"
)

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
