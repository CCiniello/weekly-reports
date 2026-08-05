# Task Creation Standard

## 1. Creation threshold

Create or materially update a task only when all conditions are true:

- It supports a documented Reveal goal.
- It is based on an approved, available source.
- It is not a duplicate of an open, in-progress, deferred, or recently completed task.
- It was not rejected through feedback unless materially new evidence justifies reopening it.
- Confidence is High.
- An owner can be assigned deterministically.
- A realistic due date can be set.
- All required fields can be populated.
- Completion can be verified through acceptance criteria and a success KPI.

Medium-confidence actions belong in Proposed Actions or Open Questions. Low-confidence observations remain in the report only.

## 2. Weekly limits

- Maximum genuinely new tasks per run: **5**
- Maximum designated weekly priorities: **3**
- Maximum urgent/critical new task: **1**
- Update existing tasks before creating new ones.
- Do not create an investigation task and an implementation task for the same unknown in the same run.

## 3. Priority scoring

Score each candidate 1–5.

Priority score:
- Qualified lead potential: 30%
- Commercial intent: 20%
- Proximity to a ranking/conversion win: 15%
- Strategic goal alignment: 15%
- Evidence confidence: 10%
- Effort/dependency feasibility: 10%

For effort/dependency feasibility, 5 means low effort/few dependencies and 1 means high effort/heavy dependencies.

Only the highest-scoring valid actions should become tasks.

## 4. Required task content

Each task must include:
- Action-led title
- Product = Reveal
- Track
- Category
- Cluster
- Primary SEO Keyword
- Current Rankings from GSC
- Why it Matters
- Step by Step Fix
- Success KPI
- Insight/evidence
- Effort: S, M, or L
- Native priority
- Owner
- Due date
- Dependencies
- Acceptance criteria
- Links to the report and relevant source/task/page
- Goal supported
- Confidence
- Priority score

## 5. Owner routing

- Technical task: assign **Dian Jelyazkov** only. Post a plain-text FYI comment naming **Sathya Sundaresan** and his email. The current connector cannot create a native notifying mention, so never claim he was notified.
- All other Reveal SEO tasks: assign **Casey Ciniello**.
- Never assign Alex.
- Do not add Sathya as a second assignee unless Casey changes this rule.

## 6. Default due-date rules

Use business days and respect existing dependencies.

| Work type | Default due date |
|---|---|
| Critical tracking, broken form, or configuration issue | 1–2 business days |
| Technical SEO fix | 5–10 business days |
| On-page optimization | 7 business days |
| Internal-linking change | 5 business days |
| New money-page brief/specification | 10 business days |
| Full page production | Use the existing project plan; never invent a launch date |
| Investigation or validation | 3 business days |
| Monthly-audit follow-up | Before the next monthly run |
| Backlink/digital PR action | 15 business days unless campaign timing says otherwise |

If an action depends on another task, date it after the dependency or leave it proposed until the dependency date is known.

## 7. Completed-task audit

For recently completed tasks:
- Verify acceptance criteria.
- Check whether the implementation exists.
- Evaluate the KPI only after a reasonable measurement period.
- Do not reopen solely because the task finished late.
- Reopen or create a follow-up only when implementation is incomplete, validation failed, or the expected outcome did not materialize after the measurement period.

## 8. Duplicate matching

Match against:
- Exact and semantic title similarity
- Same page/URL
- Same primary keyword
- Same technical issue
- Same success KPI
- Parent/child or dependency relationship

When a match exists, enrich or update the existing task rather than creating another.

## 9. Report-only Track

Track is not a Slingshot field and must not be included in customFields.

Infer Track only for rendering the report:
- Technical
- Product
- Content
- Backlinks

The underlying task remains governed by Category, Cluster, Recommendation, Page Type, title, and context.
