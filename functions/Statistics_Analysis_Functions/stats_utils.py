from scipy import stats
import pandas as pd

def ttest(df, group_col, value_col, equal_var=False):
    """Compare means between two groups"""
    groups = df[group_col].unique()
    group1 = df[df[group_col] == groups[0]][value_col]
    group2 = df[df[group_col] == groups[1]][value_col]
    
    t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=equal_var)
    
    return {
        'test': 't-test',
        'group1_mean': group1.mean(),
        'group2_mean': group2.mean(),
        't_statistic': t_stat,
        'p_value': p_value,
        'significant': p_value < 0.05
    }

def chi_square(df, col1, col2):
    """Test independence between two categorical variables"""
    contingency = pd.crosstab(df[col1], df[col2])
    chi2, p_value, dof, expected = stats.chi2_contingency(contingency)
    
    return {
        'test': 'chi-square',
        'chi2_statistic': chi2,
        'p_value': p_value,
        'degrees_of_freedom': dof,
        'significant': p_value < 0.05
    }

def correlation_test(df, col1, col2, method='pearson'):
    """Test correlation significance"""
    if method == 'pearson':
        corr, p_value = stats.pearsonr(df[col1], df[col2])
    else:
        corr, p_value = stats.spearmanr(df[col1], df[col2])
    
    return {
        'method': method,
        'correlation': corr,
        'p_value': p_value,
        'significant': p_value < 0.05
    }