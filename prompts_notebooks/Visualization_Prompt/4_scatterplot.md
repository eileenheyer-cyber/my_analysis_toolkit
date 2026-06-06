# Annotated Bubble Scatter Plot with Quadrant Analysis

## Use this prompt when
I want to compare two numeric metrics and show which items are high/low on both dimensions.

Examples:
- Skill demand vs. salary
- Product sales volume vs. profit margin
- Marketing spend vs. conversion rate
- Customer count vs. average revenue
- Country job postings vs. median salary

## Prompt Template

Create a clean, professional Seaborn scatter plot with quadrant analysis.

Dataset:
- DataFrame name: `{dataframe_name}`
- Label column or index: `{label_col}`
- X-axis column: `{x_col}`
- Y-axis column: `{y_col}`

Chart goal:
Show the relationship between `{x_col}` and `{y_col}` for `{analysis_subject}`.

Chart requirements:
- Use Seaborn and Matplotlib
- Create a scatter plot
- X-axis: `{x_col}`
- Y-axis: `{y_col}`
- Point size should be based on `{size_col}`
- Point color should be based on `{color_col}`
- Use a blue color palette
- Higher values should appear darker
- Add labels with small arrows pointing to each dot
- Add a vertical median line for `{x_col}`
- Add a horizontal median line for `{y_col}`
- Add quadrant labels:
  - High `{x_col}` / High `{y_col}`
  - Low `{x_col}` / High `{y_col}`
- Format x-axis as `{x_format}`
- Format y-axis as `{y_format}`
- Use light dashed gridlines
- Remove unnecessary borders with sns.despine()
- Use a clean whitegrid style
- Make the title bold and professional
- Make sure labels do not overlap too much

Title:
`{chart_title}`

Return full Python code only.

Example Chart 
![Salary vs Demand Scatter Plot](images/salary_vs_demand_scatter.png)
