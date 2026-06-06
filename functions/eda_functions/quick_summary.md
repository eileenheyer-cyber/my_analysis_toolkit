# Quick Data Summary

## Purpose
Get an instant overview of your dataset — shape, column types, missing values, and basic statistics. Use this first when exploring new data.

## Prompt
```
Analyze the pandas dataframe {dataframe} and provide:
1. Shape and column names
2. Data types for each column
3. Count of missing values per column (with percentage)
4. Basic statistics (mean, median, min, max, std) for numeric columns
5. Sample unique values for categorical columns
6. Highlight any potential issues (high missingness, unusual data types, etc.)

Format as a clear summary report.
```

## Variables
- `{dataframe}`: Your pandas DataFrame variable name (e.g., `df`, `data`, `sales_data`)

## Example Output
```
DATASET SUMMARY: sales_df
─────────────────────────
Shape: (1000 rows, 8 columns)

COLUMNS & TYPES:
- order_id (int64)
- customer_name (object)
- purchase_date (datetime64)
- amount (float64)
- region (object)
- product_category (object)
- quantity (int64)
- is_returned (bool)

MISSING VALUES:
- order_id: 0 (0%)
- customer_name: 0 (0%)
- purchase_date: 0 (0%)
- amount: 2 (0.2%)
- region: 5 (0.5%)
- product_category: 0 (0%)
- quantity: 0 (0%)
- is_returned: 0 (0%)

NUMERIC STATS:
amount: mean=245.67, median=199.50, min=10.00, max=2500.00, std=312.45
quantity: mean=2.3, median=2.0, min=1, max=15, std=1.8

CATEGORICAL SAMPLES:
- region: ['North America', 'Europe', 'Asia', 'South America']
- product_category: ['Electronics', 'Clothing', 'Home & Garden']

ISSUES DETECTED:
⚠️  Minor: 2 missing values in 'amount' column (0.2%)
⚠️  Minor: 5 missing values in 'region' column (0.5%)
✓ No critical issues
```

## Notes
- Run this immediately after loading new data
- Pay attention to missing value patterns — they're often meaningful
- Use the data types check to catch unexpected formats
- High std relative to mean suggests outliers worth investigating

## Next Steps
Based on findings, follow up with:
- `eda/check_distributions.md` — if you see skewed numeric data
- `cleaning/handle_missing_values.md` — if missingness > 1%
- `eda/identify_outliers.md` — if std is very high
