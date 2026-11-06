
# Name  : ABYAN KHAN
# Lane  :  AI    (delete two)
# Date  : 6 NOVEMBER 2026



import pandas as pd

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

data = pd.read_csv("mysample_csv.csv")  # replace with pd.read_csv("your_file.csv")



# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

# your column(s) go here
data["percent"] = ((data["value"] / data["limit"]) * 100).round(1)
status = lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
data["status"] = data["percent"].apply(status)


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

print(data)

print(data[(data["status"] != "OK")])

grouped = (data.groupby("status"))
print(data["status"].value_counts())
data.to_csv("newsample_record.csv", index=False)

import matplotlib.pyplot as plt
data["status"].value_counts().plot(kind="bar", title="Count Status")
plt.tight_layout()
plt.figure()
plt.savefig("counts_status.png")
plt.show()

# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case