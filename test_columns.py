import pandas as pd

# Load the data
try:
    df = pd.read_csv(
        'jupyter_notebooks/input_data/'
        'cleaned_water_pollution_disease_with_cost.csv'
    )
    print("✅ Data loaded successfully!")
    print(f"Dataset shape: {df.shape}")
    print("\n📋 Available columns:")
    for i, col in enumerate(df.columns):
        print(f"{i+1:2d}. {col}")

    # Check for required columns
    required_columns = [
        "Contaminant Level (ppm)",
        "Health Burden Index",
        "GDP per Capita (USD)",
        "Estimated Cost per Outbreak (€)",
        "Region",
        "Country"
    ]

    print("\n🔍 Checking required columns:")
    missing_columns = []
    for col in required_columns:
        if col in df.columns:
            print(f"✅ {col}")
        else:
            print(f"❌ {col}")
            missing_columns.append(col)

    if missing_columns:
        print(f"\n⚠️  Missing columns: {missing_columns}")
    else:
        print("\n🎉 All required columns are present!")

except Exception as e:
    print(f"❌ Error loading data: {e}")
