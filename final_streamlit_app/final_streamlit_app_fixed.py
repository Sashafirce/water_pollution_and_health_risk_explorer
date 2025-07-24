
import streamlit as st
import pandas as pd

# Load the data
df = pd.read_csv("final_dataset_with_predictions.csv")

# Set up the app layout
st.set_page_config(layout="wide")
st.title("🌍 Water Pollution & Public Health Risk Explorer")

# Summary KPIs
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Average Contamination (ppm)", round(df["Average Contamination (ppm)"].mean(), 2))
with col2:
    st.metric("Avg Disease Burden Index", round(df["Total Health Burden Index"].mean(), 2))
with col3:
    st.metric("Avg Predicted Infant Mortality", round(df["Predicted Infant Mortality Rate"].mean(), 2))

st.markdown("## 🧪 Hypothesis Explorer")

# Tabs for each hypothesis and ML
tab1, tab2, tab3, tab4 = st.tabs([
    "H1: Contamination vs Disease Burden",
    "H2: Healthcare Access vs Disease Burden",
    "H3: Water & Sanitation vs Infant Mortality",
    "ML: Predicted Infant Mortality"
])

with tab1:
    st.subheader("H1: Is higher contamination linked to worse disease burden?")
    st.markdown("Explore how pollutant levels correlate with health burden across countries.")
    st.image("https://public.tableau.com/placeholder_link_h1", caption="Tableau Dashboard H1", use_column_width=True)

with tab2:
    st.subheader("H2: Does healthcare access protect against health burden?")
    st.markdown("Compare healthcare index with disease burden to reveal protective patterns.")
    st.image("https://public.tableau.com/placeholder_link_h2", caption="Tableau Dashboard H2", use_column_width=True)

with tab3:
    st.subheader("H3: Are poor water & sanitation systems linked to higher infant deaths?")
    st.markdown("Track the relationship between WASH indicators and infant mortality.")
    st.image("https://public.tableau.com/placeholder_link_h3", caption="Tableau Dashboard H3", use_column_width=True)

with tab4:
    st.subheader("ML Model: Predicting Infant Mortality from Pollution & Access")
    st.markdown("Our regression model estimates infant mortality based on contamination, sanitation, and healthcare variables.")
    st.image("https://public.tableau.com/placeholder_link_ml", caption="ML Prediction Dashboard", use_column_width=True)

# Footer
st.markdown("---")
st.caption("Created with ❤️ by Marie. Powered by Streamlit.")
