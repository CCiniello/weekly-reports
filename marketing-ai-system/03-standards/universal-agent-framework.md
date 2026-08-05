# Universal Agent Framework

## Phase 0 — Initialize

- Set report date and reporting windows.
- Load the approved operating files.
- Confirm product, channel, owner, destinations, and task limits.
- Confirm that the canonical template is accessible.

Stop and log a configuration failure when a required destination, identifier, or canonical template is missing.

## Phase 1 — Context and feedback

Read in this order:
1. Marketing Constitution
2. Product goals and current-quarter priorities
3. Metric definitions and source map
4. Task creation and report standards
5. New feedback
6. Standing applied-feedback log
7. Current relevant tracker
8. Recently completed tasks
9. Prior report and prior run log

Produce an internal context summary:
- Goals
- Current priorities
- Standing decisions
- Open work
- Blockers
- Questions
- Actions that must not be recommended

## Phase 2 — Data collection

- Validate each source independently.
- Record Fresh, Partial, Stale, Unavailable, or Rebaselined.
- Pull raw data without making recommendations during collection.
- Preserve query parameters and windows in the run log.
- Never replace a failed source.

## Phase 3 — Analysis

Analyze:
- Goal progress
- Week-over-week and month-to-date change
- Quality vs volume
- High-intent vs vanity traffic
- Opportunity creation and status
- What changed in the work tracker
- Whether completed work produced the expected result
- Leading and lagging indicators
- Risks and forecast

Separate:
- Observation
- Interpretation
- Recommendation
- Assumption

## Phase 4 — Recommendation prioritization

- Generate candidate actions.
- Score each action.
- Remove duplicates, rejected work, unsupported ideas, and blocked actions.
- Select no more than the permitted task limit.
- Designate no more than three weekly priorities.
- Put medium-confidence ideas in Proposed Actions/Open Questions.

## Phase 5 — Task sync

- Match existing tasks first.
- Update existing tasks when appropriate.
- Create only genuinely new tasks.
- Populate every required field.
- Apply owner and date rules.
- Confirm the write succeeded.
- Record created and updated task IDs.

## Phase 6 — Artifact update

- Copy the canonical prior HTML.
- Replace only permitted run-specific values.
- Preserve exact structure, CSS, JS, classes, feedback block, and interactions.
- Render Tasks from the synced tracker.
- Validate all tabs, buttons, tables, links, and responsive behavior.

## Phase 7 — Publish

- Save the dated artifact.
- Replace the approved latest-report path.
- Commit only the approved file(s).
- Post the story-first team summary.
- Post the applied-feedback log.
- Save the machine-readable run log.

## Phase 8 — Self-evaluation

Score the run:
- Data completeness
- Source compliance
- Goal alignment
- Duplicate prevention
- Task completeness
- Report-structure preservation
- Feedback application
- Forecast confidence
- Publication success

Do not label the run successful if a critical write, publication, or source-of-truth rule failed.
