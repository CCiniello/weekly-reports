# Reveal SEO Dry Run Review — 2026-08-05

## Result

Overall: PASS WITH FIXES REQUIRED BEFORE PRODUCTION WRITES

## Passed

- Repository structure is correct.
- Operating files were accessible.
- Canonical report structure, CSS, JavaScript, tabs, and feedback behavior were preserved.
- GSC, GA4, Salesforce, Ahrefs, Amplitude, Slingshot task, and opportunity sources were accessible.
- New 50/month organic lead target appeared.
- Tier 1 organic lead calculation appeared.
- High-intent allowlist sessions appeared.
- Opportunity tracker data appeared.
- No tasks, comments, discussions, or GitHub files were changed in dry-run mode.

## Required fixes

1. AI data is inconsistent:
   - KPI/summary reported 31.3% and stale.
   - Detailed AI tiles still reported 27.4%, 7.9, 445, 80%, and called the report a fresh baseline.
   - Use one latest valid report consistently. If Aug 4 failed, use Jul 28 values everywhere and mark stale.

2. Footer is stale:
   - Footer says Generated Mon Aug 3, 2026.
   - Must match Aug 5 dry run or the production Monday date.

3. Cluster narrative mismatch:
   - Embedded Analytics row shows 4,150 impressions.
   - Verdict text says 4,120.
   - All repeated values must be identical.

4. Technical routing is not yet reflected:
   - Several technical tasks render Casey or Unassigned.
   - Controlled write test should update one existing technical task to Dian.
   - Sathya should be plain-text FYI only, not a co-owner/avatar.

5. Track is report-only:
   - Do not attempt to write Track.
   - Continue rendering inferred Track in the HTML.

6. Opportunity freshness:
   - Tracker has no new records after June.
   - Label tracker stale/incomplete.
   - Do not conclude demand created zero opportunities; conclude the tracker cannot prove newer opportunity creation.

7. Run log:
   - No prior run log is expected for the first run.
   - First controlled/production run must create the initial JSON log.

8. Salesforce connector identity:
   - Connector authenticated as Casey McGuigan.
   - Queries succeeded.
   - Confirm this is an approved service identity or accepted operating identity before unattended production.

## Controlled write recommendation

Use one existing technical task that is currently assigned to Casey or Unassigned.

Preferred candidate:
`301 redirect /glossary/embedded-bi-business-intelligence → /embedded-bi`

Test only:
- Assign Dian.
- Keep existing status, priority, dates, and custom fields unless a correction is required.
- Post plain-text FYI comment for Sathya.
- Re-read task.
- Verify assignment and comment.
- Do not create a new task in the same test.
