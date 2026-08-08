# AI Visibility Report Standard

## Canonical template (shared across all products)
Every AI Visibility report is built from ONE shared executive-dashboard engine. The engine
(HTML shell + all CSS + all JS render logic) is IDENTICAL across Reveal, Slingshot, and Ignite UI;
products differ ONLY by (a) the `REPORT` data object injected into the page and (b) the `theme-*`
body class. This is what makes the three reports one reporting system.

Canonical sources (keep in sync — same engine bytes, different data):
- marketing-ai-system/07-templates/ai-visibility/reveal-canonical.html
- marketing-ai-system/07-templates/ai-visibility/slingshot-canonical.html
- marketing-ai-system/07-templates/ai-visibility/ignite-ui-canonical.html

Each run: copy the product's canonical template, replace ONLY the `REPORT` data object with the
run's values, and publish to the product's live path. NEVER hand-edit the shared CSS/JS, the render
functions, the tab logic, the copy button, or the theme system. If the shell must change, change it
once in the engine and re-apply to all three canonicals so they never diverge.

Preserve exactly: the three tabs (Report / Tasks / Summary), all CSS, all JS render functions,
task table/board/timeline views, the copy-summary button, WoW/sparkline/gauge/progress-bar
components, the NEW-task badge, and the theme tokens.

## Report reading order (executive-first)
The Report tab MUST render in this order — optimized for a 30-second executive scan before analyst detail:
1. Hero
2. Executive Dashboard — 4 KPI gauges (Overall Visibility, Prompt Coverage, Discovery Coverage,
   Competitive Citations), each with current, target, status color, and WoW delta. This block
   REPLACES the old Measurement Health table; the measurement-health status + note render as a
   single band directly beneath the gauges.
3. Goal Scoreboard — every 30-day and 90-day goal (see columns below), with a visual progress bar.
4. Executive Summary — What's Working (3 bullets) / Watch (3 bullets) / Priority (1 highest-impact move). No walls of text.
5. KPI Cards — the 6 headline metrics (Overall AI Visibility, Prompt Coverage, Discovery Topic
   Coverage, Competitive Citations, AI Answers Found, Average Prompt Position), each with value,
   target, WoW indicator, status color, and a sparkline where history exists.
6. Visibility Trends — with 30 Days / 90 Days / YTD window tabs that swap the chart without
   duplicating sections. Annotate any rebaseline point; never plot across a methodology change as if continuous.
7. Competitor Snapshot — horizontal share-of-voice bars (own brand highlighted). If per-competitor
   values can't be isolated, render an honest note instead of fabricated bars.
8. Topic Coverage — ranked horizontal bars (strengths/weaknesses obvious at a glance).
9. Supporting Evidence — condensed cards (by model, citations & sources, prompt audit, website readiness).
10. Definitions — plain-English glossary.

## Goal Progress Scorecard columns
Goal | Current | Target | Progress | Insight | Status
Every documented 30-day and 90-day goal must appear as a row with a progress bar and a status badge.
Do not hide goals only in prose. Group into "30-day goals" and "90-day goals".

## WoW everywhere
Every KPI shows a WoW indicator: increase, decrease, or unchanged, with the percentage/point
change where available, and a sparkline where >=2 comparable points exist. Never show an isolated
number without trend context.

## Tasks are single-source-of-truth
The Report tab must NOT contain a task list — only high-level references to work (e.g., in Priority).
All action items live in the Tasks tab, synced from Slingshot. Tag every task created during the
current run with a NEW badge (data-driven `isNew` flag on the task object).

## Data integrity
The same report ID, date, window, response count, visibility, rank, citations, topic values, and
freshness label must match everywhere in the file. All values are actual Amplitude AI Visibility
outputs — never fabricated. Presentation changes never alter calculations, scoring, task generation,
data sources, or standing decisions.
