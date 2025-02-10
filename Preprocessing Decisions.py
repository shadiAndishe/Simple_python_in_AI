
#You are given a dataset that may have missing values.
#The preprocessing decisions might depend on the percentage of missing values in each feature.
import pandas as pd
import numpy as np
def preprocess_data(df):
    for column in df.columns:
        missing_percentage = df[column].isnull().mean()

        if missing_percentage > 0.5:
            df[column] = df[column].fillna(df[column].mode()[0])  # Replace missing with mode if > 50% missing
        elif missing_percentage > 0.2:
            df[column] = df[column].fillna(df[column].mean())  # Replace missing with mean if > 20% missing
        else:
            df[column] = df[column].dropna()  # Drop rows if missing value is low

    return df


# Example
data = pd.DataFrame({
    'age': [25, np.nan, 30, 35, np.nan],
    'salary': [50000, 55000, np.nan, 60000, 65000]
})

preprocessed_data = preprocess_data(data)
print(preprocessed_data)
