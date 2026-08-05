# Slingshot Field Map — Reveal SEO

Status: COMPLETE FOR PRODUCTION TEST

## Containers

- Task type name: SEO Optimization
- Task type ID: `e97e10ef_16ac6931-1f79-4dae-a048-4ef743748a43_ds`
- Section ID: `e97e10ef_2e972631-fe61-42cb-bf51-885002b7ce30_tg`
- Task list ID: `e97e10ef_0a775366-47ca-4550-8556-8d051ecc00b4_tg`
- Project ID: `e97e10ef_211fe76e-5670-47db-a46c-7311eb663c0a_proj`
- Workspace ID: `e97e10ef_88e81918-3a2f-40cb-91d9-72abf7bfe9d1_ws`

## Native fields

### Status
Write through native `statusId`, never through customFields.

Allowed:
- `status_open`
- `status_in_progress`
- `status_review`
- `status_blocked`
- `status_completed`

Special field ID, reference only:
`e97e10ef_9391b4ae-02cc-42eb-aba5-73429ad7743b_df`

### Priority
Write through native `priority`, never through customFields.

Allowed:
- `none`
- `low`
- `medium`
- `high`

Special field ID, reference only:
`e97e10ef_ae872d29-c108-49d9-8bb8-ba34ed75a1cf_df`

### Dates
Use ISO `YYYY-MM-DD`. Epoch seconds are accepted, but never use milliseconds.

### Assignees
Write as:
`assigneeIds = ["<user-id>"]`

- Casey Ciniello: `e97e10ef_8edef387-534e-46ef-855f-e8ada6810913_u`
- Dian Jelyazkov: `e97e10ef_37893533-0155-4227-9d66-09f76526cd63_u`
- Sathya Sundaresan: `e97e10ef_56afc171-14a5-4ac9-bd54-4ce83633a88e_u`

Technical tasks:
- Assign Dian only.
- Add a plain-text task comment:
  `FYI Sathya Sundaresan (ssundaresan@infragistics.com): <reason/context>`
- The available tool cannot create a native notifying @mention. Do not claim Sathya was notified.
- In reports, show Dian as Owner and Sathya as FYI, not as a second assignee.

## Custom fields

| Field | ID | Type | Allowed/write value |
|---|---|---|---|
| Product | `e97e10ef_09c93449-10dc-4d9a-9c0b-1312e9aec1ae_df` | dropdown | Reveal, Slingshot, App Builder, UI Tools |
| Category | `e97e10ef_60f90011-d946-4500-8638-e765ea65d002_df` | dropdown | SEO, LLM, Conversion, Technical, On-Page Content, Internal Linking, Engagement / CRO, Remarketing |
| Cluster | `e97e10ef_37f36102-2b8f-489d-ba23-66f19c82fae9_df` | dropdown | Technical, LLM visibility, Use cases, Marketing ICP, Compete, Brand, Templates, Embedded Analytics, Embedded BI, White Label, Embedded Dashboards |
| Effort | `e97e10ef_c61d635c-557b-487a-b5c0-eb2827f9a5dc_df` | dropdown | S, M, L |
| Primary SEO Keyword | `e97e10ef_343bc5c2-315e-445a-a927-bddfb5824000_df` | text | free text |
| Why it Matters | `e97e10ef_210c6355-524b-4e34-8cb8-634e95c91502_df` | longText | free text |
| Step by Step Fix | `e97e10ef_2ed3ae47-bfe8-487a-9667-7a491837977b_df` | longText | free text |
| Current Rankings | `e97e10ef_67f3b6fe-5f07-4b9d-87c1-fdfa0726617d_df` | longText | free text |
| Insight | `e97e10ef_a24cc67f-4c06-4cbf-b3a1-79aea6aced8a_df` | longText | free text |
| Success KPI | `e97e10ef_afa3e47d-c4ad-401c-931c-6d2f3cdba223_df` | longText | free text |
| Acceptance Criteria | `e97e10ef_078e7446-0d42-43d5-bab4-40685b76b709_df` | longText | free text |
| Link to URL | `e97e10ef_25869c3e-6979-4cbb-9069-4eff75e69f51_df` | text | URL/path |
| Reccomendation | `e97e10ef_170f6641-38c3-4c72-80cb-2946fc73b18d_df` | dropdown | Optimize, Rewrite, REDIRECT, FIX, KEEP AS-IS, DELETE, NOINDEX, CREATE, INVESTIGATE, AUDIT, KEEP |
| Reason | `e97e10ef_f596bb17-107c-402b-91cc-2b195672ce77_df` | longText | free text |
| Page Type | `e97e10ef_001f6a85-ecdc-45f1-b303-7866e62da6bb_df` | dropdown | Blog, Product, Comparison, Glossary, Head / guide page, Off-domain, Homepage (long-tail anchor) |
| Breaking Change Milestone | `e97e10ef_7e1ba2e9-5c74-4769-80fa-61b1a6377647_df` | checkbox | boolean |
| Deferred Reason | `e97e10ef_667e63be-dd76-4923-b7f7-5bbe945b67e4_df` | longText | free text |

## Track

There is no writable Track field.

- Track is report-only and inferred from Category, Recommendation, Page Type, task title, and task context.
- Never attempt to write Track to Slingshot.
- Recommended report mapping:
  - Technical → Technical
  - LLM → Content
  - On-Page Content / Internal Linking → Content
  - Compete cluster or Comparison page type → Content
  - Link-earning work → Backlinks
  - New Product page → Product

## Write tools

- Create: `mcp__Slingshot__slingshot_create_task`
- Update: `mcp__Slingshot__slingshot_update_task`
- Comment: `mcp__Slingshot__slingshot_post_task_message`
- Verify task: `mcp__Slingshot__slingshot_get_task`
- Verify comment: `mcp__Slingshot__slingshot_list_task_messages`

## Two-step confirmation

For create, update, and comment:
1. Call without `confirmationToken`.
2. Inspect preview and validation.
3. Call the same tool with identical parameters plus returned `confirmationToken`.
4. Re-read the task and verify fields, assignee, dates, status, priority, custom fields, and `modifiedAt`.
5. For comments, verify the new feed entry/message count.

Never reuse a confirmation token for different parameters.
