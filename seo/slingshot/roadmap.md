# Slingshot SEO & Content Reset — Roadmap

**Evergreen · owned by the SEO Program agent (Agent 1).**
This is a living plan, not a fixed schedule. Each Monday the SEO Program agent reads this file, marks what moved, adjusts sequencing based on what actually happened, and commits the updated version back. Treat every date as a *target*, not a commitment — the plan flexes as rankings, crawl results, and the Reimagined launch evolve. The **Roadmap tab in the weekly report renders from this file's current state.**

- **Repo home:** `seo/slingshot/roadmap.md` (agent reads + rewrites here weekly)
- **Baseline set:** Jul 27, 2026 — DR 55 · 461 organic keywords (127 in top 3) · 1,225 referring domains · ~1,440 organic visits/mo (Ahrefs) · 185 organic Search sessions/wk (GA4) · 0 organic demos · AI share-of-voice pending (no Brand Radar report yet) · GSC not yet feeding Ahrefs
- **Last updated:** Jul 27, 2026
- **Status key:** `planned` · `in progress` · `done` · `changed` (with a note on why)

---

## Standing operating rules (read every Monday, before touching the plan)

**Roadmap ownership.** This file is mine to maintain. Each Monday: fetch it, set each row's Status from the live Slingshot task state, move finished weeks into the Completed log with the date, re-sequence upcoming weeks if priorities shifted (note *why* in the Changelog), add newly-emerged work, and commit the updated file back. Treat it as living — it will change week over week. The report's Roadmap tab renders from this file's current state.

**Creating content tasks.** When pushing a content item into the Content Production list, never create a bare title — write a full **BRIEF** into the description and tag the task `ready-to-write` so the Content Writer agent picks it up. Every brief must include:
1. Target keyword + search volume + search intent (informational / commercial / comparison).
2. The pillar and hub page it belongs to, and which pages to internal-link (up to hub, down to spokes).
3. Page type (hub / spoke / comparison / discipline) and target URL per the taxonomy.
4. The answer-first opening angle — the 40–60 word direct answer the page should lead with.
5. Any "own already" ranking to protect or consolidate.
6. A one-line reminder of the two-track rule: rank in today's vocabulary up top; seed the Reimagined vision deeper; no unshipped-feature claims.

Only tag `ready-to-write` once the brief is complete — a tagged task with no brief produces weak content.

> **Tag mechanism note:** Slingshot's MCP surface exposes no native tag/label primitive, so `ready-to-write` is applied as a `**[ready-to-write]**` marker on the first line of the task description. If a filterable field is wanted, formalize a "Content Stage" dropdown custom field with a "Ready to Write" option and switch to it.

**Guardrails that don't change:** rebuild on-domain (never start fresh); every removed URL gets a 301; marketing is the core ICP; only *this week's* slice goes into Slingshot at a time (WIP ~5).

---

## Lane 1 — Content & Rankings  (Agent 1 → Content Production list)

| Wk | Focus | Tasks | Status |
|----|-------|-------|--------|
| 1 | Baseline + comparisons | Baseline scoreboard (rankings, organic demos, AI share); draft `/compare/` hub; spec vs-Asana + vs-Monday | **done (baseline) · in progress (hub + spec briefs live, ready-to-write)** |
| 2 | Comparison build | Build `/compare/` hub; ship vs-Asana, vs-Monday | planned |
| 3 | Comparison build | Ship vs-ClickUp, vs-AgencyAnalytics, vs-Databox; spec the 3 P1 hubs | planned |
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
1. Read the Slingshot list(s) and set each row's **Status** from the live task state.
2. Move finished weeks down into the **Completed log** (below) with the date done.
3. Re-sequence upcoming weeks if priorities shifted — and note *why* in a one-line changelog.
4. Add new work as it emerges (this is evergreen — the six pillars will spawn spokes, migration will surface new fixes).
5. Commit the updated file back to `seo/slingshot/roadmap.md`.

## Completed log
- Wk 1 — Baseline scoreboard (rankings, organic demos, AI share of voice) — done 2026-07-27

## Changelog
- 2026-07-27 — Roadmap initialized in repo and baseline set (first run). Created the "SEO Content Production" section in the empty Content Production list; pushed Wk 1's slice live as full ready-to-write briefs (`/compare/` hub + vs-Asana/vs-Monday spokes). Flagged: GSC not feeding Ahrefs, and no AI-visibility (Brand Radar) report yet — both block two KPIs until resolved.
