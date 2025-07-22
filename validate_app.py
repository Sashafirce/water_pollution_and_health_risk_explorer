#!/usr/bin/env python3
"""
Test script to validate the Streamlit app
"""


def main():
    print("🔍 Checking app_combined_final.py...")

    # Check if all necessary imports are available
    try:
        import streamlit  # noqa: F401
        print("✅ streamlit import: OK")
    except ImportError as e:
        print(f"❌ streamlit import: {e}")
        return False

    try:
        import plotly.express  # noqa: F401
        print("✅ plotly.express import: OK")
    except ImportError as e:
        print(f"❌ plotly.express import: {e}")
        return False

    try:
        import pandas as pd
        print("✅ pandas import: OK")
    except ImportError as e:
        print(f"❌ pandas import: {e}")
        return False

    # Check if data file exists
    import os
    data_path = ("jupyter_notebooks/input_data/"
                 "cleaned_water_pollution_disease_with_cost.csv")
    if os.path.exists(data_path):
        print("✅ Data file exists: OK")
    else:
        print(f"❌ Data file missing: {data_path}")
        return False

    # Load and validate data
    try:
        df = pd.read_csv(data_path)
        print(f"✅ Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")

        # Check required columns
        required_cols = [
            "Contaminant Level (ppm)",
            "Health Burden Index",
            "GDP per Capita (USD)",
            "Estimated Cost per Outbreak (€)",
            "Region",
            "Country"
        ]

        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            print(f"❌ Missing columns: {missing_cols}")
            return False
        else:
            print("✅ All required columns present: OK")

    except Exception as e:
        print(f"❌ Data loading error: {e}")
        return False

    print("\n🎉 All checks passed! Your app should work correctly.")
    print("\n🚀 To run the app, use:")
    print("   streamlit run app_combined_final.py")

    return True


if __name__ == "__main__":
    main()
