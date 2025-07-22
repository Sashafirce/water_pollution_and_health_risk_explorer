import pandas as pd

# Test if the data loads correctly
try:
    file_path = "jupyter_notebooks/input_data/cleaned_water_pollution_disease_with_cost.csv"
    df = pd.read_csv(file_path, nrows=10)  # Read only first 10 rows to avoid memory issues
    print("✅ Data loaded successfully!")
    print(f"Shape: {df.shape}")
    print("\nColumns:")
    for i, col in enumerate(df.columns):
        print(f"{i+1}. {col}")
    
    print("\nFirst few rows:")
    print(df.head(3))
    
    # Check if key columns exist
    required_columns = [
        "Region", "Country", "Contaminant Level (ppm)", 
        "Health Burden Index", "GDP per Capita (USD)",
        "Estimated Cost per Outbreak (€)"
    ]
    
    missing_columns = []
    for col in required_columns:
        if col not in df.columns:
            missing_columns.append(col)
    
    if missing_columns:
        print(f"\n❌ Missing columns: {missing_columns}")
    else:
        print("\n✅ All required columns are present!")
        
except Exception as e:
    print(f"❌ Error loading data: {e}")
