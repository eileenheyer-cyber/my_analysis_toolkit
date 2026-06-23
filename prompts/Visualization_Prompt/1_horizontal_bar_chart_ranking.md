# Horizontal Bar Chart Ranking Prompt

## Purpose

Use this prompt when I want to compare the top categories by count, frequency, sales, revenue, salary, or any other numeric metric.

This prompt is useful for charts like:

- Top 10 job titles by number of job postings
- Top 10 skills by demand
- Top 10 products by sales
- Top 10 countries by revenue
- Top 10 customer segments by order count

## Reusable Prompt

```text
I have a pandas DataFrame called {df_name}.

Create a clean and professional horizontal bar chart to show the top {top_n} categories by {metric_name}.

Data logic:
- Category column: {category_column}
- Metric column: {metric_column}
- Aggregation method: {aggregation_method}
- Sort the result from highest to lowest
- Show only the top {top_n} categories
- Display the highest value at the top of the chart

Chart style:
- Use a horizontal bar chart
- Use a dark-to-light blue gradient
- The highest value should have the darkest color
- Add value labels at the end of each bar
- Format large numbers with commas
- Use a clean white background
- Add light dashed vertical gridlines
- Remove unnecessary chart borders/spines
- Keep the chart minimal, readable, and portfolio-ready
- Add enough right padding so labels are not cut off

Chart labels:
- Title: {chart_title}
- X-axis label: {x_axis_label}
- Y-axis label: empty or minimal

Return reusable Python code using pandas, matplotlib, and seaborn.

```

## Example Chart

Example chart:

![Top 10 Job Titles](assets/top_10_job_titles_by_count.png)
