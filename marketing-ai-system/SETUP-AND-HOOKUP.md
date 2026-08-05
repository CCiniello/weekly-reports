# Setup and Hookup Guide

## 1. Repository placement

Place this entire `marketing-ai-system` folder at the root of:

`CCiniello/weekly-reports/marketing-ai-system/`

Keep the current report at:

`CCiniello/weekly-reports/seo/reveal/analysis/index.html`

Copy the attached approved HTML into:

`marketing-ai-system/08-templates/reveal-seo-canonical.html`

Do not move the production `index.html`; the template copy is a safety reference.

## 2. Cowork scheduled-task instruction

Replace the long duplicated scheduled prompt with a short bootstrap:

> Run the Reveal SEO Weekly production agent. Read and follow `marketing-ai-system/06-agents/reveal/seo-weekly/agent-instructions.md` and every required operating file it references. Use `seo/reveal/analysis/index.html` as the canonical live template and `marketing-ai-system/08-templates/reveal-seo-canonical.html` as the fallback safety copy. Execute autonomously. Do not redesign or simplify any artifact. If required task-field tokens or a source are unavailable, follow the documented failure rules and log the issue.

Schedule: Mondays, 5:00 AM, America/New_York.

## 3. Slingshot configuration still required

The shared link cannot by itself supply reliable API field metadata to this package. Record the following in:

`06-agents/reveal/seo-weekly/slingshot-field-map.md`

Required:
- Task type ID
- Field IDs
- Option IDs/tokens
- Status values
- Priority values
- Assignee write format
- Mention/comment write method
- Date format
- Two-step confirmation requirements

The agent must not invent these values.

## 4. Opportunity tracker

The agent must read:
- Opportunity Created Date
- Acquisition Medium
- Status

Filter Acquisition Medium = organic. Report:
- Opportunities created this month
- Prior-month comparison
- Current status distribution
- Any new organic opportunity since the last run

## 5. Test procedure

Run manually before enabling the schedule.

### Dry run
- Read all sources.
- Generate report to a temporary path.
- Produce proposed task writes without writing.
- Confirm goal is 50 organic leads.
- Confirm Tier 1 definition.
- Confirm organic opportunities.
- Confirm high-intent allowlist behavior.
- Confirm no design changes.

### Controlled write
- Allow updates to one matching existing task.
- Allow creation of at most one new task.
- Confirm Dian assignment + Sathya FYI for technical.
- Confirm all custom fields.
- Confirm no duplicate.

### Publish test
- Publish to a test branch or temporary report path.
- Open every tab.
- Test copy-summary.
- Test feedback modal.
- Test table/board/timeline.
- Compare CSS and DOM structure against canonical.

### Production launch
- Merge only after Casey approves the dry-run report and task writes.
- Enable Monday 5:00 AM schedule.
- Review the first three weekly run logs.
