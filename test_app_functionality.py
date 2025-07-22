import plotly.express as px
import pandas as pd


def test_app():
    try:
        # Test data loading
        file_path = ("jupyter_notebooks/input_data/"
                     "cleaned_water_pollution_disease_with_cost.csv")
        df = pd.read_csv(file_path)
        print("✅ Data loading: SUCCESS")

        # Test filtering
        regions = df["Region"].unique()
        df_filtered = df[df["Region"].isin(regions)]
        print("✅ Data filtering: SUCCESS")

        # Test chart creation
        try:
            px.scatter(
                df_filtered,
                x="Contaminant Level (ppm)",
                y="Health Burden Index",
                color="Region",
                hover_data=["Country"],
                trendline="ols",
                template="plotly_white"
            )
            print("✅ H1 chart: SUCCESS")
        except Exception as e:
            print(f"❌ H1 chart: {e}")

        try:
            px.scatter(
                df_filtered,
                x="GDP per Capita (USD)",
                y="Health Burden Index",
                color="Country",
                hover_data=["Region"],
                trendline="ols",
                template="plotly_white"
            )
            print("✅ H2a chart: SUCCESS")
        except Exception as e:
            print(f"❌ H2a chart: {e}")

        try:
            px.scatter_3d(
                df_filtered,
                x="GDP per Capita (USD)",
                y="Contaminant Level (ppm)",
                z="Health Burden Index",
                color="Region",
                hover_name="Country"
            )
            print("✅ H2b chart: SUCCESS")
        except Exception as e:
            print(f"❌ H2b chart: {e}")

        try:
            px.scatter(
                df_filtered,
                x="Contaminant Level (ppm)",
                y="Estimated Cost per Outbreak (€)",
                color="Region",
                hover_data=["Country"],
                trendline="ols",
                template="plotly_white"
            )
            print("✅ ML cost chart: SUCCESS")
        except Exception as e:
            print(f"❌ ML cost chart: {e}")

        print("\n🎉 All tests completed!")

    except Exception as e:
        print(f"❌ Overall error: {e}")


if __name__ == "__main__":
    test_app()
