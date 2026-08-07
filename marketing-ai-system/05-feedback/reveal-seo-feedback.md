# Reveal SEO Feedback

## Standing decisions

- Canonical report = `seo/reveal/analysis/index.html`. Each run copies it and swaps only run data, date, windows, and the task array. The two fixes below are baked into the canonical — preserve them; do not regress.
- Goal Scoreboard bars: `.bar` must be `display:inline-block;width:120px;height:8px;border-radius:999px;background:var(--graybg);overflow:hidden;vertical-align:middle` (it is an inline `<span>`, so without `display:inline-block` + explicit width/height the bar collapses and no progress renders). Keep the `.bar > i` fill rule as-is.
- Tasks-tab dates: Slingshot due/start dates are date-only `YYYY-MM-DD` and must display exactly as stored. Parse them with `localDate(iso){const [y,m,d]=iso.split('-').map(Number);return new Date(y,m-1,d);}` — never `new Date(iso)` (that parses as UTC midnight and shifts back a day in America/New_York). Use `localDate()` for TODAY and every due/start-date display, overdue check, sort, and board/timeline render.

## New feedback
