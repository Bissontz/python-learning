#!/usr/bin/env python3
# quick script from last week — still works on my laptop, please don't judge
# pulls a few "alert-ish" rows from a local json dump and prints a summary
import json, sys, os

p = os.path.join(os.path.dirname(__file__), "sample_events.json")
# fallback if someone runs from elsewhere
if not os.path.exists(p):
    p = "sample_events.json"

try:
    f = open(p)
    data = json.load(f)
    f.close()
except:
    print("couldnt read file", p)
    sys.exit(1)

# sometimes the dump is a list, sometimes {"events": [...]}
if type(data) == dict and "events" in data:
    stuff = data["events"]
elif type(data) == list:
    stuff = data
else:
    print("weird shape")
    sys.exit(1)

cnt = 0
hi = []
locs = {}
for i in range(len(stuff)):
    row = stuff[i]
    # skip junk
    if row == None:
        continue
    if "id" not in row:
        continue
    sev = row["severity"] if "severity" in row else "unknown"
    # normalize a bit
    if sev == "HIGH" or sev == "high" or sev == "High" or sev == 3 or sev == "3":
        sev2 = "high"
    elif sev == "MED" or sev == "medium" or sev == "Medium" or sev == 2:
        sev2 = "medium"
    elif sev == "LOW" or sev == "low" or sev == 1:
        sev2 = "low"
    else:
        sev2 = str(sev).lower()
    loc = row["location"] if "location" in row else None
    if loc is None or loc == "":
        loc = "UNSPECIFIED"
    if loc not in locs:
        locs[loc] = 0
    locs[loc] = locs[loc] + 1
    cnt = cnt + 1
    if sev2 == "high":
        # keep a short blurb for the high ones
        who = row["actor"] if "actor" in row else "?"
        what = row["summary"] if "summary" in row else row["desc"] if "desc" in row else ""
        hi.append(str(row["id"]) + "|" + who + "|" + what[:80])

print("total usable rows:", cnt)
print("locations:")
# sort by count desc the hard way
keys = list(locs.keys())
for a in range(len(keys)):
    for b in range(a + 1, len(keys)):
        if locs[keys[a]] < locs[keys[b]]:
            tmp = keys[a]
            keys[a] = keys[b]
            keys[b] = tmp
for k in keys:
    print(" ", k, locs[k])
print("high severity snippets:")
if len(hi) == 0:
    print("  (none)")
else:
    for x in hi:
        print(" ", x)

# also write a tiny out file for later
out = os.path.join(os.path.dirname(__file__), "summary_out.txt")
try:
    g = open(out, "w")
    g.write("count=" + str(cnt) + "\n")
    g.write("high=" + str(len(hi)) + "\n")
    g.close()
except Exception as e:
    print("write failed", e)
