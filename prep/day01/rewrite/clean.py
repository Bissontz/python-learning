#!/usr/bin/env python3
import json, sys, os

def load_events(path):
    try:
        with open(path, "r") as inputFile:
            jsonData = json.load(inputFile)
    except Exception as e:
        sys.exit(f"Error reading {path}: {e}")

    if isinstance(jsonData, dict):
        return jsonData.get("events", [])
    elif isinstance(jsonData, list):
        return jsonData
    else:
        sys.exit("Unexpected JSON shape")

def normalize_severity(severity):
    """Normalize severity values to a standard set."""
    if isinstance(severity, str):
        severity = severity.lower()
    else:
        severity = str(severity).lower()

    if severity in ["high", "3"]:
        return "high"
    elif severity in ["medium", "med", "2"]:
        return "medium"
    elif severity in ["low", "1"]:
        return "low"
    else:
        return severity

def print_console_summary(rowCount, highEntries, locations):
    print("total usable rows:", rowCount)

    print("locations:")
    for loc, count in locations:
        print(" ", loc, count)

    print("high severity snippets:")
    if len(highEntries) == 0:
        print("  (none)")
    else:
        for x in highEntries:
            print(" ", x)

def write_summary_file(path, rowCount, highEntries):
    try:
        with open(path, "w") as g:
            g.write("count=" + str(rowCount) + "\n")
            g.write("high=" + str(len(highEntries)) + "\n")
    except Exception as e:
        sys.exit(f"Error writing {path}: {e}")

inFilePath = os.path.join(os.path.dirname(__file__), "sample_events.json")
# fallback if someone runs from elsewhere
if not os.path.exists(inFilePath):
    inFilePath = "sample_events.json"

entries = load_events(inFilePath)

rowCount = 0
highEntries = []
locations = {}

for i in range(len(entries)):
    row = entries[i]

    if row is None:
        continue
    if "id" not in row:
        continue

    severity = normalize_severity(row.get("severity", "unknown"))

    location = row.get("location") or "UNSPECIFIED"
    if location not in locations:
        locations[location] = 1
    else:
        locations[location] += 1

    if severity == "high":
        actor = row.get("actor", "?")
        summary = row.get("summary", row.get("desc", ""))
        highEntries.append(f"{row['id']}|{actor}|{summary[:80]}")

    rowCount += 1

locations = sorted(locations.items(), key=lambda x: x[1], reverse=True)

print_console_summary(rowCount, highEntries, locations)

outputFile = os.path.join(os.path.dirname(__file__), "summary_out.txt")
write_summary_file(outputFile, rowCount, highEntries)

