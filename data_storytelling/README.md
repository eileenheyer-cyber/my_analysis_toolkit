# Data Storytelling

> Principles and guidelines for creating charts that are consistent, professional, and clear — inspired by *Storytelling with Data* by Cole Nussbaumer Knaflic.

---

## Purpose

This section is the opinionated foundation of the toolkit. Its job is to answer the question *"how should this chart look and work?"* before any code is written.

The goal is not aesthetic novelty. It is clarity: every visual choice should either help the reader understand the data faster or get out of the way. Charts built from these principles should be immediately recognizable as deliberate, not as defaults.

---

## What's in this section

| File | What it covers |
|---|---|
| `big_idea.md` | Defining the single message a chart must communicate before building it |
| `chart_selection.md` | Choosing the right chart type for the relationship you're showing |
| `color_usage.md` | Palette rules, how to use color to direct attention, what to avoid |
| `annotation.md` | Titles, labels, callouts — making the chart explain itself |
| `dashboard_design.md` | Layout, hierarchy, and flow when multiple charts share a canvas |
| `examples.md` | Before/after references and worked examples |

---

## Core principles

These five principles run through every file in this section. When in doubt, come back here.

**1. Start with the big idea.**
Every chart answers exactly one question. Write that question in plain language before touching any code. If you can't write it in one sentence, the chart isn't ready to be built.

**2. Choose the right chart, not a familiar one.**
The chart type should match the relationship in the data — comparison, distribution, composition, trend, or correlation. Defaulting to a bar chart or line chart because it's easy is a decision worth reconsidering every time.

**3. Use color to focus attention, not to decorate.**
Color is the loudest signal in a chart. Reserve it for the one thing that matters. Everything else should be grey or muted. If everything is colored, nothing is emphasized.

**4. Eliminate clutter ruthlessly.**
Gridlines, tick marks, borders, legends, and labels all compete for the reader's attention. Remove anything that doesn't directly support reading the data. The goal is the minimum necessary ink.

**5. Make the chart explain itself.**
A chart that needs a paragraph of context to understand has failed. Titles should state the insight, not describe the axes. Annotations should answer the question the reader will ask when they look at the most interesting part of the chart.

---

## How to use this section

These files are references, not checklists. The intended workflow is:

1. **Before building** — read `big_idea.md` and `chart_selection.md` to frame what you're making and why.
2. **While building** — use `color_usage.md` and `annotation.md` as a live reference.
3. **Before sharing** — check your output against `examples.md` to catch common problems.
4. **For dashboards** — treat `dashboard_design.md` as a separate layout pass after individual charts are done.

---

## Relationship to the rest of the toolkit

The `data_storytelling` section defines the *what* and *why*. The `functions` section (and any templates or snippets elsewhere in the repo) provide the *how* — reusable code that implements these principles so they don't need to be rebuilt from scratch each time.

If a function or template conflicts with a principle in this section, the principle wins. Update the code, not the standard.

---

## Source material

The principles here are drawn primarily from:

- *Storytelling with Data* — Cole Nussbaumer Knaflic (2015)
- *Storytelling with Data: Let's Practice!* — Cole Nussbaumer Knaflic (2019)

Where this toolkit diverges from the book, the divergence is intentional and documented in the relevant file.