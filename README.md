# Data Analysis Prompts Toolkit

A personal repository of refined prompts for repetitive data analysis tasks using Python, pandas, and matplotlib/seaborn/plotly.

## 📁 Structure

```
data-analysis-prompts/
├── visualization/          # Chart creation prompts
├── cleaning/               # Data cleaning & preprocessing
├── eda/                    # Exploratory data analysis
├── analysis/               # Statistical analysis & modeling
└── README.md
```

## 🚀 Quick Start

### Using a Prompt
1. Navigate to the relevant folder (e.g., `visualization/`)
2. Open the `.md` file you need
3. Replace variables in curly braces: `{dataframe}`, `{column_name}`, etc.
4. Copy the prompt and paste into Claude

### Example
```markdown
# File: visualization/bar_chart.md

Prompt:
Create a matplotlib bar chart showing {y_column} by {x_column} from {dataframe}
```

Replace with your actual values:
```
Create a matplotlib bar chart showing sales by product from df
```

## 📋 Prompts by Category

### Visualization
- `bar_chart.md` — Quick comparative bar charts
- `scatter_plot.md` — Correlation & relationship exploration
- `distribution_plot.md` — Single & multiple distributions
- `heatmap.md` — Correlation matrices & cross-tabulations

### Cleaning
- `handle_missing_values.md` — Strategies for NaN/null values
- `normalize_columns.md` — Scaling & normalization
- `fix_column_names.md` — Standardize naming conventions

### EDA
- `quick_summary.md` — Shape, dtypes, nulls, basic stats
- `check_distributions.md` — Distribution analysis
- `identify_outliers.md` — Detect & handle anomalies

### Analysis
- `correlation_analysis.md` — Find relationships between variables
- `group_and_aggregate.md` — Groupby operations & summaries

## 💡 Tips

- **Variables are in curly braces**: `{dataframe}`, `{column_name}`, `{x_column}`, etc.
- **Check "Example Output"** in each file to see expected results
- **Notes section** tells you when to use that prompt
- **Update prompts** when you find something works better

## 🔄 Workflow

Typical data analysis session:
1. Start with `eda/quick_summary.md` to understand your data
2. Use `cleaning/` prompts as needed
3. Explore with `visualization/` and `eda/` prompts
4. Dive deeper with `analysis/` prompts
5. Polish final visualizations

## 📝 Adding New Prompts

When a prompt works well, save it:

1. Create a new `.md` file in the appropriate folder
2. Use the template below:

```markdown
# [Chart Type / Task Name]

## Purpose
[One sentence: what this does and when to use it]

## Prompt
[Your actual prompt with {variables} in curly braces]

## Variables
- `{variable_name}`: description of what goes here
- `{another_var}`: format/type expected

## Example Output
[Paste a working result you liked]

## Notes
- Works best when...
- Common pitfalls...
- Alternatives...
```

3. Commit: `git add [filename].md && git commit -m "Add [description]"`

## 🔧 Optional: Using a Script

Load prompts programmatically with:

```python
import re

def load_prompt(filename, **variables):
    with open(f"prompts/{filename}.md") as f:
        template = f.read()
    # Find the "Prompt" section
    prompt = template.split("## Prompt\n")[1].split("\n## ")[0]
    # Replace variables
    return re.sub(r'\{(\w+)\}', 
                  lambda m: str(variables.get(m.group(1), '')), 
                  prompt)

# Usage
prompt = load_prompt("visualization/bar_chart", 
                     x_column="product", 
                     y_column="sales")
print(prompt)
```

## 📊 Favorites

Your go-to prompts (add these as you find patterns):
- [ ] Quick summary (EDA)
- [ ] Bar chart (Visualization)
- [ ] Handle missing values (Cleaning)

---

Last updated: 2026
Personal toolkit for data analysis with Claude
