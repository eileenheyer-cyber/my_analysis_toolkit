import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def quick_summary(df):
    """One-line EDA overview"""
    print(f"Shape: {df.shape}")
    print(f"\nData Types:\n{df.dtypes}")
    print(f"\nMissing Values:\n{df.isnull().sum()}")
    print(f"\nBasic Stats:\n{df.describe()}")

def check_distributions(df, numeric_cols=None):
    """Plot distributions of numeric columns"""
    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=['number']).columns
    
    fig, axes = plt.subplots(len(numeric_cols), 1, figsize=(10, 3*len(numeric_cols)))
    for ax, col in zip(axes, numeric_cols):
        df[col].hist(ax=ax, bins=30, edgecolor='black')
        ax.set_title(f"Distribution of {col}")
    plt.tight_layout()
    plt.show()

def identify_outliers(df, column, method='iqr'):
    """Flag potential outliers"""
    if method == 'iqr':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        outliers = df[(df[column] < lower) | (df[column] > upper)]
        return outliers
    return None

def correlation_matrix(df, plot=True):
    """Calculate and optionally plot correlations"""
    corr = df.select_dtypes(include=['number']).corr()
    
    if plot:
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='RdBu_r', center=0)
        plt.title('Correlation Matrix')
        plt.show()
    
    return corr