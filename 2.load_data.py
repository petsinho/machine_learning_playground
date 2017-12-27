import os
import pandas as pd

HOUSING_PATH = "datasets/housing"

# Load data using pandas
def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

housing = load_housing_data()
housing.head(10)