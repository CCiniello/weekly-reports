# Reveal SEO Configuration
Status: LIVE
Schedule: Monday 5:00 AM America/New_York

Business lead OKRs (context — do NOT alter here; separate from the SEO KPI below): 250 total leads/month; 150 paid; 50 organic; 50 other.

SEO organic-lead KPI (CANONICAL — this is the numerator for the 50/mo SEO-program goal):
- Metric: 50 deduplicated Tier-1 organic leads per month.
- Source: Salesforce Lead_Event__c.
- Filters (ALL must apply, in this order):
  1. ProductFamilyName__c = Reveal
  2. TrackingMedium__c = organic
  3. Tier-1 events only: Lead Event Name contains "pricing quote", "demo request", or "gated demo"
  4. Exclude spam / disqualified records per the shared Reveal lead-quality rule
  5. Dedupe by unique email (COUNT_DISTINCT Email__c) AFTER filters 1–4
- Each run: COMPUTE the current value fresh with this exact definition before calculating progress vs 50. Do NOT carry a prior all-organic figure forward as Tier-1 (e.g. the 23 on the Aug 7 brief was the broader all-organic deduped count, not Tier-1).
- Supporting context (optional): the broader all-organic deduped count (Reveal + organic, dedupe email, no Tier-1 filter) may be shown as context, but is NEVER the numerator for the 50 Tier-1 SEO goal.
- If the shared lead-quality (spam/disqualified) rule can't be located at run time, flag it in the brief rather than silently skipping the exclusion.
Sources: GSC sc-domain:revealbi.io; GA4 516472465; Ahrefs; Amplitude Reveal BI orgBrandId 30690; opportunity tracker e97e10ef_da444fd7-abbc-4c97-929a-b1a6fac46235_tg.
Tasks: list e97e10ef_0a775366-47ca-4550-8556-8d051ecc00b4_tg; section e97e10ef_2e972631-fe61-42cb-bf51-885002b7ce30_tg.
Report: seo/reveal/analysis/index.html.
Routing: Technical → Dian e97e10ef_37893533-0155-4227-9d66-09f76526cd63_u; plain-text FYI Sathya only. Other → Casey e97e10ef_8edef387-534e-46ef-855f-e8ada6810913_u.
