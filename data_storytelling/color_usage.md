# Color Usage

> Color is the most powerful attention-directing tool in a chart — and the most commonly misused. Every color choice should be deliberate, not decorative.

By the time you reach color, the Big Idea is written and the chart type is chosen. Color's job now is narrow and specific: make the one thing that matters impossible to miss, and make everything else recede.

---

## The core principle: color is a spotlight, not a paint bucket

The single biggest color mistake is using a different color for every category by default — most charting tools do this automatically, and most people never turn it off. The result is a chart where everything is visually loud and nothing is emphasized. If every bar is a different color, the reader has no idea which one matters.

Color should answer one question: **where do I want the reader to look first?** Everything else is the backdrop that makes that point land.

---

## The grey-first rule

Start every chart in grey. Add color only to the data points or categories that are directly part of the Big Idea.

```
Default state:     Every element is grey.
Add color:         Only to what the Big Idea is about.
Result:            One or two colored elements against a grey field.
```

This is the single highest-leverage habit in this file. A bar chart with eleven grey bars and one orange bar tells the reader exactly where to look before they've read a single label. The same chart with twelve different colors tells them nothing.

---

## Choosing the color itself

When something does need color, the choice is not arbitrary.

**Use one accent color, used consistently.** Pick a single color that will mean "this is the important thing" across the whole toolkit. Consistency here is what makes a viewer trust the signal — if the accent color sometimes means "important" and sometimes means "category 4," it stops working as a spotlight.

**Reserve red and green for their cultural meaning.** Red reads as negative, warning, or decrease. Green reads as positive, good, or increase. Don't use them as arbitrary categorical colors — if a chart has a red bar that doesn't mean "bad," the reader's instinct will fight the data.

**Check for colorblind accessibility.** Red/green combinations are the most common form of color blindness and the most common chart-color mistake. If red and green are both present and meaningful, add a secondary cue — position, label, or pattern — so the distinction doesn't rely on color alone.

**Limit the palette.** A chart with more than 2–3 colors is usually a sign that color is being used to separate categories that should be separated some other way (position, faceting, direct labeling) instead.

---

## Where color should go

| Use color for | Don't use color for |
|---|---|
| The single data point or series the Big Idea is about | Every category, by default, because the tool auto-assigns them |
| Highlighting a change, threshold, or outlier | Decoration, branding, or "making it pop" |
| A consistent meaning across the whole toolkit (e.g. one accent = focus) | Different meanings in different charts (inconsistent signal) |
| Distinguishing 2–3 genuinely distinct groups when needed | Distinguishing many groups — use direct labeling instead |

---

## Preattentive attributes: color is not the only tool

Knaflic's broader point is that color is one of several "preattentive attributes" — visual properties the brain processes before conscious attention kicks in. Others include size, position, and contrast. Color gets overused because it's the easiest to apply, not because it's always the best tool.

Before reaching for color, ask whether **position** or **size** could do the job instead:

- Sorting a bar chart by value (position) often draws the eye to the extremes without any color at all.
- Making one data label larger or bolder (size/weight) can highlight a number without touching the palette.
- Placing the key takeaway physically closer to the relevant data point (proximity) reduces the need for a legend entirely.

Color is most effective when it works *alongside* these, not as the only signal doing the work.

---

## Practical defaults for this toolkit

These are working defaults — keep them centralized in `base_style.py` (or equivalent) so every chart pulls from the same source rather than redefining color per-script.

- **Neutral / background:** a single grey, used for all non-highlighted data (e.g. `#B0B0B0` or similar — confirm against your actual style file).
- **Accent / focus:** one consistent color reserved for the data point the Big Idea is about.
- **Negative / warning:** red, used only when the meaning is genuinely negative.
- **Positive / good:** a green or blue, used only when the meaning is genuinely positive — confirm the choice doesn't clash with the accent color.

If a chart needs more than these four roles, that's usually a sign the chart is trying to say more than one thing — revisit the Big Idea before adding more colors.

---

## A quick self-check before shipping a chart

- If I removed all color from this chart, would I lose information, or just decoration?
- Is there exactly one thing the color is drawing my eye to?
- Does my accent color mean the same thing here as it does in every other chart in this toolkit?
- If a colorblind reader saw this, would the point still come across?

If any answer is uncomfortable, the color usage needs another pass.

---

## After this

Once color is doing its job, move to `annotation.md` — titles, labels, and callouts are the layer that explains *why* the colored element matters, not just *where* it is.

---

## Source

The grey-first principle, the spotlight framing, and the preattentive attributes concept are drawn from Chapter 5 of *Storytelling with Data* (Knaflic, 2015). The practical defaults and self-check are toolkit-specific and original to this repo.