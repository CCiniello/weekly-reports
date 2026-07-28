# Slingshot SEO & Content Reset — Roadmap

**Evergreen · owned by the SEO Program agent (Agent 1).**
This is a living plan, not a fixed schedule. Each Monday the SEO Program agent reads this file, marks what moved, adjusts sequencing based on what actually happened, and commits the updated version back. Treat every date as a *target*, not a commitment. The **Roadmap tab in the weekly report renders from this file's current state.**

- **Repo home:** `seo/slingshot/roadmap.md` (agent reads + rewrites here weekly)
- **Baseline set:** Jul 27, 2026 — DR 55 · 461 organic keywords (127 in top 3) · 1,225 referring domains · ~1,440 organic visits/mo (Ahrefs) · 185 organic Search sessions/wk (GA4) · 0 organic demos · AI share-of-voice pending (no Brand Radar report yet) · GSC not yet feeding Ahrefs
- **Last updated:** Jul 28, 2026
- **Status key:** `planned` · `in progress` · `done` · `changed` (with a note on why)

---

## Standing operating rules (read every Monday, before touching the plan)

**Roadmap ownership.** This file is mine to maintain. Each Monday: fetch it, set each row's Status from the live Slingshot task state, move finished weeks into the Completed log with the date, re-sequence upcoming weeks if priorities shifted (note *why* in the Changelog), add newly-emerged work, and commit the updated file back. The report's Roadmap tab renders from this file's current state.

**Creating & typing content tasks (finalized 2026-07-28).**
- Stamp the correct **org task type at creation** (`create_task` accepts `taskTypeId`; an existing task's type CANNOT be changed afterward):
  - **Website** — `e97e10ef_fd5c8e5d-bbdc-4e95-a332-4a1669ba91c3_ds` → indexable www pages: the P1 hubs, the category pillar, the `/compare/` hub + competitor "Compete" pages, discipline solution pages.
  - **Blog** — `e97e10ef_03d542a5-45d2-4d95-ac4e-c9ec4c605b12_ds` → editorial spokes (how-tos, templates, thought-leadership / Jason Beres bylines).
  - **SEO Optimization** — `e97e10ef_16ac6931-1f79-4dae-a048-4ef743748a43_ds` → work on existing pages: merges/consolidations, refreshes, interlinking, schema, 301s, on-page fixes.
- Write the full **BRIEF** into the description (all six brief elements below) AND fill the applicable **structured custom fields** so it's a full PM task. Website field values in use: Search Intent ∈ {Informational, Commercial Investigation, Transactional, Navigational, Thought Leadership, Pain Point}; Funnel ∈ {Top of Funnel, Mid Funnel, Bottom Funnel, Retention, Expansion}; Webpage Type ∈ {PPC Landing Page, Feature Page, Template Page, Solution / Use Case, Compete, Homepage, Integration Page, Glossary Page, Guide Page}. Comparison pages = Webpage Type "Compete" · Search Intent "Commercial Investigation" · Funnel "Bottom Funnel". If a needed field is missing on the type, flag Casey to add it.
- **Acceptance gate = Casey ticks the "Ready to Write" checkbox** (machine-readable). Create it unchecked. The old `[ready-to-write]` text marker is retired.
- **Comms loop:** Casey → agent via the task **comment / activity thread** (agent reads it reliably, including links). Agent → Casey via the **Agent Response** field (writes reliably) or a comment. The PMM Response rich-text field is retired (agent can't read human-typed rich text).

Every BRIEF must include: (1) target keyword + volume + intent; (2) pillar + hub + internal-link plan (up to hub, down to spokes); (3) page type + target URL per taxonomy; (4) the 40–60 word answer-first opening; (5) any "own already" ranking to protect/consolidate; (6) the two-track reminder (rank in today's vocabulary up top; seed the Reimagined vision deeper; no unshipped-feature claims).

> **Known MCP limitations (as of 2026-07-28, retry each run):**
> - Writing **org-scoped custom fields** via the MCP is erroring (tried by field name AND field ID, single and multi) — personal-type fields and the description write fine. Until fixed, put all field values in the brief text and either retry the structured-field writes next run or have Casey fill them in the UI.
> - **Posting** task comments via the MCP is erroring (reading comments works).
> - The **Ready to Write** checkbox lives on the Website type; confirm it also exists on Blog and SEO Optimization so the accept signal is uniform (add it if missing).

**/compare/ status:** the hub **EXISTS** (built ~mid-July 2026), just not SEO-optimized — treat it as an optimization target, not a net-new build. 301 the flat `/slingshot-vs-*/` comparison URLs into `/compare/…` spokes.

**Guardrails that don't change:** rebuild on-domain (never start fresh); every removed URL gets a 301; marketing is the core ICP; only *this week's* slice goes into Slingshot at a time (WIP ~5).

---

## Lane 1 — Content & Rankings  (Agent 1 → Content Production list)

| Wk | Focus | Tasks | Status |
|----|-------|-------|--------|
| 1 | Baseline + comparisons | Baseline scoreboard (done); **optimize existing `/compare/` hub**; build vs-Asana + vs-Monday "Compete" pages | in progress |
| 2 | Comparison build | Ship vs-ClickUp; consolidate `/slingshot-vs-agency-analytics/` + `/slingshot-vs-klipfolio/` into `/compare/…` spokes (301); spec the 3 P1 hubs | planned |
| 3 | Comparison + hub prep | Ship vs-Databox; finalize the 3 P1 hub briefs | planned |
| 4 | P1 hub | Build `/marketing-analytics/` hub | planned |
| 5 | P1 hub | Build `/campaign-management/` hub | planned |
| 6 | P1 hub | Build `/marketing-project-management/` hub | planned |
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
- 2026-07-28 — Locked the content-task workflow (type-at-creation via Website/Blog/SEO Optimization; Ready-to-Write checkbox = accept gate; comments = Casey→agent, Agent Response = agent→Casey). Confirmed `/compare/` hub already exists, so Wk 1 shifts from "draft hub" to "optimize existing hub," and Wk 2 drops the hub-build — comparison work pulls forward ~1 week. Rebuilt Wk 1's tasks as properly-typed PM tasks: 1 SEO Optimization (optimize `/compare/`) + 2 Website "Compete" pages (vs-Asana, vs-Monday); full briefs in descriptions. Flagged MCP limits: org custom-field writes and comment-posting are erroring (retry next run).
