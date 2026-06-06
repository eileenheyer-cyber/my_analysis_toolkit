# My Analysis Toolkit

A personal reusable toolkit for data analysis projects.

This repository collects two things:

1. **Reusable Python functions** for cleaning, EDA, and statistics.
2. **Reusable prompt templates** for visualization, business insights, and chart feedback.

The goal is to build a practical workflow system that helps me analyze new datasets faster, ask better AI questions, and create more consistent project outputs.

---

## Repository Structure

```text
MY_ANALYSIS_TOOLKIT/
│
├── functions/
│   │
│   ├── cleaning_function/
│   │   ├── __init__.py
│   │   └── cleaning_utils.py
│   │
│   ├── eda_functions/
│   │   ├── eda_function.py
│   │   └── quick_summary.md
│   │
│   └── Statistics_Analysis_Functions/
│       └── stats_utils.py
│
├── prompts_notebooks/
│   │
│   ├── Business_Insight_Prompt/
│   │
│   ├── Visualization_Examples/
│   │
│   └── Visualization_Prompt/
│       ├── 1_horizontal_bar_chart.md
│       ├── 2_distribution_chart.md
│       ├── 3_boxplot_comparison.md
│       ├── 4_scatterplot.md
│       └── 5_dashboard_chart_feedback.md
│
├── .gitignore
└── README.md
```

---

## Purpose

This toolkit is designed to support different types of data analysis projects, for example:

- Job market analysis
- Sales analysis
- Customer analysis
- Marketing analysis
- Business intelligence projects
- Portfolio projects
- Learning projects with Python, SQL, and Power BI

Instead of starting from zero every time, I can reuse existing functions, prompts, and analysis structures.

---

## Main Workflow

```text
New dataset
→ understand the business question
→ use EDA functions
→ use visualization prompts
→ create charts
→ generate insights
→ improve the toolkit
```

The repository grows through real projects. Whenever I solve a useful problem, I save the function or prompt so I can reuse it later.

---

## Python Functions

The `functions/` folder contains reusable Python helper functions.

### Cleaning Functions

Location:

```text
functions/cleaning_function/
```

Purpose:

- Clean column names
- Handle missing values
- Remove duplicates
- Prepare data for analysis

Example use cases:

```text
clean messy column names
standardize text columns
prepare raw data before EDA
```

### EDA Functions

Location:

```text
functions/eda_functions/
```

Purpose:

- Quickly inspect a dataset
- Summarize columns
- Check missing values
- Understand basic data structure

Example use cases:

```text
first look at a new dataset
quick data quality check
generate summary tables
```

### Statistics Analysis Functions

Location:

```text
functions/Statistics_Analysis_Functions/
```

Purpose:

- Support statistical analysis
- Calculate descriptive statistics
- Prepare statistical summaries

Example use cases:

```text
compare groups
summarize numeric variables
prepare data for deeper analysis
```

---

## Prompt Library

The `prompts_notebooks/` folder contains reusable prompts for AI-assisted data analysis.

The goal of the prompt library is not just to get faster answers, but to ask better and more structured questions.

### Visualization Prompts

Location:

```text
prompts_notebooks/Visualization_Prompt/
```

Current prompt files:

```text
1_horizontal_bar_chart.md
2_distribution_chart.md
3_boxplot_comparison.md
4_scatter_plot.md
5_dashboard_chart_feedback.md
```

These prompts help create consistent and professional charts.

They are useful for:

- Ranking charts
- Salary distributions
- Group comparisons
- Scatter_plots
- Dashboard feedback
- Portfolio visualizations

### Business Insight Prompts

Location:

```text
prompts_notebooks/Business_Insight_Prompt/
```

Purpose:

- Turn chart results into insights
- Connect analysis results to business questions
- Write clearer interpretations
- Generate next-step recommendations

Example use cases:

```text
explain what a chart shows
write portfolio-style insights
turn analysis into business recommendations
```

### Visualization Examples

Location:

```text
prompts_notebooks/Visualization_Examples/
```

Purpose:

- Save good chart examples
- Store visual inspiration
- Compare before/after chart improvements
- Build a personal visualization reference library

---

## How to Use the Prompt Files

1. Open the prompt file you need.
2. Copy the reusable prompt.
3. Replace the placeholders with your own dataset information.
4. Paste the prompt into ChatGPT or another AI tool.
5. Save the improved version back into the repository if it works well.

Example:

```text
Open:
prompts_notebooks/Visualization_Prompt/1_horizontal_bar_chart.md

Replace:
{df_name} = df
{category_column} = job_title_short
{top_n} = 10
{chart_title} = Top 10 Job Titles by Number of Job Postings
{x_axis_label} = Job Posting Count
```

---

## Prompt Design Rule

A good prompt should include:

1. **Context** — What project or dataset am I working on?
2. **Input** — Which columns, code, chart, or result do I already have?
3. **Task** — What exactly do I want AI to do?
4. **Requirements** — What style, logic, or constraints should be followed?
5. **Output format** — Should the answer be code, explanation, insight, checklist, or markdown?

---

## Example Prompt Structure

```text
Context:
I am working on a data analysis project about [topic].

Data:
The DataFrame is called [df_name].
Important columns are [columns].

Task:
Create / explain / improve / analyze [specific task].

Requirements:
- Requirement 1
- Requirement 2
- Requirement 3

Output:
Return [Python code / markdown explanation / business insight / checklist].
```

---

## Development Principle

This toolkit should stay practical.

Do not add random files just to make the repository bigger. Only add prompts and functions that are useful in real projects.

A file is worth saving when:

```text
I will probably need this again.
```

---

## Roadmap

Planned improvements:

- Add more chart prompts
- Add SQL prompts
- Add Power BI prompts
- Add EDA checklist prompts
- Add more reusable Python cleaning functions
- Add example notebooks
- Add before/after chart examples
- Improve documentation for each function

---

## Personal Learning Goal

This repository is part of my learning journey toward becoming a stronger data analyst.

It helps me practice:

- Python
- Pandas
- Data visualization
- Statistics
- Business thinking
- Prompt engineering
- Data storytelling

The long-term goal is to build a reusable workflow system that supports both learning projects and portfolio projects.
