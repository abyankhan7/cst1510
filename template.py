# Name  : Abyan khan
# Lane  :  AI
# Date  : 16 October 2026
# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def status_of(percent):
    # return status based on percentage
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    # calculate and return difference and percentage
    difference = limit - value
    percentage = (value / limit) * 100
    status = status_of(percentage)
    return difference, percentage, status

def print_report(label, value, limit, difference, percentage, status):
    difference, percentage, status = check(value, limit)
    status = status_of(percentage)
    print("Label:", label)
    print("Value:", value)
    print("Limit:", limit)
    print("Difference:", difference)
    print("Percent:", round(percentage, 2))
    print("Status:", status)


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

  # replace with your code
def load_records(path):
    records = []
    try:
        with open(path, "r") as file:
            for line in file:
                label, value, limit = line.strip().split(",")
                records.append({
                    "label": label,
                    "value": float(value),
                    "limit": float(limit)
                })
    except FileNotFoundError:
        print("Error: file not found.")
    return records


def main():
    records = load_records("records_sample.txt")
    with open("results.txt", "w") as output:
        for record in records:
            label = record["label"]
            value = record["value"]
            limit = record["limit"]
            difference, percent, status = check(value, limit)
            print_report(label, value, limit, difference, percent, status)
            output.write(f"{label},{status}\n")
    with open("results.txt", "r") as output:
        print(output.read(), end="")
main()


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
count = 0
for record in load_records("records_sample.txt"):
    label = record["label"]
    value = record["value"]
    limit = record["limit"]
    difference, percent, status = check(value, limit)
    print_report(label, value, limit, difference, percent, status)
    if status == "OVER LIMIT":
        count = count + 1
print("THE TOTAL OVER LIMIT COUNT IS :", count)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job