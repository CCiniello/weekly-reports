# Slingshot SEO & Content Reset — Roadmap

**Evergreen · owned by the SEO Program agent (Agent 1).**
This is a living plan, not a fixed schedule. Each Monday the SEO Program agent reads this file, marks what moved, adjusts sequencing based on what actually happened, and commits the updated version back. Treat every date as a *target*, not a commitment. The **Roadmap tab in the weekly report renders from this file's current state.** The report is organized as tabs — **Report · Traffic · Tasks · Roadmap · Sitemap · Summary · Cheat sheet** — where the **Roadmap tab is now a visual two-lane 8-week timeline** and the **Sitemap tab is a page-cleanup tracker** (every URL grouped by verdict, read live from `sitemap.json`).

- **Repo home:** `seo/slingshot/roadmap.md` (agent reads + rewrites here weekly)
- **Baseline set:** Jul 27, 2026 — DR 55 · 461 organic keywords (127 in top 3) · 1,225 referring domains · ~1,440 organic visits/mo (Ahrefs) · 185 organic Search sessions/wk (GA4) · 0 organic demos · AI share-of-voice 3.1% (Amplitude, from 2026-07-28 report)
- **Current read (Aug 3, 2026):** DR 55 · 409 organic keywords (106 in top 3) · 1,263 referring domains · ~1,227 organic visits/mo (Ahrefs) · GSC 212 clicks/wk (flat) · 179,052 impressions/wk (+18% WoW) · avg pos 33.2 · 151 organic sessions/wk (GA4, declining) · 0 organic demos · 1 organic first-login · AI SoV 3.1% (no new Amplitude report this week — still the 2026-07-28 run)
- **Last updated:** Aug 3, 2026
- **Status key:** `planned` · `in progress` · `done` · `changed` (with a note on why)

---

## Standing operating rules (read every Monday, before touching the plan)

**Read the live task list first (added 2026-08-03).** Every Monday, *before* planning, the agent reads the **live Slingshot task list** to capture status, completions, and due-date changes — reconciling reality against this file — and only then re-sequences the plan and picks the week's moves. The report's Tasks and Roadmap tabs are refreshed from this live read each Monday.

**Roadmap ownership.** This file is mine to maintain. Each Monday: fetch it, set each row's Status from the live Slingshot task state, move finished weeks into the Completed log with the date, re-sequence upcoming weeks if priorities shifted (note *why* in the Changelog), add newly-emerged work, and commit the updated file back. The report's Roadmap tab renders from this file's current state as a visual two-lane 8-week timeline.

**Weekly AI share-of-voice (added 2026-07-29).** Every run, pull Amplitude AI Visibility for Slingshot (orgBrandId **49405** — `scores`, `competitors`, `topics`) and put AI SoV in the report's KPI snapshot as a standing metric. Baseline 2026-07-28: **3.1%** (seen in 1 of 32 answers, avg rank 9.7) vs Asana 47% · monday 41% · ClickUp 25% · Databox 22%. We register **only** on the Comparisons topic (10%); 0% on marketing analytics / campaign management / marketing PM. Track the trend and the topic mix weekly. **Note:** the Amplitude report is a monthly crawl — expect the same numbers week-to-week until a new report runs; report the run date so a stale read isn't mistaken for a fresh one. The report surfaces this in a dedicated **AI Visibility** section (competitive Share-of-Voice table + topic-coverage tiles).

**3–5 moves per week (added 2026-07-29).** Each week pick the **3–5 highest-leverage actions — never more** — spanning content, technical/cannibalization, LLM/AEO visibility, and content cleanup. Surface them in the report's **Tasks tab** (the standalone "This week — the N moves" section on the Report tab is **retired** as of 2026-08-03) AND push them into Slingshot. Items created this Monday are badged **NEW** in the Tasks tab; carryovers are not. Bias toward aggressive consolidation (do a whole cluster at once, not one page at a time) over timid single-page steps.

**Task assignment (added 2026-07-29 — REQUIRED).** Every task the agent creates in **Content Production OR Technical SEO** must be:
- **Assigned to Casey** (owner set, not left blank);
- given a **Start date and Due date**;
- have **Estimated Time** filled.
No unassigned, date-less, or estimate-less tasks — this applies to all task types (Website / Blog / SEO Optimization / cleanup). *(MCP note: assignee + start/due are writable and now enforced; the Time-Tracking `estimated` field is still NOT writable via the connector, so estimates are carried in the brief text — "Est: Nh" — and surfaced in the report's Tasks tab until the field opens up. Confirmed again 2026-08-03.)*

**Creating & typing content tasks (finalized 2026-07-28).**
- Stamp the correct **org task type at creation** (`create_task` accepts `taskTypeId`; an existing task's type CANNOT be changed afterward):
  - **Website** — `e97e10ef_fd5c8e5d-bbdc-4e95-a332-4a1669ba91c3_ds` → indexable www pages: the P1 hubs, the category pillar, the `/compare/` hub + competitor "Compete" pages, discipline solution pages.
  - **Blog** — `e97e10ef_03d542a5-45d2-4d95-ac4e-c9ec4c605b12_ds` → editorial spokes (how-tos, templates, thought-leadership / Jason Beres bylines).
  - **SEO Optimization** — `e97e10ef_16ac6931-1f79-4dae-a048-4ef743748a43_ds` → work on existing pages: merges/consolidations, refreshes, interlinking, schema, 301s, on-page fixes.
- Write the full **BRIEF** into the description (all six brief elements below) AND fill the applicable **structured custom fields** so it's a full PM task. Website field values in use: Search Intent ∈ {Informational, Commercial Investigation, Transactional, Navigational, Thought Leadership, Pain Point}; Funnel ∈ {Top of Funnel, Mid Funnel, Bottom Funnel, Retention, Expansion}; Webpage Type ∈ {PPC Landing Page, Feature Page, Template Page, Solution / Use Case, Compete, Homepage, Integration Page, Glossary Page, Guide Page}. Comparison pages = Webpage Type "Compete" · Search Intent "Commercial Investigation" · Funnel "Bottom Funnel". **The Website-type structured custom fields (Search Intent / Funnel / Webpage Type) plus the time-estimate are NOT yet writable via MCP**, so these values are written into the brief text (labeled "Fields to set in the panel") AND surfaced per-task in the report's **Tasks tab** for Casey to apply in the UI, until the connector supports writes.
- **Acceptance gate = Casey ticks the "Ready to Write" checkbox** (machine-readable). Create it unchecked. The old `[ready-to-write]` text marker is retired.
- **Comms loop:** Casey → agent via the task **comment / activity thread** (agent reads it reliably, including links). Agent → Casey via the **Agent Response** field (writes reliably) or a comment. The PMM Response rich-text field is retired (agent can't read human-typed rich text).

Every BRIEF must include: (1) target keyword + volume + intent; (2) pillar + hub + internal-link plan (up to hub, down to spokes); (3) page type + target URL per taxonomy; (4) the 40–60 word answer-first opening; (5) any "own already" ranking to protect/consolidate; (6) the two-track reminder (rank in today's vocabulary up top; seed the Reimagined vision deeper; no unshipped-feature claims).

> **Known MCP limitations (retry each run):**
> - **RESOLVED 2026-08-03:** the Slingshot task endpoints are working again. `list_tasks`, `get_task`, `list_task_sections`, `update_task` (assign / dates) and `create_task` (with type) all succeed. This week's slice was pushed + assigned via MCP for the first time.
> - **Still broken:** the Time-Tracking `estimated` field can't be written via `create_task`/`update_task` (stays 0). Estimates live in the brief text. Structured Website custom fields (Search Intent / Funnel / Webpage Type) also aren't writable — carried in the brief and surfaced in the report's Tasks tab until the connector supports writes.
> - Confirm the **Ready to Write** checkbox exists on Blog + SEO Optimization types (not just Website) so the accept signal is uniform.

**/compare/ status:** the hub **EXISTS** (built ~mid-July 2026), just not SEO-optimized — treat it as an optimization target, not a net-new build. 301 the flat `/slingshot-vs-*/` comparison URLs into `/compare/…` spokes.

**Guardrails that don't change:** rebuild on-domain (never start fresh); every removed URL gets a 301; marketing is the core ICP; only *this week's* slice goes into Slingshot at a time (WIP ~5).

---

## This week's slice — LIVE in Slingshot (owner: Casey · all P1 · start 2026-08-03 · due 2026-08-09)
_Rendered in the report's **Tasks tab** (not the Report tab). All five are assigned to Casey with start/due dates in Slingshot. Estimates + the structured fields (Search Intent / Funnel / Webpage Type) shown here and in each brief and the Tasks tab (not yet MCP-writable)._

| # | Task | Type | Est. | State |
|---|------|------|------|-------|
| 1 | Migrate + optimize `/slingshot-vs-asana/` → `/compare/slingshot-vs-asana/` (301 + optimize) | SEO Optimization | 3h | carried over, re-dated |
| 2 | Migrate + optimize `/slingshot-vs-monday/` → `/compare/slingshot-vs-monday/` (301 + optimize) | Website (Compete) | 3h | carried over, re-dated |
| 3 | Optimize the `/compare/` hub as the canonical anchor (answer-first, tables, interlinks) | SEO Optimization | 4h | carried over, re-dated |
| 4 | Kill marketing-analytics cannibalization: stand up `/marketing-analytics/`, 301 the 3 dupes | Website | 6h | NEW this week |
| 5 | Kill campaign cannibalization: stand up `/campaign-management/`, 301 the 3 dupes | Website | 6h | NEW this week |

_Queued for next week (not pushed yet, per WIP ~5): comparison-schema + FAQ schema on `/compare/` pages and AI-citation outreach to the review/listicle domains LLMs cite (the AEO move); content cleanup of the off-ICP bounce magnets (`/blog/top-task-management-tools/` 17% eng, `/blog/top-12-slack-alternatives/`) and fold `/blog/trello-vs-asana/` + `/blog/wrike-vs-asana/` into their `/compare/` spokes; migrate the next comparison batch (agencyanalytics, klipfolio, databox, notion)._

---

## Lane 1 — Content & Rankings  (Agent 1 → Content Production list)

| Wk | Focus | Tasks | Status |
|----|-------|-------|--------|
| 1 | Comparisons + cannibalization (aggressive) | Migrate `/slingshot-vs-*/` → `/compare/` (301 + optimize); optimize `/compare/` hub; kill marketing-analytics + campaign cannibalization (build canonical hubs, 301 dupes) | in progress |
| 2 | Comparison batch + AEO | Migrate + optimize the next comparison batch (agencyanalytics, klipfolio, databox, notion); comparison + FAQ schema; AI-citation outreach | planned |
| 3 | Hubs + interlink | Interlink the `/compare/` cluster and the new analytics/campaign hubs; refresh AgencyAnalytics/Klipfolio spokes | planned |
| 4 | P1 hub | Optimize existing `/marketing-project-management/` hub; consolidate `/solutions/marketing/project-management/` into it | planned |
| 5 | Consolidate SEO | Merge 2 SEO pages → `/solutions/marketing/seo/`; interlink template winners up to it | planned |
| 6 | Refresh winners | Refresh marketing-KPIs + content-KPIs winners, interlink to the money hubs | planned |
| 7 | Category pillar | Launch `/marketing-execution-platform/` category pillar | planned |
| 8 | Thought leadership | First Jason Beres byline spoke seeding the category + GEO assets | planned |

## Lane 2 — Technical, IA & Cleanup  (Agent 2 → Technical + Cleanup lists)

| Wk | Focus | Tasks | Status |
|----|-------|-------|--------|
| 1 | Foundation | Full crawl + master URL inventory — DONE; surfaced: **568 broken redirects + 180 canonical-to-redirect**, **403 on locale pages + hreflang** (P1), old help-centre `.html` 500s (P2), 47 orphan pages (P3), malformed `/in-the-news/` pagination (P3); **fix revealbi.io form bug** (in progress) | in progress |
| 2 | Duplicates | Pick slash convention; 301 all trailing-slash duplicates; set canonicals (in progress — pulled forward) | in progress |
| 3 | Redirects + errors | Repoint the 568 broken redirects to final 200 targets; fix 403 locale/hreflang; fix help-centre `.html` | planned |
| 4 | Cannibalization tech | Execute the 301 maps for the analytics + campaign consolidations (pairs with Lane 1 Wk1 hubs) | planned |
| 5 | Taxonomy hygiene | Convert `/templates/?department=` → crawlable folders; flatten over-deep product URLs | planned |
| 6 | Migration | Launch full redirect map (controlled push); monitor GSC coverage + 404s daily | planned |
| 7 | Schema + sitemaps | Organization + SoftwareApplication + FAQ schema on money pages; clean XML sitemaps per section; submit in GSC | planned |
| 8 | Prune + AEO tech | 301 thin legacy blog posts into nearest hub; publish `llms.txt`; AI-bot crawlability audit | planned |

_Content-cleanup queue (from GA4 engagement): prune/re-angle off-ICP magnets that bounce hard — `/blog/top-task-management-tools/` (17% engagement, confirmed Aug 3), `/blog/what-is-micromanagement/` (converts nobody), `/blog/top-12-slack-alternatives/`; internal-link on-ICP winners (`/blog/types-of-data-analysis/` 75% eng this week) up to the money hubs._

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
- Lane 2 — Full crawl + master URL inventory + baseline health score — done ~2026-08-01 (surfaced the redirect/locale/help-centre backlog now sequenced into Lane 2 Wk 2–3)

## Changelog
- 2026-07-27 — Roadmap initialized in repo and baseline set (first run). Created the "SEO Content Production" section in the empty Content Production list; pushed Wk 1's slice live as full briefs (`/compare/` hub + vs-Asana/vs-Monday). Flagged: GSC not feeding Ahrefs, and no AI-visibility (Brand Radar) report yet.
- 2026-07-28 — Locked the content-task workflow (type-at-creation via Website/Blog/SEO Optimization; Ready-to-Write checkbox = accept gate; comments = Casey→agent, Agent Response = agent→Casey). Confirmed `/compare/` hub already exists, so Wk 1 shifts from "draft hub" to "optimize existing hub," and Wk 2 drops the hub-build — comparison work pulls forward ~1 week.
- 2026-07-29 — Wired Amplitude AI share-of-voice as a standing weekly KPI (3.1% baseline). Added the **3–5 moves/week** rule and went aggressive on Wk 1. Added the **mandatory task-assignment rule**. Report upgraded (VP card, AI-SoV in scorecard + KPIs, Analysis section, This-week moves on Report tab, GA4 engagement snapshot). **Blocker:** Slingshot connector errored on all task endpoints, so the slice was specified but not pushed/assigned via MCP.
- 2026-08-03 — **Slingshot task endpoints back online.** Pushed + assigned this week's slice via MCP for the first time: the 3 carried-over comparison tasks (vs-asana, vs-monday, `/compare/` hub) were unassigned/date-less/overdue (due 08-02) — now **assigned to Casey, start 08-03, due 08-09**. Created 2 NEW Website tasks: **build `/marketing-analytics/` hub** and **build `/campaign-management/` hub**, each 301-consolidating its 3 cannibalizing dupes — pulling the hub builds forward from Wk 4–5 into now because a canonical hub is the prerequisite for the two AI-visibility topics where we score **0%**. Re-sequenced Lane 1 (comparison batch + AEO becomes Wk 2; queued schema/outreach + content cleanup for next week to hold WIP ~5). Lane 2 foundation crawl marked done; its findings (568 broken redirects, 403 locale/hreflang, help-centre 500s) sequenced into Wk 2–3; slash-convention pulled forward and in progress. **Honest read:** organic footprint contracted WoW (keywords 461→409, top-3 127→106, Ahrefs traffic ~1,440→1,227, GA4 sessions still sliding) while GSC impressions rose +18% — expected volatility on a low reset baseline before the consolidations ship; watch next week. AI SoV unchanged at 3.1% (no new Amplitude crawl since 07-28).
- 2026-08-03 — **Report redesign.** Reorganized the weekly report into seven tabs — **Report · Traffic · Tasks · Roadmap · Sitemap · Summary · Cheat sheet**. Moved this week's work off the Report tab into a dedicated **Tasks tab** rendering each task's full field set (Type · Status · Owner · Start · Due · Estimate · Priority · Primary keyword + volume · Search Intent · Funnel · Webpage Type · Target URL · Slingshot link), with **NEW** badges on the two Monday-created hubs and "carryover" on the three comparison moves; **retired** the standalone "This week — the 5 moves" section from the Report tab. Added an **AI Visibility** section (competitive Share-of-Voice table + topic-coverage tiles) to the Report tab and folded the old Analysis points (cannibalization is the throttle; +18% impressions vs flat clicks; content-cleanup of bounce magnets) into the top VP-readout narrative, then removed the standalone Analysis block. Rebuilt the **Roadmap tab as a visual two-lane 8-week timeline** with live status (Lane 1 Content, Lane 2 Technical/Cleanup), and the **Sitemap tab as a page-cleanup tracker** grouping every URL by verdict with per-group counts (still reading live from `sitemap.json`). Tightened the KPI/scorecard grid to fit more per row; added the **Cheat sheet** tab (pillars, two-track rule, guardrails, glossary); removed the interactive-feedback icons/modal and the "artifact" pointer — the static GitHub page is the sole deliverable now. Added the standing rule to **read the live Slingshot task list every Monday first** (status/completions/due-date changes) before planning.
