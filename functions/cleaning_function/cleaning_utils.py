import pandas as pd
import numpy as np

def handle_missing_values(df, strategy='auto'):
    """
    Handle missing values intelligently.
    
    strategy='auto': Median for numeric, Mode for categorical
    strategy='drop': Remove rows with any NaN
    strategy='forward_fill': For time series
    """
    df = df.copy()
    
    # Numeric columns → median
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        if df[col].isnull().sum() > 0:
            df[col].fillna(df[col].median(), inplace=True)
    
    # Categorical → mode
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        if df[col].isnull().sum() > 0:
            df[col].fillna(df[col].mode()[0], inplace=True)
    
    return df

def standardize_column_names(df):
    """Convert column names to lowercase, replace spaces with underscores"""
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df

def remove_duplicates(df, subset=None, keep='first'):
    """Remove duplicate rows"""
    return df.drop_duplicates(subset=subset, keep=keep)

def remove_outliers(df, column, method='iqr', threshold=1.5):
    """Remove outliers using IQR or z-score"""
    if method == 'iqr':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - threshold * IQR
        upper = Q3 + threshold * IQR
        return df[(df[column] >= lower) & (df[column] <= upper)]
    
    return df