# 1. Interpret Statistical Findings

## Purpose
Turn your analysis (correlation, regression, test results) 
into plain English that business people understand

## Prompt
Analyze these findings and explain:
- What does the result mean in plain English?
- How strong/significant is this?
- What are the limitations?
- What's NOT explained by this analysis?

{finding}: [e.g., "Sales increased 23% after we changed the website"]
{context}: [relevant business context]


# 2.Recommend Data-Driven Actions

## Purpose
Go from "interesting finding" to "here's what we should do"

## Prompt
Based on this insight: {insight}

Suggest 3-5 actionable next steps:
- What experiment/test could we run?
- What decision should we make?
- What's the expected impact?
- What are the risks?
- What data would we need to decide?

# 3.Executive Summary for Non-Technical Audience

## Purpose
Distill your analysis into 1-page summary for leadership

## Prompt
Write a 1-page executive summary:

Finding: {finding}
Data analyzed: {data_description}
Time period: {period}

Include:
- 1-sentence headline (no jargon)
- Why this matters for the business
- Key numbers (with context)
- Recommended action
- Timeline/next steps

# 4. When Something Weird Happens in Data

## Purpose
You found an outlier or unexpected pattern. 
Figure out if it's real or a data quality issue.

## Prompt
I found this anomaly: {anomaly_description}

Is this:
- Real business signal worth investigating?
- Data quality issue (bad data)?
- Seasonal/expected variation?
- Statistical noise?

Help me investigate by suggesting:
- What questions to ask
- What data to check
- How to validate if it's real


# 5.Present Same Finding to Different People

## Purpose
Sales VP cares about revenue. 
Data scientist cares about methodology.
Same insight, different framing.

## Prompt
Finding: {finding}

How would you explain this to:
1. Executive (wants impact + decision)
2. Operational team (wants practical steps)
3. Data team (wants methodology + confidence)

For each, provide:
- Key metric they care about
- Why it matters to them
- What action they should take