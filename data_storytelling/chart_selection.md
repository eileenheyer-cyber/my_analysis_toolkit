# Chart Selection

> The right chart is the one that makes the relationship in your data visible as fast as possible. Choose by what you need to show, not by what you already know how to build.

Chart selection happens after the Big Idea is written and before any code is touched. The Big Idea tells you *what* the chart must communicate. The chart type determines *how* that communication lands. A mismatch between the two — the right data in the wrong chart — is one of the most common reasons a chart fails to persuade.

---

## Start with the relationship, not the data

Knaflic organises chart choice around a single question: **what relationship in the data is the point?**

There are five. Every chart you will ever build fits into one of them.

| Relationship | The question you are answering |
|---|---|
| **Comparison** | How do these things rank or differ from each other? |
| **Trend** | How does this change over time? |
| **Distribution** | How is this spread across a range? |
| **Composition** | How do parts relate to a whole? |
| **Correlation** | Do these two things move together? |

Identify the relationship first. The chart type follows from it. If you find yourself picking the chart before you can name the relationship, stop — the Big Idea probably needs more work.

---

## The decision guide

### Comparison
You are showing how categories rank or differ at a point in time.

```
How many categories?
├── Few (2–7)  →  Horizontal bar chart
│                 (easier to read labels, natural ranking order)
└── Many (8+)  →  Still a bar chart, but reconsider:
                  can the Big Idea survive this many categories?
                  If not, group or filter before building.
```

**Use:** Bar chart (vertical or horizontal)
**Avoid:** Pie chart — humans are poor at comparing angles and arc lengths. A bar chart of the same data is almost always clearer.
**Avoid:** Radar/spider chart — distorts comparison by encoding values as distance from a centre point across arbitrary axes.

---

### Trend
You are showing how a single measure changes over time. Time is always on the x-axis.

```
Is the change continuous or discrete?
├── Continuous (daily, monthly, quarterly)  →  Line chart
└── Discrete (e.g. annual survey snapshots)  →  Bar chart or connected dot plot
```

**Use:** Line chart for continuous time series. The line implies connection between points — only use it when that connection is meaningful (i.e. the thing being measured existed between the data points).
**Avoid:** Bar chart for long continuous time series — bars imply discrete, separate counts, and become unreadable beyond ~12 bars.
**Avoid:** Dual-axis charts — they allow the visual relationship between two lines to be manipulated by rescaling either axis. If two measures matter, build two charts.

---

### Distribution
You are showing how values spread across a range — where they cluster, where they thin out, and whether there are outliers.

```
How many data points?
├── Few (< ~30)         →  Strip plot or dot plot
├── Moderate (~30–200)  →  Box plot (if audience knows how to read one)
│                          or violin plot
└── Many (200+)         →  Histogram
```

**Use:** Histogram for large datasets — it shows the shape of the distribution (normal, skewed, bimodal) clearly.
**Use:** Box plot when comparing distributions across multiple groups side by side.
**Avoid:** Pie chart — it cannot show distribution, only composition.
**Avoid:** Summarising a distribution as a single average in a bar chart unless the spread genuinely does not matter to the Big Idea. An average hides the shape.

---

### Composition
You are showing how parts make up a whole, and the whole always equals 100%.

```
Is the composition changing over time?
├── No (static snapshot)    →  Single stacked bar or waffle chart
│                              (pie chart only if 2–3 categories max)
└── Yes (over time)         →  Stacked bar chart (not stacked area —
                               harder to read individual segment changes)
```

**Use:** Stacked bar chart for composition over time — each bar is 100%, segments show changing proportions.
**Use:** Pie chart only when there are 2 or 3 categories and the point is about one dominant share (e.g. "two-thirds of revenue comes from one product"). More than 3 slices and a bar chart is clearer.
**Avoid:** Exploded pie charts — pulling a slice out does not make a pie chart easier to read, it makes it harder.
**Avoid:** 3D charts of any kind — the third dimension adds no information and distorts the areas being compared.

---

### Correlation
You are showing whether and how two continuous variables move together.

```
Are you showing the relationship itself, or individual data points?
├── The relationship (pattern, trend)  →  Scatter plot with a trend line
└── Individual points matter           →  Scatter plot, labelled selectively
```

**Use:** Scatter plot — it is the only chart type that directly encodes two continuous variables simultaneously.
**Use:** Trend line (regression line) when the direction of the relationship is the point, not the individual points.
**Avoid:** Line chart — a line chart implies time on the x-axis. If neither variable is time, a line chart misrepresents the relationship.
**Avoid:** Bubble chart unless the third variable (bubble size) is central to the Big Idea. Bubble size is hard to read accurately and adds cognitive load.

---

## The chart you should almost never use

Knaflic is direct about this: **the pie chart is almost always the wrong choice.**

The reason is perceptual. Humans judge length and position accurately. We judge angle and area poorly. A bar chart encodes the same information as a pie chart using length, which is the most accurately perceived visual attribute. The only scenario where a pie chart earns its place is when you have two or three categories and the point is about one dominant share — and even then, a single stacked bar chart is cleaner.

This is not a rule against ever using a pie chart. It is a rule that every pie chart in this toolkit should be a deliberate exception, not a default.

---

## The simplicity rule

When two chart types could both show the relationship correctly, choose the simpler one. Simplicity here means:

- Fewer chart elements for the reader to decode
- A chart type the audience has seen before
- No secondary axis, no dual encoding, no colour gradient

Novelty is not a virtue in chart selection. A chart the audience has never seen before asks them to learn how to read it before they can understand what it says. That is cognitive load the Big Idea has to overcome before it even lands.

The only time a less familiar chart type is justified is when the familiar one genuinely cannot show the relationship — not when the unfamiliar one looks more impressive.

---

## Quick reference

| You want to show | Reach for | Avoid |
|---|---|---|
| How categories compare | Horizontal bar chart | Pie chart, radar chart |
| Change over continuous time | Line chart | Bar chart (long series) |
| Change at discrete time points | Bar chart | Line chart |
| How values are distributed | Histogram, box plot | Bar chart of averages |
| How parts make a whole | Stacked bar, pie (2–3 cats only) | 3D charts, exploded pie |
| Whether two variables correlate | Scatter plot | Line chart, bubble chart |

---

## After choosing

Once the chart type is selected, move to `color_usage.md` to determine how attention will be directed within it, and `annotation.md` to determine what text the chart needs to carry its own meaning.

For worked examples of each chart type, see `examples.md`.

---

## Source

The relationship-first framework and chart type guidance are drawn from Chapters 2 and 3 of *Storytelling with Data* (Knaflic, 2015). The decision trees, quick reference table, and toolkit-specific rules are original to this repo. The position on pie charts reflects Knaflic's own stated view.