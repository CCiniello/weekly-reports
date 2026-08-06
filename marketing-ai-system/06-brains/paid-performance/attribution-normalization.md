# Paid Attribution Normalization

## Principle
Raw Salesforce tracking fields are inconsistent. Normalize using case-insensitive contains logic across source, medium, campaign, content, details, and tracking ID. Preserve raw fields in audit output.

## Base object
`Lead_Event__c`

## Reveal
Base: `ProductFamilyName__c = 'Reveal'`
Deduplicate: `COUNT_DISTINCT(Email__c)`
Tier-1 event name contains: `pricing quote`, `demo request`, or `gated demo`.
Exclude spam where the field is available.

## Channel rules
### Google
- TrackingMedium__c = cpc
- TrackingSource__c contains google
- Demand Gen may appear in campaign, content, or details; classify when any normalized field contains demandgen or demand gen

### Microsoft / Bing
- TrackingMedium__c = cpc
- TrackingSource__c contains bing or microsoft

### LinkedIn
- TrackingSource__c contains linked, including linkedin and linkedin.com
- Do not require exact medium until tracking is cleaned

### Reddit
- TrackingSource__c contains reddit
- Medium may be referral

## Ultimate
- Lead event name contains ultimate trial
- TrackingMedium__c = cpc
- Normalize source using channel rules

## Quality controls
- Deduplicate by email within the reporting window
- Display unclassified paid records
- Display conflicting source/campaign signals
- Never silently force an ambiguous record into a channel
- Assign attribution confidence: High / Medium / Low
