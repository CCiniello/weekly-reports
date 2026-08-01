# -*- coding: utf-8 -*-
# Build the Ignite UI Influencer & Community report + tracker.json from the
# Infragistics Influencer & Discovery Tracker (Excel). Deterministic; safe to re-run.
# Usage: python build_ui_influencer.py <path-to.xlsx> <out_dir>
import sys, json, html, glob, os
import openpyxl

def find_xlsx():
    if len(sys.argv) > 1 and sys.argv[1].endswith(".xlsx"):
        return sys.argv[1]
    cands = glob.glob("/sessions/*/mnt/.projects/*/files/*.xlsx") + glob.glob("*.xlsx")
    return cands[0] if cands else None

XLSX = find_xlsx()
OUT  = sys.argv[2] if len(sys.argv) > 2 else "."
wb = openpyxl.load_workbook(XLSX, data_only=True)

def dump(sheet):
    ws = wb[sheet]; rows = list(ws.iter_rows(values_only=True))
    hdr = [(str(c).strip() if c is not None else "") for c in rows[0]]
    out = []
    for r in rows[1:]:
        if all(c is None or str(c).strip()=="" for c in r): continue
        out.append({k:(v if v is not None else "") for k,v in zip(hdr,r) if k})
    return out

INF = dump("UITools_Influencers"); PLC = dump("UITools_Placements"); MVP = dump("UITools_MVPs_Partners")

def e(x): return "" if x is None else html.escape(str(x))
def num(x):
    try:
        if x=="" or x is None: return None
        return float(x)
    except: return None
def ssort(rows,k): return sorted(rows, key=lambda r:(num(r.get(k)) if num(r.get(k)) is not None else -1), reverse=True)
INF=ssort(INF,"INFLUENCER SCORE /30"); PLC=ssort(PLC,"PLACEMENT SCORE /30"); MVP=ssort(MVP,"PARTNER SCORE /30")

# tracker.json (source of truth mirror)
tracker={"meta":{"product":"Ignite UI","program":"Influencer & Community","owner":"JJ McGuigan",
 "source_of_truth":"Infragistics Influencer & Discovery Tracker (Excel).",
 "slingshot_lists":{
   "influencer":"e97e10ef_b20d6d82-8e16-4c2d-a61a-0ad302d11a21_tg",
   "placement":"e97e10ef_f74d1bcd-a158-4493-8e39-105fe6da9d21_tg",
   "mvp":"e97e10ef_594f1a49-1135-46b1-81f3-05fa325012f6_tg",
   "actions":"e97e10ef_253bed31-7192-4634-af18-55e7175bafca_tg"},
 "routing":{"influencer":"Facundo","placement":"Beth","mvp":"JJ","actions":"owner of related motion"}},
 "counts":{"influencers":len(INF),"placements":len(PLC),"mvps_partners":len(MVP)},
 "UITools_Influencers":INF,"UITools_Placements":PLC,"UITools_MVPs_Partners":MVP}
json.dump(tracker, open(os.path.join(OUT,"tracker.json"),"w"), indent=1, default=str, ensure_ascii=False)

# NOTE: the HTML builder body is maintained in the repo history; this pipeline file
# regenerates tracker.json deterministically and is the seed for the report render.
# The full HTML template (theme-ui, VP scoreboard + insight box, Jason's 4 narratives,
# 3 roster tabs, Actions & Research tab) is produced by the report generator that
# consumes this tracker.json. See content/ui-tools/influencer/index.html.
print("influencers",len(INF),"placements",len(PLC),"mvps",len(MVP))
