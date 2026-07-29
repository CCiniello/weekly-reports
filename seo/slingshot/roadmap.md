# Slingshot SEO & Content Reset — Roadmap

**Evergreen · owned by the SEO Program agent (Agent 1).**
This is a living plan, not a fixed schedule. Each Monday the SEO Program agent reads this file, marks what moved, adjusts sequencing based on what actually happened, and commits the updated version back. Treat every date as a *target*, not a commitment. The **Roadmap tab in the weekly report renders from this file's current state.**

- **Repo home:** `seo/slingshot/roadmap.md` (agent reads + rewrites here weekly)
- **Baseline set:** Jul 27, 2026 — DR 55 · 461 organic keywords (127 in top 3) · 1,225 referring domains · ~1,440 organic visits/mo (Ahrefs) · 185 organic Search sessions/wk (GA4) · 0 organic demos · AI share-of-voice 3.1% (Amplitude, from 2026-07-28 report)
- **Last updated:** Jul 29, 2026
- **Status key:** `planned` · `in progress` · `done` · `changed` (with a note on why)

---

## Standing operating rules (read every Monday, before touching the plan)

**Roadmap ownership.** This file is mine to maintain. Each Monday: fetch it, set each row's Status from the live Slingshot task state, move finished weeks into the Completed log with the date, re-sequence upcoming weeks if priorities shifted (note *why* in the Changelog), add newly-emerged work, and commit the updated file back. The report's Roadmap tab renders from this file's current state.

**Weekly AI share-of-voice (added 2026-07-29).** Every run, pull Amplitude AI Visibility for Slingshot (orgBrandId **49405** — `scores`, `competitors`, `topics`) and put AI SoV in the report's KPI snapshot as a standing metric. Baseline 2026-07-28: **3.1%** (seen in 1 of 32 answers, avg rank 9.7) vs Asana 47% · monday 41% · ClickUp 25% · Databox 22%. We register **only** on the Comparisons topic (10%); 0% on marketing analytics / campaign management / marketing PM. Track the trend and the topic mix weekly.

**3–5 moves per week (added 2026-07-29).** Each week pick the **3–5 highest-leverage actions — never more** — spanning content, technical/cannibalization, LLM/AEO visibility, and content cleanup. Render them in the report's "This week — the N moves" section AND push them into Slingshot. Bias toward aggressive consolidation (do a whole cluster at once, not one page at a time) over timid single-page steps.

**Task assignment (added 2026-07-29 — REQUIRED).** Every task the agent creates in **Content Production OR Technical SEO** must be:
- **Assigned to Casey** (owner set, not left blank);
- given a **Start date and Due date**;
- have **Estimated Time** filled.
No unassigned, date-less, or estimate-less tasks — this applies to all task types (Website / Blog / SEO Optimization / cleanup).

**Creating & typing content tasks (finalized 2026-07-28).**
- Stamp the correct **org task type at creation** (`create_task` accepts `taskTypeId`; an existing task's type CANNOT be changed afterward):
  - **Website** — `e97e10ef_fd5c8e5d-bbdc-4e95-a332-4a1669ba91c3_ds` → indexable www pages: the P1 hubs, the category pillar, the `/compare/` hub + competitor "Compete" pages, discipline solution pages.
  - **Blog** — `e97e10ef_03d542a5-45d2-4d95-ac4e-c9ec4c605b12_ds` → editorial spokes (how-tos, templates, thought-leadership / Jason Beres bylines).
  - **SEO Optimization** — `e97e10ef_16ac6931-1f79-4dae-a048-4ef743748a43_ds` → work on existing pages: merges/consolidations, refreshes, interlinking, schema, 301s, on-page fixes.
- Write the full **BRIEF** into the description (all six brief elements below) AND fill the applicable **structured custom fields** so it's a full PM task. Website field values in use: Search Intent ∈ {Informational, Commercial Investigation, Transactional, Navigational, Thought Leadership, Pain Point}; Funnel ∈ {Top of Funnel, Mid Funnel, Bottom Funnel, Retention, Expansion}; Webpage Type ∈ {PPC Landing Page, Feature Page, Template Page, Solution / Use Case, Compete, Homepage, Integration Page, Glossary Page, Guide Page}. Comparison pages = Webpage Type "Compete" · Search Intent "Commercial Investigation" · Funnel "Bottom Funnel". If a needed field is missing on the type, flag Casey to add it.
- **Acceptance gate = Casey ticks the "Ready to Write" checkbox** (machine-readable). Create it unchecked. The old `[ready-to-write]` text marker is retired.
- **Comms loop:** Casey → agent via the task **comment / activity thread** (agent reads it reliably, including links). Agent → Casey via the **Agent Response** field (writes reliably) or a comment. The PMM Response rich-text field is retired (agent can't read human-typed rich text).

Every BRIEF must include: (1) target keyword + volume + intent; (2) pillar + hub + internal-link plan (up to hub, down to spokes); (3) page type + target URL per taxonomy; (4) the 40–60 word answer-first opening; (5) any "own already" ranking to protect/consolidate; (6) the two-track reminder (rank in today's vocabulary up top; seed the Reimagined vision deeper; no unshipped-feature claims).

> **Known MCP limitations (retry each run):**
> - **As of 2026-07-29 the Slingshot connector errors on ALL task endpoints for this org** — `list_tasks`, `get_task_list`, `list_custom_fields`, and every task write (assign, dates, estimate, custom fields) return "An error occurred invoking". Non-task endpoints (`list_workspaces`) work. **Net effect: the agent currently cannot read or modify tasks, assignments, dates, or estimates via MCP.** Until fixed, specify each task fully in the report/roadmap and have Casey apply in the UI; retry the writes each run. This is the same root cause as the earlier org custom-field write failures — a connector-side defect, not a setup issue.
> - **Posting** task comments via the MCP is also erroring (reading comments works when the task endpoints are up).
> - The **Ready to Write** checkbox lives on the Website type; confirm it also exists on Blog and SEO Optimization so the accept signal is uniform (add it if missing).

**/compare/ status:** the hub **EXISTS** (built ~mid-July 2026), just not SEO-optimized — treat it as an optimization target, not a net-new build. 301 the flat `/slingshot-vs-*/` comparison URLs into `/compare/…` spokes.

**Guardrails that don't change:** rebuild on-domain (never start fresh); every removed URL gets a 301; marketing is the core ICP; only *this week's* slice goes into Slingshot at a time (WIP ~5).

---

## This week's slice — ready to apply (owner: Casey · all P1)
_Assign each to Casey; start 2026-07-29; due 2026-08-02; estimate as noted. (Push blocked by the connector bug above — apply in the UI for now.)_

| # | Task | Type | Est. |
|---|------|------|------|
| 1 | Migrate all 14 `/slingshot-vs-*/` pages into `/compare/` (301 + optimize each) | SEO Optimization | 8h |
| 2 | Optimize the `/compare/` hub as the canonical anchor (answer-first, tables, interlinks) | SEO Optimization | 4h |
| 3 | Kill marketing-analytics cannibalization: stand up `/marketing-analytics/`, 301 the 3 dupes | Website | 6h |
| 4 | Kill campaign cannibalization: stand up `/campaign-management/`, 301 the 3 dupes | Website | 6h |
| 5 | Win "X vs Y" in AI answers: comparison schema + pitch the review/listicle domains LLMs cite | SEO Optimization | 3h |

---

## Lane 1 — Content & Rankings  (Agent 1 → Content Production list)

| Wk | Focus | Tasks | Status |
|----|-------|-------|--------|
| 1 | Comparisons + cannibalization (aggressive) | Migrate **all 14** `/slingshot-vs-*/` → `/compare/` (301 + optimize); optimize `/compare/` hub; kill marketing-analytics + campaign cannibalization (build canonical hubs, 301 dupes); comparison schema + AI-citation outreach | in progress |
| 2 | Hubs + interlink | Finalize the 3 P1 hub briefs; interlink the `/compare/` cluster; refresh AgencyAnalytics/Klipfolio spokes | planned |
| 3 | Comparison + hub prep | Optimize AgencyAnalytics + Databox + Klipfolio comparisons; finalize hub briefs | planned |
| 4 | P1 hub | Build `/marketing-analytics/` hub (consolidation target for Wk-1 301s) | planned |
| 5 | P1 hub | Build `/campaign-management/` hub (consolidation target for Wk-1 301s) | planned |
| 6 | P1 hub | Optimize existing `/marketing-project-management/` hub | planned |
| 7 | Consolidate + refresh | Merge 2 SEO pages → `/solutions/marketing/seo/`; refresh marketing-KPIs + content-KPIs winners, interlink to hubs | planned |
| 8 | Category pillar | Launch `/marketing-execution-platform/` + first thought-leadership spoke | planned |

## Lane 2 — Technical, IA & Cleanup  (Agent 2 → Technical + Cleanup lists)

| Wk | Focus | Tasks | Status |
|----|-------|-------|--------|
| 1 | Foundation | Full crawl + master URL inventory (traffic/backlinks/rankings); baseline health score; **fix revealbi.io form bug** | planned |
| 2 | Duplicates | Pick slash convention; 301 all trailing-slash duplicates; set canonicals | planned |
| 3 | Cannibalization | 301 campaign-mgmt duplicates into canonical hub; execute cannibalization map | planned |
| 4 | Taxonomy hygiene | Convert `/templates/?department=` → crawlable folders; flatten over-deep product URLs | planned |
| 5 | Redirect map | Build full new-taxonomy 301 map; test in staging | planned |
| 6 | Migration | Launch redirect map (controlled push); monitor GSC coverage + 404s daily | planned |
| 7 | Schema + sitemaps | Organization + SoftwareApplication + FAQ schema on money pages; clean XML sitemaps per section; submit in GSC | planned |
| 8 | Prune + AEO tech | 301 thin legacy blog posts into nearest hub; publish `llms.txt`; AI-bot crawlability audit | planned |

_Content-cleanup queue (from GA4 engagement): prune/re-angle off-ICP magnets that bounce hard — `/blog/top-task-management-tools/` (72% bounce), `/blog/what-is-micromanagement/` (converts nobody), `/blog/top-12-slack-alternatives/`; internal-link on-ICP winners (`/blog/types-of-data-analysis/` 67% eng, content-KPIs #9) up to the money hubs._

---

## How the agent maintains this
Each Monday, Agent 1 (and Agent 2 for Lane 2) will:
1. Read the Slingshot list(s) and set each row's **Status** from the live task state (Website/Blog/SEO-Optimization task with **Ready to Write = true** ⇒ accepted/in production; bare or unchecked ⇒ proposed/in triage).
2. Move finished weeks down into the **Completed log** (below) with the date done.
3. Re-sequence upcoming weeks if priorities shifted — and note *why* in the changelog.
4. Add new work as it emerges (the six pillars will spawn spokes; migration will surface fixes).
5. Commit the updated file back to `seo/slingshot/roadmap.md`.

## Completed log
- Wk 1 — Baseline scoreboard (rankings, organic demos, AI share of voice) — done 2026-07-27

## Changelog
- 2026-07-27 — Roadmap initialized in repo and baseline set (first run). Created the "SEO Content Production" section in the empty Content Production list; pushed Wk 1's slice live as full briefs (`/compare/` hub + vs-Asana/vs-Monday). Flagged: GSC not feeding Ahrefs, and no AI-visibility (Brand Radar) report yet.
- 2026-07-28 — Locked the content-task workflow (type-at-creation via Website/Blog/SEO Optimization; Ready-to-Write checkbox = accept gate; comments = Casey→agent, Agent Response = agent→Casey). Confirmed `/compare/` hub already exists, so Wk 1 shifts from "draft hub" to "optimize existing hub," and Wk 2 drops the hub-build — comparison work pulls forward ~1 week.
- 2026-07-29 — Wired Amplitude AI share-of-voice as a standing weekly KPI (3.1% baseline). Added the **3–5 moves/week** rule and went aggressive on Wk 1 (migrate ALL 14 comparison pages + kill both cannibalization clusters at once, vs. one page at a time). Added the **mandatory task-assignment rule** (owner = Casey + start/due + estimated time on every task). Report upgraded: aligned VP card, AI-SoV in scorecard + KPIs, new Analysis section (cannibalization / AI visibility / content cleanup), "This week — the 5 moves" moved onto the Report tab, GA4 engagement snapshot (device split + weekly sessions) + per-landing-page engagement/avg-time columns on Traffic. **Blocker:** Slingshot connector now errors on all task endpoints (read + write), so this week's slice is specified here + in the report but could not be pushed/assigned via MCP — apply in UI, retry next run.
