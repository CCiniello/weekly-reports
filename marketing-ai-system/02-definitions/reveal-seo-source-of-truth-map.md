# Reveal SEO Source-of-Truth Map

## Reporting timezone and windows

- Timezone: America/New_York (Eastern Time).
- Weekly current window: the last complete Monday–Sunday period.
- Weekly comparison window: the Monday–Sunday period immediately before it.
- GSC keyword and ranking-page tables: trailing 28 complete days ending on Sunday.
- Monthly lead and opportunity reporting: calendar month, through the latest complete available day. Label partial months clearly.
- Amplitude: use the latest completed report. Mark stale when it predates the current reporting window or when prompt coverage/sample size changed materially.

## Approved metrics

| Metric | Source of truth | Exact rule | Do not substitute |
|---|---|---|---|
| Reveal rankings | Google Search Console through Supermetrics | Account `sc-domain:revealbi.io`; query/query+page dimensions; position, clicks, impressions | Ahrefs Rank Tracker |
| Ranking page | Google Search Console | Actual page returned for the query | Ahrefs ranking URL |
| CTR | Google Search Console | clicks ÷ impressions for the same query/page/window | GA4 CTR or Ahrefs |
| Search volume | Ahrefs Keywords Explorer | Monthly estimated search volume | GSC impressions |
| Whitespace/net-new keyword research | Ahrefs | Approved discovery use only | GSC as market demand |
| Domain Rating | Ahrefs | Current DR | Any other authority score |
| Technical health | Ahrefs Site Audit | Mirror latest completed Site Audit 1241581; do not re-crawl weekly | GSC coverage |
| Organic sessions | GA4 through Supermetrics | `sessionMedium == organic`; report approved high-intent allowlist separately | GSC clicks |
| Organic leads | Salesforce `Lead_Event__c` | COUNT_DISTINCT(`Email__c`) where ProductFamilyName__c=`Reveal` and TrackingMedium__c=`organic` | GA4 conversions |
| Tier 1 organic leads | Salesforce `Lead_Event__c` | Above organic lead rules plus Lead Event Name contains `pricing quote`, `demo request`, or `gated demo` | Form fills from analytics |
| Organic opportunities | Slingshot opportunity tracker | Opportunity Created Date + Acquisition Medium=`organic`; status from the tracker Status field | Lead count or GA4 |
| AI visibility | Amplitude AI Visibility | Brand `Reveal BI`, orgBrandId 30690, latest completed report | Ahrefs Brand Radar |
| Task status and execution | Reveal SEO Slingshot tracker | Live task list, including fields, owners, dates, blockers, and status | Report-embedded task copy |

## Reveal goals

### Monthly acquisition mix
- Total Reveal leads: **250/month**
- Paid: **150/month**
- Organic: **50/month**
- Other — ABM, events, referral, and other sources: **50/month**

The prior 100-organic-lead target is retired and must not appear in new reports unless explicitly restored.

### SEO and authority goals
- `embedded analytics` → Top 3
- `white label analytics` → Top 3
- `/embedded-bi` page live and Top 10
- `/embedded-dashboards` page live and Top 10
- Technical health ≥60, then ≥90 by March 31, 2027
- Domain Rating 60 by March 31, 2027
- Organic high-intent sessions: target retained only after the approved allowlist baseline is recalculated
- Organic leads: 50/month
- Tier 1 organic lead quality must be reported when data is available
- Organic opportunity trend and status must be reported from the opportunity tracker

## High-intent organic-session allowlist

Normalize every URL before matching:
1. Convert to lowercase.
2. Remove protocol and host.
3. Remove query strings and fragments.
4. Normalize trailing slash consistently.
5. Resolve approved redirects and canonical replacements.
6. Treat an approved successor URL as part of the allowlist.
7. Add a new page automatically only when it is a documented high-intent Reveal money page, comparison page, pricing page, product page, solution page, or approved cluster page.
8. Log every automatic allowlist addition or replacement in the run log and Definitions tab.

Seed allowlist:

- `/`
- `/embedded-analytics-software`
- `/ai`
- `/white-label-analytics`
- `/features`
- `/pricing/embedded-analytics`
- `/isv-analytics`
- `/embedded-analytics-for-saas`
- `/manufacturing-analytics`
- `/healthcare-analytics`
- `/reveal-vs-power-bi`
- `/compare`
- `/reveal-vs-logi-analytics`
- `/reveal-vs-tableau`
- `/reveal-vs-metabase`
- `/reveal-vs-luzmo`
- `/reveal-vs-gooddata`
- `/reveal-vs-bold-bi`
- `/embedded-analytics`
- `/reveal-vs-looker`
- `/blog/white-label-analytics-platform`
- `/embedded-bi`
- `/white-label-embedded-analytics`
- `/blog/embedded-analytics-platforms`
- `/reveal-vs-sisense`
- `/reveal-vs-domo`
- `/blog/power-bi-embedded-alternative`
- `/reveal-vs-toucan-toco`

## Data-state labels

- **Fresh:** full expected window is available.
- **Partial:** source returned only part of the expected data.
- **Stale:** most recent result is older than the allowed reporting period.
- **Unavailable:** query, permission, connector, or source failed.
- **Rebaselined:** methodology, prompt set, sample size, or allowlist changed enough that trend comparison is invalid.

## Failure rules

- Never substitute Ahrefs rankings for GSC.
- Never substitute GA4 conversions for Salesforce leads.
- Never substitute Brand Radar for Amplitude.
- Never silently carry forward an old value.
- When critical goal data is unavailable, do not create metric-driven implementation tasks from that missing evidence.
