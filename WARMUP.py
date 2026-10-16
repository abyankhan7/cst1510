# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
labels = ["R-001", "R-002", "R-003"]
print(labels[2]) #index 3 is out of range

# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
record = {"label": "R-001", "value": 87.0, "limit": 100.0}
print(record["value"]) # status not in the dict

# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

with open("records.txt", "r") as f:
    print(f.read())